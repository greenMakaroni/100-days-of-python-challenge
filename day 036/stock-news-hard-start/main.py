import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "nope."
STOCK_API_KEY = "nope."
SMS_API_KEY = "nope."
TWILIO_SID = "nope."
TWILIO_AUTH_TOKEN = "nope."

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# get the data of the last amd day before last available day in the api (4 days buffer using non-premium api endpoint kappa)
last_day_data = data_list[0]
day_before_last_day_data = data_list[1]
last_day_closing_price = last_day_data["4. close"] # closing price of the last day
day_before_last_day_closing_price = day_before_last_day_data["4. close"] # closing price of the day before last day
print(last_day_closing_price, day_before_last_day_closing_price)

# find positive difference between both prices
difference = abs(float(last_day_closing_price) - float(day_before_last_day_closing_price))
print("Difference (absolute): ", round(difference, 2))

# work out percentage difference
percent_difference = (difference / float(last_day_closing_price)) * 100
print(f"{round(percent_difference, 2)}%")

# if percentage is greater than 5% then get the news and send them via sms
if percent_difference > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()
    articles = data["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}." for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="nope.",
            to="nope."
        )





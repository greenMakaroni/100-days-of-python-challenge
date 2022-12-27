import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = ""
STOCK_API_KEY = ""
SMS_API_KEY = ""

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
    print("Get News!")
else:
    print("No news!")

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import smtplib
import datetime as dt
from random import choice

bot_email = "edfrghnergt3488923hnf@gmail.com"
bot_password = "DON'T PUSH YOUR PASSWORDS TO GITHUB"
my_email = "radical.dave.software@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

# 0 = MONDAY
if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        today_quote = choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        try:
            connection.login(bot_email, bot_password)
            connection.sendmail(
                from_addr=bot_email,
                to_addrs=my_email,
                msg=f"Subject: Monday motivation quote\n\n{today_quote}"
            )
        except:
            print("Something went wrong!")
        else:
            print("Email sent!")
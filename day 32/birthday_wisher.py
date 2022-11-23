# Use pythonanywhere cloud hosting to upload the python file and schedule it to run at specified time of day, week, year etc...

import datetime as dt
import pandas
from random import choice
import smtplib

email_host = "smtp.gmail.com"
bot_email = "edfrghnergt3488923hnf@gmail.com"
bot_password = "DON'T PUSH YOUR PASSWORDS TO GITHUB"

# create a tuple from today's month and day using datetime
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# use pandas to read birthdays.csv
data = pandas.read_csv("birthdays.csv")

# create dictionary of birthdays using dictionary comprehensions
birthdays = { (data_row.month, data_row.day) : data_row for (index, data_row) in data.iterrows() }

# check if today_tuple is in birthdays dictionary to see if there's somebody's birthday today.
if today_tuple in birthdays:
    birthday_person = birthdays[today_tuple]
    # pick random letter template
    file_path = f"./letter_templates/letter_{choice(range(1, 4))}.txt"

    # use replace() method to replace [NAME] placeholder inside letter template
    with open(file_path) as letter:
        text = letter.read()
        formatted_text = text.replace("[NAME]", birthday_person["name"])

    # open smtp connection
    with smtplib.SMTP(email_host) as connection:
        # secure the connection
        connection.starttls()
        try:
            #login to our bot acc
            connection.login(user=bot_email, password=bot_password)
        except:
            print("Something went wrong")
        else:
            #send mail
            connection.sendmail(
                from_addr=bot_email,
                to_addrs="radical.dave.software@gmail.com",
                msg=f"Subject: Happy Birthday {birthday_person['name']}!\n\n {formatted_text}")
            print("Mail sent!")







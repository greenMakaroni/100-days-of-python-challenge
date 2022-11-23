# import smtplib
#
# my_email = "edfrghnergt3488923hnf@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     try:
#         connection.login(user=my_email, password="DON'T PUSH YOUR PASSWORDS TO GITHUB")
#         connection.sendmail(from_addr=my_email, to_addrs="radical.dave.software@gmail.com", msg="Subject:Happy Birthday!\n\n Muahahahaha")
#         # connection.close() // with smtlib as connection closes connection automatically
#     except:
#         print("Something went wrong")
#     else:
#         print("Email sent!")

import datetime as dt

current_time = dt.datetime.now()

print(
    f"Year: {current_time.year},\n"
    f"Month: {current_time.month},\n"
    f"Day: {current_time.day},\n"
    f"Hour: {current_time.hour},\n"
    f"Minute: {current_time.minute},\n"
    f"Second: {current_time.second},\n"
    f"Microsecond: {current_time.microsecond},\n"
    f"Weekday: {current_time.weekday()}")

my_birthday = dt.datetime(year=1995, month=11, day=9, hour=12)
print(my_birthday)


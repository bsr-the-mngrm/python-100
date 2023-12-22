# import smtplib
# import os
# from dotenv import load_dotenv
#
# load_dotenv('env/.env')
#
# sender_email = os.getenv('SENDER_EMAIL')
# sender_password = os.getenv('SENDER_APP_KEY')
# recipient_email = os.getenv('RECIPIENT_EMAIL')
#
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=sender_email, password=sender_password)
#     connection.sendmail(
#         from_addr=sender_email,
#         to_addrs=recipient_email,
#         msg="Subject: Testing\n\nHello SMTP!"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1900, month=1, day=1, hour=4, minute=49)
print(date_of_birth)

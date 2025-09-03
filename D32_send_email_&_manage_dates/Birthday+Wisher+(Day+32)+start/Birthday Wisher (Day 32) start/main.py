import smtplib

# should open 2-step authentication
app_psw="znzersqfjymthjwc"
yahoo_email="joytestingpython@yahoo.com"
gmail="joy481339@gmail.com"

# connection=smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=gmail,password=app_psw)
# connection.sendmail(from_addr=gmail,to_addrs=yahoo_email,msg="hello")
# connection.close()

# method 2
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=gmail,password=app_psw)
#     connection.sendmail(from_addr=gmail,to_addrs=yahoo_email,msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt
import pandas
import random

# now=dt.datetime.now()
# print(now.year,now.month,now.day)
# print(now)
# date_of_birth=dt.datetime(year=1995,month=12,day=31)
# print(date_of_birth)

# send motivational quotes on Monday via email
now=dt.datetime.now()
weekday=now.weekday()
if weekday==1:
    with open("quotes.txt") as f:
        quotes=f.readlines() #get a list
        choose_quote=random.choice(quotes)

    print(choose_quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()# secure connection
        connection.login(user=gmail,password=app_psw)
        connection.sendmail(from_addr=gmail,to_addrs=yahoo_email,msg=f"Subject:Motivational Quotes of Monday \n\n{choose_quote}")


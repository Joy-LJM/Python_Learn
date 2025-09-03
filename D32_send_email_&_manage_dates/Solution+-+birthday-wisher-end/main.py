import pandas
import datetime as dt
import smtplib
import random

APP_PSW= "znzersqfjymthjwc"
GMAIL= "joy481339@gmail.com"

time=dt.datetime.now()
today_tuple=(time.month, time.day) #used as dict key

birthdays=pandas.read_csv("birthdays.csv")
birthdays_dict={ (row.month,row.day):row for (index,row) in birthdays.iterrows()}

# if not birthdays_dict.get(today_tuple).empty :
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    filepath=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as f:
        contents=f.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(GMAIL, APP_PSW)
        connection.sendmail(from_addr=GMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{contents}")

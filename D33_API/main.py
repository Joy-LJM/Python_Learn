import requests
import datetime as dt
import smtplib
import time
# Add the os and dotenv modules
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MY_LAG= 43.652382
MY_LONG=-79.383736

GMAIL=os.environ['GMAIL']
APP_PSW=os.environ['APP_PSW']

def is_iss_overhead():
    # api of International Space Station
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])
    # my position is within +5 or -5 degree of the iss position
    if MY_LAG-5<=iss_latitude<=MY_LAG+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True
    return False

def is_night():
    parameter={
        "lat":MY_LAG,
        "lng":MY_LONG,
        "formatted":0
    }
    sun_response=requests.get("https://api.sunrise-sunset.org/json",params=parameter)
    sun_response.raise_for_status()
    results=sun_response.json()["results"]
    sunrise_hour=int(results['sunrise'].split('T')[1].split(':')[0])
    sunset_hour=int(results['sunset'].split('T')[1].split(':')[0])

    current_time=dt.datetime.now().hour

    if current_time <= sunrise_hour or current_time >= sunset_hour:
        return True
    return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=GMAIL,password=APP_PSW)
            connection.sendmail(from_addr=GMAIL,to_addrs=GMAIL,msg="Subject:ISS Overhead\n\nLook up! ISS is above you in the sky.")



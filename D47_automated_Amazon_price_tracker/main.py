import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

email=os.getenv("EMAIL_ADDRESS")
app_psw=os.getenv("APP_PSW")
smtp_server=os.getenv("SMTP_ADDRESS")
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0","Accept-Language":"en-US"}


product_res=requests.get(url=URL,headers=headers)
soup=BeautifulSoup(product_res.text,"html.parser")

print(soup.prettify())

price=soup.find(name='span', attrs={"class":"a-offscreen"}).getText()

# Remove the dollar sign using split
price_without_currency=price.replace("CAD","")

# Convert to floating point number
price_as_float=float(price_without_currency)
print(price_as_float)

# config email connection
TARGET_PRICE=120
if price_as_float<TARGET_PRICE:
    product_title = soup.find(id="productTitle").getText().strip()
    msg=f'{product_title} is now ${price_as_float}!\n{URL}'
    email_content = f'Subject: Amazon Price Alert!\n\n{msg}'

    with smtplib.SMTP(smtp_server, 587) as connection:
        connection.starttls()
        connection.login(email, app_psw)
        connection.sendmail(from_addr=email,msg=email_content.encode("utf-8"),to_addrs=email)
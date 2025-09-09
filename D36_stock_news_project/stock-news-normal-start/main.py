import requests
import datetime as dt
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY= "NRX152PHCWOPD7VT"
NEWS_API_KEY="11c016deffc34b108a57469f82bf4f71"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get yesterday's closing stock price
response=requests.get(f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}")
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()] #items():contains the key-value pairs of the dictionary, as tuples in a list
yesterday_closing_price= data_list[0]["4. close"]

#Get the day before yesterday's closing stock price
day_before_yesterday_closing_price= data_list[1]["4. close"]

#Find the positive difference, e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_price=float(yesterday_closing_price)-float(day_before_yesterday_closing_price) #absolute value of the specified number: 4.44
up_down=None
if difference_price>0:
    up_down="⬆️"
else:
    up_down="⬇️"
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage=round(abs(difference_price)/float(yesterday_closing_price)*100)

# If difference percentage is greater than 5 then print("Get News").
if diff_percentage> 1:
    #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT,{"apiKey":NEWS_API_KEY,"qInTitle":COMPANY_NAME})
    articles=news_response.json()["articles"]
    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles= articles[:3]

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles=[f"{STOCK_NAME}:{up_down}{diff_percentage}%\nHeadline:{article['title']}\nBrief:{article['description']}" for article in three_articles]

    #Send each article as a separate message via Twilio.
    APP_PSW= "znzersqfjymthjwc"
    GMAIL= "joy481339@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(GMAIL, APP_PSW)
        for msg in formatted_articles:
            connection.sendmail(from_addr=GMAIL, to_addrs=GMAIL, msg=msg)


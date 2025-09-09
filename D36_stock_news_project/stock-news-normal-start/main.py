import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY= "NRX152PHCWOPD7VT"
NEWS_API_KEY="11c016deffc34b108a57469f82bf4f71"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response=requests.get(f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}")
data=response.json()
print(data)
yesterday_time=str(dt.datetime.today() - dt.timedelta(days=1)).split(" ")[0]#2025-09-08(Monday)
yesterday_data=data["Time Series (Daily)"][yesterday_time]
yesterday_closing_price=[value for (key,value) in yesterday_data.items() if key=="4. close"] #346.4000

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_time=str(dt.datetime.today() - dt.timedelta(days=4)).split(" ")[0] ##2025-09-05(Friday)
before_yesterday_data=data["Time Series (Daily)"][before_yesterday_time]
before_yesterday_closing_price=[value for (key,value) in before_yesterday_data.items() if key=="4. close"] #350.8400

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_price=abs(yesterday_closing_price[0]-before_yesterday_data[0]) #absolute value of the specified number: 4.44

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage=(difference_price/before_yesterday_closing_price)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage>=5:
    print("Get news")
    news_response = requests.get(NEWS_ENDPOINT,{"apiKey":NEWS_API_KEY,"q":COMPANY_NAME})
    articles=news_response.json()["articles"]
    articles.slice(0,3)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


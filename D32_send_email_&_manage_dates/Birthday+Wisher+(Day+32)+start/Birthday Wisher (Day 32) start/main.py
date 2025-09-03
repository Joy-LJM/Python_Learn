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

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=gmail,password=app_psw)
    connection.sendmail(from_addr=gmail,to_addrs=yahoo_email,msg="Subject:Hello\n\nThis is the body of my email")
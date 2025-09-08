import requests

API_KEY="9413021806979ce883dc89aaec876344"
MY_LAG= 43.652382
MY_LONG=-79.383736

parameter={
    "lat":MY_LAG,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4
}

# need to set content-type or there will be 401 error
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter,headers={"Content-Type":"application/json"})
response.raise_for_status()
weather_data=response.json()
lists=weather_data["list"]
will_rain=False
print(lists)
for item in lists:
   condition_code=item["weather"][0]["id"]
   if int(condition_code)<700:
       will_rain=True
if will_rain:
    print("Bring an umbrella!")

print(response.status_code)

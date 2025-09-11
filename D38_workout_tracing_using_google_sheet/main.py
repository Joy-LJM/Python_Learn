import requests
import datetime
import os

# set environment variables
# os.environ["NUTRITIONIX_APP_ID"]="cac36e9b"
# os.environ["NUTRITIONIX_APP_KEY"]="4b3cdd6e809f0f7c3e7f35d8482ecc2d"
# os.environ["NUTRITIONIX_ENDPOINT"]="https://trackapi.nutritionix.com"
# os.environ["SHEETY_AUTH_TOKEN"]="Basic am95OmxlYXJuaW5n"
#get an environment variable： Actual values are stored as environment variables： Run->Edit configuration
NUTRITIONIX_APP_ID= os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_APP_KEY= os.environ["NUTRITIONIX_APP_KEY"]
NUTRITIONIX_ENDPOINT=os.environ["NUTRITIONIX_ENDPOINT"]
SHEETY_AUTH_TOKEN=os.environ["SHEETY_AUTH_TOKEN"]

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

answer=input("Tell me which exercise you did: ")
parameter={
    "query":answer,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers={
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
    'Content-Type': 'application/json',
}

exercise_response=requests.post(f"{NUTRITIONIX_ENDPOINT}/v2/natural/exercise",json=parameter,headers=headers)
exercise_response.raise_for_status()
exercise_data=exercise_response.json()["exercises"]

GOOGLE_SHEET_NAME = "workout"

for exercise in exercise_data:
    exercise_type=exercise["name"].title()
    duration_min=exercise["duration_min"]
    calories=exercise["nf_calories"]
    date=datetime.date.today().strftime("%d/%m/%Y")
    time=datetime.datetime.now().strftime("%X") # %H:%M:%S

    # sheety api set up
    sheety_param={
        GOOGLE_SHEET_NAME:{
            "date":date,
            "time":time,
            "calories":calories,
            "duration":duration_min,
            "exercise":exercise_type,
        }
    }
    sheety_res=requests.post(
        url="https://api.sheety.co/fa06f3b40577c9ef38ad6c1ade34ca6b/myWorkouts/workouts",
        json=sheety_param,
        headers={
            'Content-Type': 'application/json',
            "Authorization": SHEETY_AUTH_TOKEN # as authentication set into "basic"  in sheety
        }
    )
    print(sheety_res.json())
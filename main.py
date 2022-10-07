import requests
from datetime import datetime as dt
GENDER = "Male"
WEIGHT_KG = 65
HEIGHT_CM = 174
AGE = 22

APP_ID="85f1159e"
API_KEY="170bb9e7036c9a49462b707c8f595ed1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)
##########Dealing with sheety

sheet_endpoint="https://api.sheety.co/25625e1188e03ed6296be01fd8862fce/workouts2/workouts"
today_date=dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)



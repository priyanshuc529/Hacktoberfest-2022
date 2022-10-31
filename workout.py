import os
import requests
import datetime
exc_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY

}
parameter = {
    "query":f"{input('what execersise did you do today ?')}"
}

workout_updater = "https://api.sheety.co/e10af357f12484e1b6c8de611b5abcfe/myWorkouts/workouts"

dt = datetime.date.today()
time = datetime.datetime.now()

response = requests.post(url=exc_endpoint,json=parameter ,headers = header)

for exercise in response.json()["exercises"]:
    new_parameter = {

        "workout":{
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
            "exercise":exercise["user_input"],
            "date":dt.strftime("%d/%m/%Y"),
            "time":time.strftime("%H:%M:%S")
    }

}
    header_new = {
        'Authorization': 'Bearer dhbdophduwhdkjbdmwldwbnwbdwmdljdbjdbwldvwkd'
    }





    new_respnse = requests.post(url=workout_updater,json=new_parameter,headers = header_new)
    print(new_respnse.text)

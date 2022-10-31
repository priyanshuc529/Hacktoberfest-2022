import requests
MY_LONG = input("your longitude")
MY_LAT = input("You latitude")
# response  = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude =  response.json()["iss_position"]["latitude"]
#
# position_of_iss = (longitude,latitude)
# print(position_of_iss)

parameter = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}


sunrise = requests.get(url= "https://api.sunrise-sunset.org/json",params=parameter).json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = requests.get(url= "https://api.sunrise-sunset.org/json",params=parameter).json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset,sunrise)

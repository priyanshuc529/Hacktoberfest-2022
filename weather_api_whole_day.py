

import requests
# from bs4 import BeautifulSoup as bs
# print("Enter city name: ")
# city_name = input()

response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key= &q=Hyderabad&days=4")


rainy= {'Torrential rain shower',  'Freezing drizzle',  'Heavy rain at times', 'Light freezing rain', 'Heavy rain', 'Light rain shower', 'Moderate rain at times', 'Moderate or heavy sleet showers', 'Patchy light drizzle',  'Moderate rain', 'Light sleet', 'Light drizzle', 'Patchy rain possible', 'Moderate or heavy sleet', 'Heavy freezing drizzle', 'Patchy freezing drizzle possible', 'Moderate or heavy rain with thunder', 'Light sleet showers', 'Patchy light rain with thunder',  'Patchy light rain', 'Moderate or heavy rain shower', 'Moderate or heavy freezing rain', 'Thundery outbreaks possible', 'Light rain', 'Patchy sleet possible'}

NoRain = ['Clear',
'Overcast',
'Sunny',
'Cloudy',
'Partly cloudy']

resjson = response.json()
location = resjson['location']
city = location['name']
region = location['region']
country = location['country']
current_time = location['localtime'] 
weather_status = resjson['current']['condition']['text']

print(f'City : {city}, Region : {region} , Country : {country} , Current_weather_status : {weather_status} , Current_Time : {current_time}')
print("Day wise")
# for i in range(3):
for j in range(24):
    print(resjson['forecast']['forecastday'][0]['hour'][j]['time'],resjson['forecast']['forecastday'][1]['hour'][j]['condition']['text'])
    x = resjson['forecast']['forecastday'][0]['hour'][j]['condition']['text']
if x in rainy:
        print("Its going to rain")
elif x in NoRain:
        print("Sunny")
else:
        print("foggy or snow")





import requests
# from bs4 import BeautifulSoup as bs
response = requests.get("http://api.weatherapi.com/v1/current.json?key=&q=Hyderabad")
resjson = response.json()
location = resjson['location']
city = location['name']
region = location['region']
country = location['country']
time = location['localtime'] 
weather_status = resjson['current']['condition']['text']

print(f'City : {city}, Region : {region} , Country : {country} , weather_status : {weather_status} , Time : {time}')



# soup = bs(r.content,"html.parser")
# x = soup.find("location")
# print(x.text)

# import json

# f = open('options.json')
# data = json.load(f)
# day = set()
# night = set()


# print(len(data))
# for i in range(len(data)):
#     day.add(data[i]['day'])
#     night.add(data[i]['night'])

# print(f"Days: {day} ,\n  Night : {night}")
# s = day.union(night)

# print(s,len(s))

# f.close()



# s= {'Mist', 'Torrential rain shower', 'Clear', 'Freezing drizzle', 'Overcast', 'Partly cloudy', 'Heavy rain at times', 'Light freezing rain', 'Heavy rain', 'Light rain shower', 'Moderate rain at times', 'Moderate or heavy sleet showers', 'Patchy light drizzle', 'Fog', 'Moderate rain', 'Light sleet', 'Light drizzle', 'Patchy rain possible', 'Moderate or heavy sleet', 'Heavy freezing drizzle', 'Patchy freezing drizzle possible', 'Moderate or heavy rain with thunder', 'Cloudy', 'Light sleet showers', 'Patchy light rain with thunder', 'Sunny', 'Patchy light rain', 'Moderate or heavy rain shower', 'Moderate or heavy freezing rain', 'Thundery outbreaks possible', 'Light rain', 'Freezing fog', 'Patchy sleet possible'}
# {'Mist', 'Torrential rain show

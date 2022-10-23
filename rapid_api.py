import requests
import json

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?aggregateHours=24&combinationMethod=aggregate&contentType=json&unitGroup=us&locationMode=single&key= &dataElements=default&locations=SangaReddy&forecastday=1"


r = requests.get(url)
j = r.json()

x= j['location']
address = x['address']
date= x['values'][0]['datetimeStr']
condition = x['values'][0]['conditions']
# Pretty Print JSON
# json_formatted_str = json.dumps(y, indent=4)
# print(json_formatted_str)

print(date[0:10],condition,address)

# import csv
#
# temp = []
#
# with open("weather_data.csv") as f:
#      data = csv.reader(f)
#      i =0
#      for row in data:
#          if i > 0:
#              a = row[1]
#              print(a)
#          i+=1

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# sunday = data[data.day == "Sunday"]
# print((sunday.temp * 9/5)+ 32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_sq = data[data["Primary Fur Color"] == "Gray"]

black_sq =data[data["Primary Fur Color"] == "Black"]

cinnamon_sq = data[data["Primary Fur Color"] == "Cinnamon"]


data_dict = {
    "fur": ["Gray","NaN","Cinnamon"],
    "Number": [len(gray_sq),len(black_sq),len(cinnamon_sq)]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("sq count.csv")

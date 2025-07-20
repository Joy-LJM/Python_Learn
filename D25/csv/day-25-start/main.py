
# with open("weather_data.csv") as data:
#     weather_data=data.readlines()
#     print(weather_data) #['day,temp,condition\n',...]

# import csv
#
# with open("weather_data.csv") as data:
#     weather_data=csv.reader(data)
#     print(weather_data)
#     temperatures=[]
#     for row in weather_data:
#         if row[1] !='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data=pandas.read_csv("weather_data.csv")
print(data)
temp=data["temp"] # read data by its column name
print(temp)
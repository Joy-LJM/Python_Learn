
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
# print(data)
# print(type(data)) # DataFrame
# print(data.to_dict())
# temp=data["temp"] # read data by its column name;
# print(temp)
# print(type(temp))# Series
# tem_list=temp.to_list()
# print(temp.to_dict())
# # calculate average temperature:mean() mean:平均的
# average=temp.mean()
# print(average)
# # find the max value of temp
# max_temp=temp.max()
# print(max_temp)

#get data in column
# print(data['condition']) # take it as dictionary
# print(data.condition) # object attribute

# get data in row
monday=data[data.day=='Monday']
# print(monday.condition)
monday_temp=monday.temp[0] # [] to get a single value from the pandas Series by index
fahrenheit=monday_temp*1.8+32
print(fahrenheit)
# print(data[data.temp==data.temp.max()])

# create a dataframe from scratch
data_dict={
    "students":["Amy",'Jurin',"Chisa"],
    "scores":[90,88,100]
}
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

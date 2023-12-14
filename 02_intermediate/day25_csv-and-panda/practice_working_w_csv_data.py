# # TASK 1
# with open("csv/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# # TASK 2
# import csv
#
# with open("csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

# # TASK 3
# import csv
#
# with open("csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if str(row[1]).isnumeric():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# # TASK 4
# import pandas
#
# data = pandas.read_csv("csv/weather_data.csv")
# print(data)
# print()
# print(data["temp"])

# # TASK 5
# import pandas
#
# data = pandas.read_csv("csv/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday["temp"][0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# TASK 6 - Create a dataframe from scratch
import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 50, 100]
}

data = pandas.DataFrame(data_dict)
data.to_csv("csv/new_data.csv")

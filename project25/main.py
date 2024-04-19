# data = open("weather_data.csv")
# data = data.readlines()
# for i in range(len(data)):
#     data[i] = data[i].strip("\n")
# print(data)

# import csv

# temperatures = []
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# Get data in column
# temp_list = data["temp"].to_list()
# print(data["temp"].max())


# # # Get data in Row
# # print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_farenheit = monday_temp * 9 / 5 + 32
# print(monday_temp_farenheit)


# # Create dataframe from scratch
# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

short_table = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [
        squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"][
            "Primary Fur Color"
        ].count(),
        squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"][
            "Primary Fur Color"
        ].count(),
        squirrel_data[squirrel_data["Primary Fur Color"] == "Black"][
            "Primary Fur Color"
        ].count(),
    ],
}
short_table = pandas.DataFrame(short_table)
print(short_table)
short_table.to_csv("squirrel_count.csv")

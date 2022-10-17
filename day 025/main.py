# data = []
#
# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

import csv

data = []
temperatures = []
with open("weather_data.csv") as file:
    data = csv.reader(file)
    for row in data:
        temperatures.append(row[1])
        print(row)

print(temperatures)

# def fun():
#     return 10, 20, 30
#
# print(fun())
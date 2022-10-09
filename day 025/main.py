# data = []

# with open('weather_data.csv') as file:
#     data = file.readlines()

# print(data)

import csv 
with open('weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    print(data)

    for row in data:
        temperatures.append(row[1])
        print(row)
    
    print(temperatures)


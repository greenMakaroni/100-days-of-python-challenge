import pandas

weather = pandas.read_csv("weather_data.csv")
print(weather)
print(weather["temp"])


print(type(weather))

# check data type of column
print(type(weather["temp"]))

#convert dataFrame into dictionary
data_dict = weather.to_dict()
print(data_dict)

# list of temperatures
temp_list = weather["temp"].to_list()

print(temp_list)

#calc average
average = sum(temp_list) / len(temp_list)

# calc average
print("Average: ", average)
# find mean
print("Mean: ", weather["temp"].mean())

# find max
print("Max: ", weather["temp"].max())

#another method of accessing columns
print("Data dot: ", weather.temp)

# return row where value in column day = monday
print(weather[weather.day == "Monday"])

# return row where temperature is the highest in a week
print(weather[weather.temp == weather["temp"].max()])

# get a hold of a monday row
monday = weather[weather.day == "Monday"]

# use that row as any other dataFrame
print("Monday condition: ", monday.condition)

# challenge
monday_temp = int(monday.temp)

# convert celsius to fahrenheit
monday_temp_F = monday_temp * 9/5 + 32
print("Monday's temperature in fahrenheit: ", monday_temp_F)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
print(type(data_frame))

# create new csv file using newly created data frame
data_frame.to_csv("new_data.csv")
# Exercise 5 you are going to use dictionary comprehension to create a dictionary called weather_f that
# takes each temperature in degrees celsius and converts it into degrees fahrenheit

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# Don't change code above

# Write your code below


def celsius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f


weather_f = {day:celsius_to_fahrenheit(weather_c[f"{day}"]) for day in weather_c}


print(weather_f)
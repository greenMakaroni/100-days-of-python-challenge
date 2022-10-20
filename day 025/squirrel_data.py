import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
# print(squirrels)

gray_count = 0
cinnamon_count = 0
black_count = 0

for row in squirrels["Primary Fur Color"]:
    if row == "Gray":
        gray_count += 1
    if row == "Cinnamon":
        cinnamon_count += 1
    if row == "Black":
        black_count += 1


squirrel_count = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

data_frame = pandas.DataFrame(squirrel_count)
data_frame.to_csv("squirrel_count.csv")

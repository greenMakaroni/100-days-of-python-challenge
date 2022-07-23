# Coding exercise:
# You are painting a wall.
# The instructions on the paint can says that 1 can of 
# paintcan cover 5 square meters of wall. Given a random height and width of wall
# calculate how many cans of paint youll need to buy
import math

def calculate_paint(width, height):
    square_area = width * height
    cans_needed = square_area / 5
    return math.ceil(cans_needed)

height = int(input("Type height of the wall: "))
width = int(input("Type width of the wall: "))

print(f"For {height * width} square area of wall\nyou'll need {calculate_paint(height=height, width=width)} cans of paint")

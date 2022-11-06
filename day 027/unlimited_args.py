# unlimited (positional) arguments in form of a tuple named args
# arguments in args are accessible by index
def print_all_args(*args):
    for number in args:
        print(number)

print_all_args(1, 2, 3, 4, 8, "lalala", 12)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print("Sum of 2 + 5 + 10 = ", add(2, 5, 10))
# it can take any number of args now
# make sure to type check them
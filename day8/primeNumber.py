# Coding exercise:
# Prime number checker


def checkIfPrime(number):
    isPrime = False
    num_of_factors = 0
    for i in range(2, number + 1):
        print("i: ", i)
        if num_of_factors > 1:
            break
        else:
            if number % i == 0:
                num_of_factors += 1

    if num_of_factors == 1:
        isPrime = True

    if isPrime:
        print(f"{number} is a prime")
    else:
        print(f"{number} is NOT a prime.")
        
    

checkIfPrime(int(input("Type a number: ")))

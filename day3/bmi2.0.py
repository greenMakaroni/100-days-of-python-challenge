
height = input(' enter your height in m: ')
weight = input(' enter your weight in kg: ')

bmi = float(weight) / float(height) ** 2
 
if bmi <= 18.5:
    print("Your BMI indicates that you're underweight")
elif bmi > 18.5 and bmi <= 25:
    print("Congratulations you have a healthy normal weight")
elif bmi > 25 and bmi <= 30:
    print("Your BMI indicates that you're overweight")
elif bmi > 30 and bmi <= 35:
    print("Your BMI indicates that you're obese")
else:
    print("Your BMI indicates that you're clinically obese")

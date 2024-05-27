name = input("Hi, What's your name?")
my_height = float(input("\nEnter your height in m: "))
my_weight = float(input("\nEnter your weight in kg: "))
bmi = round(my_weight / my_height ** 2)
if bmi < 18.5:
    print(name + " is Underweight.\n")
    print(f"Your bmi is {bmi}\n")
    print("Go to the Doctor!\n")
elif bmi < 25:
    print(name + " is Healthy.\n")
    print(f"Your bmi is {bmi}\n")
    print("Good Job!\n\n")
elif bmi < 30:
    print(name + " is Overweight.\n")
    print(f"Your bmi is {bmi}\n")
    print("Be careful.Do Exercises\n")
elif bmi < 35:
    print(name + " have Obesity.\n")
    print(f"Your bmi is {bmi}\n")
    print("Consult a Doctor\n")
else:
    print(name + " is Clinically Obese.\n")
    print(f"Your bmi is {bmi}\n")
    print("It's very important to consult a Doctor\n")

# input age, weight, gender, Cr
# check whether the variables are in range, if illegal so import what is illegal
# use the equation to calculate CrCl

# using if to judge whether the variables are legal
# using elif to continue

# using if to multiple 0.85 if female

age = int(input("What is your age: "))
weight = float(input("What is your weight: "))
gender = input("What is your gender: ")
Cr = float(input("What is your creatine concentration: "))

if(age >= 100 or age <= 0):  # judge whether age is legal
    print("Your age is incorrect!")
elif(weight <= 20 or weight >= 80):  # judge whether weight is legal
    print("Your weight is incorrect!")
elif(Cr <= 0 or Cr >= 100):   # judge whether Cr is legal
    print("Your creatine concentration is incorrect!")
elif(gender != 'male' and gender != 'female'):   # judge whether gender is legal
    print("Your gender is incorrect!")

else:
    CrCl = (140 - age) * weight / (72 * Cr)
    if(gender == 'male'): print("Your CrCl is:", CrCl)  # Male 
    else:  # Female
        CrCl = CrCl * 0.85
        print("Your CrCl is:", CrCl)
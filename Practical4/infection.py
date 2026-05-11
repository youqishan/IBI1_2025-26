# 91 students
# 5 previous infected students
# grouwth rate 40%
# Find how many days all the students be infected

rate = 0.40
day = 0

new_infected = 0
total = 5.0

while total < 91:
    # According to the feedback, I don't need to make a round down...
    new_infected = total * rate

    day = day + 1
    total = total + new_infected

    # print(new_infected)
    print("Day", day, "have total {:.2f} infected students.".format(total))

print("It needs", day, "days to infect all students.")
# We found that it need 9 days to infect all 91 students!

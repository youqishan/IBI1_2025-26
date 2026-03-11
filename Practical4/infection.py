# 91 students
# 5 previous infected students
# grouwth rate 40%
# Find how many days all the students be infected

rate = 0.40
day = 1

new_infected = 0
total = 5.0

while total < 91:
    new_infected = total * rate // 1
    # new_infected round down: for example, 2.8 infecters become 2!

    print("Day", day, "have", total, "infected students.")

    day = day + 1
    # print(new_infected)
    total = total + new_infected

print("Day", day, "have 91.0 infected students.")
print("It needs", day, "days to infect all students.")
# We found that it need 11 days to infect all 91 students!
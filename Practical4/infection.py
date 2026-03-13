# 91 students
# 5 previous infected students
# grouwth rate 40%
# Find how many days all the students be infected

rate = 0.40
day = 0

new_infected = 0
total = 5.0

while total < 91:
    # new_infected round down: for example, 2.8 infecters become 2!
    new_infected = int(total * rate) 

    day = day + 1
    total = total + new_infected

    # print(new_infected)
    print("Day", day, "have total", total, "infected students.")

print("Day", day, "have total 91.0 infected students.")
print("It needs", day, "days to infect all students.")
# We found that it need 10 days to infect all 91 students!
# What does this piece of code do?
# Answer: The total_rand is a total of 11 random integers between 1 and 10, it should have a expactation at 60.5, also bigger than 11, less than 110

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1   # It is a counter, we need to run this circulation for 11 times!
	n = randint(1,10)
	total_rand+=n # Each time we add a random integer between 1 and 10 to total_rand!

print(total_rand)

a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
    
if(d > e):
    print("d is bigger than e, the growth is decelerating.")
elif(e > d):
    print("e is bigger than d, the growth is accelerating.")

# We found that d is bigger than e, and the growth is decelerating.

X = True	
Y = False	
W = X or Y	
print(W)  # W=True	

# the truth table for W:
# X = T, Y = T, so W = T
# X = T, Y = F, so W = T
# X = F, Y = T, so W = T
# X = F, Y = F, so W = F
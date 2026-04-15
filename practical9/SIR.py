import numpy as np
import matplotlib.pyplot as plt

# 1st, define the original value 
N = 10000   # total population
I = 1       # initial infected individuals
S = N - I   # initial susceptible individuals
R = 0       # initial recovered individuals

beta = 0.3
gamma = 0.05
total_days = 1000

# 2nd, create lists to store the values of S, I, R over time
S_list = [S]
I_list = [I]
R_list = [R]

# 3rd, run the 1000 days of the SIR model
for day in range(total_days):
    # first calculate the probability of be infected and recovery
    p_infection = beta * I / N
    p_recovery = gamma

    # then calculate the number of new infections and recoveries
    new_infections = np.sum(np.random.choice([0, 1], size=S, p=[1 - p_infection, p_infection]))
    new_recoveries = np.sum(np.random.choice([0, 1], size=I, p=[1 - p_recovery, p_recovery]))

    # update the values of S, I, R
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    # store the updated values
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# 4th, plot the results
plt.figure(figsize=(8, 5), dpi=150)  
plt.plot(S_list, label='Susceptible', color='#1f77b4')
plt.plot(I_list, label='Infected', color='#ff7f0e')
plt.plot(R_list, label='Recovered', color='#2ca02c')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.grid(alpha=0.3)

plt.savefig('SIR_result.png')
plt.show()
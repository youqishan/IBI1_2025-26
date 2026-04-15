import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1st, define the original value 
N = 10000   # total population
I_init = 1       # initial infected individuals

beta = 0.3
gamma = 0.05
total_days = 1000

# 2nd, add vaccination rate to the model, and store the results in a list
vaccination_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] 
infected_curves = []  

for rate in vaccination_rate:
    # define the original value for each loop
    S = N - I_init   # initial susceptible individuals
    R = 0       # initial recovered individuals

    # first, reset the initial values for each vaccination rate
    initial_R = int((N - I_init) * rate)  # vaccinated individuals are considered as recovered
    S = N - I_init - initial_R
    S = max(S, 0)  # ensure S is not negative
    R = initial_R
    I = I_init
    daily_infected = [I]  

    # then, run the 1000 days of the SIR model
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

        # store the daily infected individuals
        daily_infected.append(I)

    # store the infected curve for this vaccination rate
    infected_curves.append(daily_infected)

# 4th, plot the results
plt.figure(figsize=(12, 8), dpi=100)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rate)))

for i, curve in enumerate(infected_curves):
    plt.plot(curve, color=colors[i], label=f"{int(vaccination_rate[i] * 100)}%")

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.grid(alpha=0.3)

plt.savefig('SIR_vaccination_result.png', dpi=100)
plt.show()
'''
1st, define a grid
2nd, define the parameters for the SIR model
3rd, run the SIR model for 1000 days
    3.1 calculate the probability of infection and recovery
    3.2 calculate the number of new infections and recoveries
    3.3 save the state of the population after each day
4th, plot the results
'''

import numpy as np
import matplotlib.pyplot as plt

# 1st, provide a 100*100 grid to represent the population, and randomly select one individual to be infected
grid_size = 100
population = np.zeros((grid_size, grid_size), dtype=int)  # 0: susceptible, 1: infected, 2: recovered

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # set the initial infected individual to 1

'''
# test the graph
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial State of the Population')
plt.show()
'''

# 2nd, define the parameters for the SIR model and store it
beta = 0.3  # infection rate
gamma = 0.05  # recovery rate
total_days = 100
history = []
history.append(population.copy())  # store the initial state

# 3rd, run the SIR model for 100 days
for day in range(total_days):
    # find infected points
    infectedIndex = np.where(population == 1)

    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour, yNeighbour) != (x, y):
                    # make sure I don't fall off an edge
                    if (
                        xNeighbour != -1
                        and yNeighbour != -1
                        and xNeighbour != grid_size
                        and yNeighbour != grid_size
                    ):
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour, yNeighbour] == 0:
                            population[xNeighbour, yNeighbour] = np.random.choice(
                                range(2), 1, p=[1 - beta, beta]
                            )[0]

    # recover with probability gamma
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.rand() < gamma:
            population[x, y] = 2  # set to recovered

    history.append(population.copy())  # store the state of the population after each day

# 4th, plot the results
plt.figure(figsize=(10, 6), dpi=160)

# select day0, day10, day50, and day100 to plot
days_to_plot = [0, 10, 50, 100]
for i, day in enumerate(days_to_plot):
    plt.subplot(2, 2, i + 1)
    plt.imshow(history[day], cmap='viridis',vmin=0, vmax=2, interpolation='nearest')
    plt.title(f'Day {day}')
    # plt.xlabel([])
    # plt.ylabel([])
plt.tight_layout()

plt.savefig('spatial_SIR_result.png', dpi=160)
plt.show()
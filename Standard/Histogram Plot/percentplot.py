import random
import matplotlib.pyplot as plt

match_list = []
percent_data = []


# Random Method
# Input : Current Alpha Pack Percent Chance
# Output : True(Drop Alpha Pack) or False(Not Drop Alpha Pack)
def chance(percent):
    random_number = random.random()
    return random_number < (percent / 100)


# Simulation Method
def alphapack():
    match_list = [random.randint(0, 1) for i in range(40)]
    percent = 0
    matchs = 0
    for match in match_list:
        if match == 1:
            percent = percent + 2
            matchs = matchs + 1
            if chance(percent):
                percent_data.append(percent)
                return
        elif match == 0:
            percent = percent + 1.5
            matchs = matchs + 1


# Simulation
def simulation(generate_times):
    for i in range(generate_times):
        alphapack()
        
simulation(1000000)
# You can also change the number of simulations to 1,000,000 to get a more accurate histogram.


# Plot Histogram
plt.hist(percent_data, bins=range(1, 100), edgecolor='black', density=False) 
plt.xticks(range(1, 100)) 
plt.xlabel('Percent Chance')
plt.ylabel('Frequency')
plt.title('Distribution of Percent Chance Increments to Obtain Alpha Pack (Standard)')
plt.grid(True)
plt.show()
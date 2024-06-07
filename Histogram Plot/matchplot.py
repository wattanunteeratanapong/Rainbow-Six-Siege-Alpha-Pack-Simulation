import random
import matplotlib.pyplot as plt

match_list = []
match_data = []


# Random Method
# Input : Current Alpha Pack Chance
# Output : True(Drop Alpha Pack) or False(Not Drop Alpha Pack)
def chance(percent):
    random_number = random.random()
    return random_number < (percent / 100)


# Simulation Method
def alphapack():
    match_list = [random.randint(0, 1) for _ in range(40)]
    percent = 0
    matchs = 0
    for match in match_list:
        if match == 1:
            percent = percent + 2.5
            matchs = matchs + 1
            if chance(percent):
                match_data.append(matchs)
                return
        elif match == 0:
            percent = percent + 2.5
            matchs = matchs + 1


# Simulation
def simulation(generate_times):
    for i in range(generate_times):
        alphapack()
        
simulation(100000)


# Plot Histogram
plt.hist(match_data, bins=range(1, 40), edgecolor='black', density=False) 
plt.xticks(range(1, 40)) 
plt.xlabel('Number of Matches')
plt.ylabel('Frequency')
plt.title('Distribution of Matches to Obtain Alpha Pack')
plt.grid(True)
plt.show()
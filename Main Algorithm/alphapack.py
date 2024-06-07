import random

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
                print("\n You have got alpha pack in " + str(matchs) + " matches\n")
                percent = 0
                match_data.append(matchs)
                return 
        elif match == 0:
            percent = percent + 2.5
            matchs = matchs + 1


# Time Complexity : O(n)
# Space Complexity : O(n)


alphapack()

"""
Problem Statement:
    Selection of MPCS exams include a fitness test which is conducted on ground.
    There will be a batch of 3 trainees, appearing for running test in track for 3 rounds.
    You need to record their oxygen level after every round.
    After trainee are finished with all rounds, calculate for each trainee his average oxygen level over the 3 rounds.
    And select one with highest oxygen level as the most fit trainee.
    If more than one trainee attains the same highest average level, they all need to be selected.
    Display the most fit trainee (or trainees) and the highest average oxygen level.

Note:
    The oxygen value entered should not be accepted if it is not in the range between 1 and 100.
    If the calculated maximum average oxygen value of trainees is below 70.
    Then declare the trainees as unfit with meaningful message as “All trainees are unfit.
    Average Oxygen Values should be rounded.
"""

"""
trainee = [[], [], [], []]
for i in range(3):
    for j in range(3):
        trainee[i].append(int(input()))
        if (trainee[i][-1]) not in range(1, 101):
            print("Invalid Input")

for i in range(3):
    trainee[3].append((trainee[2][i]+trainee[1][i]+trainee[0][i])//3)
maximum = max(trainee[3])

for i in range(3):
    if trainee[3][i] < 70:
        print("Trainee {0} is unfit".format(i+1))
    elif trainee[3][i] == maximum:
        print("Trainee {0} is fit".format(i+1))
"""


average = []
for test in [1, 2, 3]:
    trainee = []
    for level in [1, 2, 3]:
        oxygen = int(input())
        if oxygen in range(1, 101):
            trainee.append(oxygen)
        else:
            print('Invalid Input : oxygen_level >=1 and oxygen_level <= 100')
            exit()
    average.append(sum(trainee) // len(trainee))

del trainee
for i, avg in enumerate(average):
    if avg > 70:
        print('Trainee {0} Fit', i+1)
    else:
        print('Trainee {0} Unfit', i+1)

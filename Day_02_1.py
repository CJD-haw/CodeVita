
"""
Problem Statement:
    At a fun fair, a street vendor is selling different colours of balloons.
    He sells N number of different colours of balloons (B[]).
    The task is to find the colour (odd) of the balloon which is present odd number of times in the bunch of balloons.
Note:
    If there is more than one colour which is odd in number.
    Then the first colour in the array which is present odd number of times is displayed.
    The colours of the balloons can all be either upper case or lower case in the array.
    If all the inputs are even in number, display the message “All are even”.
Constraints:
    3<=N<=50
    A[i]={{a-z} or {A-Z}}
"""

n = int(input())
if n >= 3 or n <= 50:

    balloons = []
    for i in range(n):
        balloons.append(input())
        if balloons[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('INVALID INPUT')
            exit()

    balloon = [[b, 0, 0] for b in set(balloons)]
    for ball in balloons:
        for bal in balloon:
            if ball == bal[0]:
                bal[1] += 1
            if bal[1] % 2 == 0:
                bal[2] = 0
            else:
                bal[2] = 1

    for bal in balloon:
        if bal[2] == 1:
            print(bal[0])

else:
    print('INVALID INPUT')



"""
Problem Statement:
    A washing machine works on the principle of Fuzzy System,
     the weight of clothes put inside it for washing is uncertain But based on weight measured by sensors,
      it decides time and water level which can be changed by menus given on the machine control area.

For low level water, the time estimate is 25 minutes,
Where approximately weight is between 2000 grams or any nonzero positive number below that.

For medium level water, the time estimate is 35 minutes,
Where approximately weight is between 2001 grams and 4000 grams.

For high level water, the time estimate is 45 minutes,
Where approximately weight is above 4000 grams.

Assume the capacity of machine is maximum 7000 grams
Where approximately weight is zero, time estimate is 0 minutes.

Write a function which takes a numeric weight in the range [0,7000] as input,
And produces estimated time as output is: “OVERLOADED”, and for all other inputs,
The output statement is “INVALID INPUT”.

Input should be in the form of integer value
Output must have the following format of Time Estimated: Minutes

Example:
    Input value
    2000
    Output value
    Time Estimated: 25 minutes
"""

"""
n = int(input())
if n==0:
    print("Time Estimated : 0 Minutes")
elif n in range(1,2001):
    print("Time Estimated : 25 Minutes")
elif n in range(2001,4001):
    print("Time Estimated : 35 Minutes")
elif n in range(4001,7001):
    print("Time Estimated : 45 Minutes")
else:
    print("INVALID INPUT")
"""

weight = int(input('Weight of clothes are '))
time = [0, 25, 35, 45]
if weight in range(0, 7001):
    if weight in range(0, 1):
        print('{0} minutes for washing {1} weight of clothes'.format(time[0], weight))
    elif weight in range(1, 2001):
        print('{0} minutes for washing {1} weight of clothes'.format(time[1], weight))
    elif weight in range(2001, 4001):
        print('{0} minutes for washing {1} weight of clothes'.format(time[2], weight))
    elif weight in range(4, 7001):
        print('{0} minutes for washing {1} weight of clothes'.format(time[3], weight))
else:
    print('Invalid Input : Weight Overload')

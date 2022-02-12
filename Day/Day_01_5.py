
"""
Problem Statement
    A party has been organised on cruise.
    The party is organised for a limited time(T).
    The number of guests entering (E[i]) and leaving (L[i]) the party at every hour is represented as elements of the array.
    The task is to find the maximum number of guests present on the cruise at any given instance within T hours.
"""

"""
Time in hours T
Visit of guests are V list
Exit of guest are E list
Find Max instance of guest at party
# Constraint
T from 1 to 25
Visit | Exit of guest from 0 to 500
"""

T = int(input())
if T >= 1 or T <= 25:
    VS = input()
    ES = input()
    V = [int(vs) for vs in VS.split(',')]
    E = [int(es) for es in ES.split(',')]
    result = []
    status = 0
    for v, e in zip(V, E):
        if v <= 500 and e <= 500:
            status += v
            status -= e
            result.append(status)
        else:
            print('Invalid Input')

    print(max(result))

else:
    print('Invalid Input')


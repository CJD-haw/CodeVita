
"""
Problem Statement
    An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW).
    A company manager wants to make the production of both types of vehicle according to the given data below:
        1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
        2nd data, Total number of wheels = W
    The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data
"""

v = int(input('TNV='))
w = int(input('TNW='))

"""
x + y = v       --> 1 (total number of two wheeler and four wheeler)
2x + 4y = w     --> 2 (total number of wheels)
from 2 - 1*2
2y = w - 2v
y = (w - 2v) // 2
x = v - y
"""

if w % 2 == 0 and w >= 2 and w > v:
    y = (w - 2*v) // 2
    x = v - y
    print("TW={0} FW={1}".format(x, y))
else:
    print("INVALID INPUT")

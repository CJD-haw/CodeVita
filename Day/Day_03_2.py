
"""
Problem Statement:
    A City Bus is a Ring Route Bus which runs in circular fashion.
    That is, Bus once starts at the Source Bus Stop,
     halts at each Bus Stop in its Route and at the end it reaches the Source Bus Stop again.
    If there are n  number of Stops and if the bus starts at Bus Stop 1,
     then after nth Bus Stop, the next stop in the Route will be Bus Stop number 1 always.
    If there are n stops, there will be n paths.One path connects two stops.
    Distances (in meters) for all paths in Ring Route is given in array Path[] as given below:
    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

Fare is determined based on the distance covered from source to destination stop
 as  Distance between Input Source and Destination Stops can be measured by looking at values in array Path[]
  and fare can be calculated as per following criteria:

    If d =1000 metres, then fare=5 INR
    (When calculating fare for others, the calculated fare containing any fraction value should be ceiled.
    For example, for distance 900n when fare initially calculated is 4.5 which must be ceiled to 5)

Path is circular in function.

Value at each index indicates distance till current stop from the previous one.

And each index position can be mapped with values at same index in BusStops [] array,
 which is a string array holding abbreviation of names for all stops as-
“THANERAILWAYSTN” = ”TH”, “GAONDEVI” = “GA”, “ICEFACTROY” = “IC”, “HARINIWASCIRCLE” = “HA”,
 “TEENHATHNAKA” = “TE”, “LUISWADI” = “LU”, “NITINCOMPANYJUNCTION” = “NI”, “CADBURRYJUNCTION” = “CA”

Given, n=8, where n is number of total BusStops.
BusStops = [ “TH”, ”GA”, ”IC”, ”HA”, ”TE”, ”LU”, ”NI”,”CA” ]

Write a code with function getFare(String Source, String Destination)
Input as source and destination stops(in the format containing first two characters of the Name of the Bus Stop)
And calculate and return travel fare.

Example 1:
Input Values
ca
Ca

Output Values
INVALID OUTPUT

Example 2:
Input Values
NI
HA
Output Values
23.0 INR

Note: Input and Output should be in format given in example.
Input should not be case sensitive and output should be in the format   INR
"""

"""
import math


def getFare():
    route = [["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"],
             [800, 600, 750, 900, 1400, 1200, 1100, 1500]
             ]
    fare = 0.0
    if not (source in route[0] and destination in route[0]):
        print("Invalid Input")
        exit()
    if route[0].index(source) < route[0].index(destination):
        for i in range(route[0].index(source), route[0].index(destination) + 1):
            fare += route[1][i]
    elif route[0].index(destination) < route[0].index(source):
        for i in range(route[0].index(source) + 1, len(route[0])):
            fare += route[1][i]
        for i in range(0, route[0].index(destination) + 1):
            fare += route[1][i]
    return float(math.ceil(fare * 0.005))


source = input()
destination = input()
cost = getFare()
if cost == 0:
    print("Invalid Input")
else:
    print(cost)

"""

path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
stops = ['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA']
cost = 5    # 1000 m = 1 km = 5 INR

source = input()
destination = input()
# print(source, destination)

if source in stops and destination in stops:
    si = stops.index(source)
    di = stops.index(destination)
    # print(si, di)

    distance = 0
    if si < di:
        distance += sum([path[i] for i in range(si, di+1)])
    elif si > di:
        distance += sum([path[i] for i in range(0, di+1)])
        distance += sum([path[i] for i in range(si+1, len(path))])

    # print(int(distance * 5 / 1000))
    import math
    print('{} INR'.format(math.ceil(distance * 0.005)))

else:
    print('Invalid Input')

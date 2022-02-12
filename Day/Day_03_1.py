
"""
Problem Statement:
    We want to estimate the cost of painting a property.
    Interior wall painting cost is Rs.18 per sq.ft.
    Exterior wall painting cost is Rs.12 per sq.ft.

Take input as
    1. Number of Interior walls.
    2. Number of Exterior walls.
    3. Surface Area of each Interior Wall in units of square feet.
    4. Surface Area of each Exterior Wall in units of square feet.

If a user enters zero  as the number of walls.
Then skip Surface area values as User may don’t  want to paint that wall.

Calculate and display the total cost of painting the property
Example 1:

6
3
12.3
15.2
12.3
15.2
12.3
15.2
10.10
10.10
10.00
Total estimated Cost : 1847.4 INR

Note: Follow in input and output format as given in above example
"""

"""
interior_walls = int(input())
exterior_walls = int(input())
if interior_walls:
    int_walls = []
    for i in range(interior_walls):
        int_walls.append(float(input()))

if exterior_walls:
    ext_walls = []
    for i in range(exterior_walls):
        ext_walls.append(float(input()))
if exterior_walls < 0 or interior_walls < 0:
    print(“Invalid Input”)
    exit()
if exterior_walls and interior_walls:
    print("Total estimated Cost : ",(sum(int_walls)*18+sum(ext_walls)*12),"INR")
else:
    if exterior_walls:
        print("Total estimated Cost : ",sum(ext_walls)*12,"INR")
    elif interior_walls:
         print("Total estimated Cost : ",sum(int_walls)*18,"INR")
    else:
        print("Total estimated Cost : 0.0 INR")
"""

interior = int(input('No. of Interior Walls : '))
exterior = int(input('No. of Exterior Walls : '))

if interior < 0 or exterior < 0:
    print('Invalid Input : No. of walls must be in +ive number')
    exit()
elif interior == 0:
    print('Does not want to paint Interior Wall')
    exit()
elif exterior == 0:
    print('Does not want to paint Exterior Wall')
    exit()
else:
    inside, outside = 'Interior', 'Exterior'
    ip_interior, ip_exterior = 'Surface of Interior Wall {0} : ', 'Surface of Exterior Wall {0} : '
    interior_square_feet = [[inside, float(input(ip_interior.format(i+1)))] for i in range(interior)]
    exterior_square_feet = [[outside, float(input(ip_exterior.format(e+1)))] for e in range(exterior)]
    total_square_feet = interior_square_feet + exterior_square_feet
    interior_cost, exterior_cost, total_cost = 18, 12, 0

    for sf in total_square_feet:
        side = sf[0]
        if side == inside:
            total_cost += sf[-1] * interior_cost
        elif side == outside:
            total_cost += sf[-1] * exterior_cost

    print('Total estimated cost is {0} INR'.format(total_cost))

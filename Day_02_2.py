
"""
Problem Statement:
    There is a JAR full of candies for sale at a mall counter.
    JAR has the capacity N, that is JAR can contain maximum N candies when JAR is full. At any point of time.
    JAR can have M number of Candies where M<=N. Candies are served to the customers.
    JAR is never remain empty as when last k candies are left.
    JAR if refilled with new candies in such a way that JAR get full.

Write a code to implement above scenario. Display JAR at counter with available number of candies.

Input should be the number of candies one customer can order at point of time.

Update the JAR after each purchase and display JAR at Counter.

Output should give number of Candies sold and updated number of Candies in JAR.

If Input is more than candies in JAR, return: “INVALID INPUT”

Given:
    N=10, where N is NUMBER OF CANDIES AVAILABLE
    K =< 5, where k is number of minimum candies that must be inside JAR ever.
"""

total = int(input('No. of Candies Available : '))
if total > 1:
    jar = int(input('No. of Candies in JAR : '))
    if jar in range(1, total+1):
        sold = int(input('No. of Candies Customer Sold : '))
        if sold in range(1, jar+1):
            print('No. of Candies Sold : ', sold)
            print('No. of Candies Left : ', total - sold)
        else:
            print("Invalid Input : sold <= jar")
            print('No. of Candies Left : ', total)
    else:
        print("Invalid Input : jar >= 1 and jar <= total")
else:
    print("Invalid Input : total > 1")

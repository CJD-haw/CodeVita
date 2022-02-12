
"""
Problem Statement:
    Addition of two numbers a Twist by using a method, pass two variables and find the sum of two numbers.

Test case:
Number 1 – 20
Number 2 – 20.38
Sum = 40.38

There were a total of 4 test cases.
Once you compile 3 of them will be shown to you and 1 will be a hidden one.
You have to display error message if numbers are not numeric.
"""


def add(a, b):
    return a + b


number1 = input('Number 1 - ')
number2 = input('Number 2 - ')
try:
    total = add(int(number1), float(number2))
    print('Sum = {}'.format(total))
except:
    print('Invalid Input')

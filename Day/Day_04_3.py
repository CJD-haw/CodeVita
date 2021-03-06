
"""
Problem Statement:
    Prime Numbers with a Twist

Write a code to check whether no is prime or not.
Condition use function check() to find whether entered no is positive or negative,
if negative then enter the no,
And if yes pas no as a parameter to prime() and check whether no is prime or not?

Whether the number is positive or not, if it is negative then print the message “please enter the positive number”
It is positive then call the function prime and check whether the take positive number is prime or not.
"""

"""
def prime(n):
   if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")

num = int(input("enter a number: "))
if (num > 0):
    prime(num)
else:
    print("please enter a positive number")
"""


def check(n):
    divisor = [d for d in range(2, n)]
    # print(divisor)
    result = [1 for d in divisor if n % d == 0]
    # print(result)
    return result


number = int(input('Enter Number : '))
if number > 0:
    if check(number):
        print('{} is not a prime number'.format(number))
    else:
        print('{} is a prime number'.format(number))
else:
    print('Kindly enter positive number')

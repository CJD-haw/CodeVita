
"""
Problem Statement:
    To be a leap year, the year number must be divisible by four.
    Except for end-of-century years, which must be divisible by 400.
    This means that the year 2000 was a leap year, although 1900 was not.
    2020, 2024 and 2028 are all leap years.

Checking if a given year is leap year or not

Explanation:
    To check whether a year is leap or not
        Step 1:
            We first divide the year by 4.
            If it is not divisible by 4 then it is not a leap year.
            If it is divisible by 4 leaving remainder 0
        Step 2:
            We divide the year by 100
            If it is not divisible by 100 then it is a leap year.
            If it is divisible by 100 leaving remainder 0
        Step 3:
            We divide the year by 400.
            If it is not divisible by 400 then it is a leap year.
            If it is divisible by 400 leaving remainder 0
            Then it is a leap year
"""

"""
#python program to check if a year number taken from the user is a leap year or not, using nested if-else.

num = int(input("Enter the year you want to check if is leap year or not: "))

#take input year from the user to check if it is a leap year

if(num%4 == 0):

 #check if the number is divisible by 4 and if true move to next loop

   if(num%100 == 0):

     #check if the input year is divisible by 100 and if true move to next loop

       if(num%400 == 0):

           print("The year {} is a leap year".format(num))

           #the input year is divisible by 4, 100 and 400, hence leap year.

       else:

           print("The year {} is Not a leap year".format(num))

   else:

       print("The year {} is a leap year".format(num))

       #if the number is divisible by both 4 and 100 it is a leap year

else:

   print("The year {} is Not a leap year".format(num))

   #if the input num is not divisible by 4 then it can not be a leap year altogether.
"""

year = int(input('Enter Year : '))
if year % 4 == 0:
    if year % 100 != 0:
        print('{} is a leap year'.format(year))
    elif year % 100 == 0 and year % 400 == 0:
        print('{} is a leap year'.format(year))
    else:
        print('{} is not a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))

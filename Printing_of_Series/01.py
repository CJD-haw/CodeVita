# 1. Write a program Program to print Arithmetic series 1 4 7 10 ...
"""
print("Enter the First Number : ")
first_num = int(input())
print("Enter the range of number(Limit) : ")
n = int(input())
print("Enter the Difference Between two Number : ")
diff = int(input())
while first_num <= n:
     print(first_num, end=" ")
     first_num += diff
"""

n = int(input())
for val in range(1, n+1, 3):
    print(val, end=' ')

# 15. Write a Program to print series: 1 22 333 4444 ... N
"""
n=int(input("Enter the range of number(Limit) : "))
for out in range(n+1):
    for i in range(out):
        print(out, end="")
    print(end=" ")
"""

n = 4
for val in range(1, n+1):
    print(str(val) * val, end=' ')

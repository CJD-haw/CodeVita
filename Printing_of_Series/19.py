# 19. Write a Program to print series: 2 4 7 12 21 38 71 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 0
pr = 2
print("2 ", end=" ")
while i < n-1:
    pr = (pr * 2) - i
    print(pr, end = " ")
    i += 1
"""

n = int(input())
val = 2
for res in range(n):
    print(val, end=' ')
    val = (val * 2) - res

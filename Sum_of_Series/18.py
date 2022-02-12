# 18. Write a program to find the sum of series: 1 + 4 - 9 + 16 - 25 + ... + N
"""
import math
print("Enter the range of number(Limit) : ")
n = int(input())
i = 2
sum = 1
while i <= n:
    if i % 2 == 0:
        sum += pow(i, 2)
    else:
        sum -= pow(i, 2)
    i += 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
odd = [-(val ** 2) for val in range(3, n+1, 2)]
even = [(val ** 2) for val in range(2, n+1, 2)]
result = [1] + odd + even
print(sum(result))
"""

print(sum([-(val ** 2) if val != 1 and val % 2 != 0 else (val ** 2) for val in range(1, int(input()) + 1)]))

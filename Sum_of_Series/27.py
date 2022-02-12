# 27. Write a Program to Find the sum of series: 9 + 99 + 999 + 9999 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
p = 9
for i in range(1, n+1):
    sum += p
    p = (p * 10) + 9
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [int('9'*val) for val in range(1, n+1)]
print(sum(result))
"""

print(sum([int('9' * val) for val in range(1, int(input()) + 1)]))

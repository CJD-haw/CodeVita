# 29. Write a Program to Find the sum of series: 3 + 33 + 333 + 3333 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
p = 3
for i in range(1, n+1):
    sum += p
    p = (p * 10) + 3
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [int('3'*val) for val in range(1, n+1)]
print(sum(result))
"""

print(sum([int('3' * val) for val in range(1, int(input()) + 1)]))

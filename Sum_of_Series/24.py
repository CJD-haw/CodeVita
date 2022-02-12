# 24. Write a Program to Find the sum of series: 1 + 11 + 111 + 1111 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
p = 1
for i in range(1, n+1):
    sum += p
    p = (p * 10) + 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [int('1'*val) for val in range(1, n+1)]
print(sum(result))
"""

print(sum([int('1' * val) for val in range(1, int(input()) + 1)]))

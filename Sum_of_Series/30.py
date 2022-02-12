# 30. Write a Program to Find the sum of series: 3 + 7 + 13 + 21 + 31 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
for i in range(2, n+2):
    sum += 1 + (i * (i-1))
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [1 + val * (val + 1) for val in range(1, n+1)]
print(sum(result))
"""

print(sum([1 + val * (val + 1) for val in range(1, int(input()) + 1)]))

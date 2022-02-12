# 26. Write a Program to Find the sum of series: 2 + 4 + 6 + 8 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
i = 0
while i <= n:
    sum += i
    i += 2
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [val for val in range(2, n+1, 2)]
print(sum(result))
"""

print(sum([val for val in range(2, int(input()) + 1, 2)]))

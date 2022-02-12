# 31. Write a Program to Find the sum of series: 1³ + 2³ + 3³ + 4³ + ... + N³
"""
n = int(input("Enter the range of number : "))
sum = 0
for i in range(1, n+1):
    sum += pow(i, 3)
print("The sum of the series =", sum)
"""

"""
n = 5
result = [val ** 3 for val in range(1, n+1)]
print(sum(result))
"""

print(sum([val ** 3 for val in range(1, int(input()) + 1)]))

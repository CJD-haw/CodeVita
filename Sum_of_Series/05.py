# 5. Write a Program to find the sum of series: 1/1 + 1/2 + 1/3 + ... + 1/N
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += 1 / i
print("The sum of the series = ", sum)
"""

"""
n = int(input())
result = [1 / val for val in range(1, n+1)]
print(sum(result))
"""

print(sum([1 / val for val in range(1, int(input()) + 1)]))

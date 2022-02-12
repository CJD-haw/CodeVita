# 2. Write a program to find the sum of series: 1 + 3 + 5 + 7 + ... + N
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
i = 1
while i <= n:
    sum += i
    i += 2
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [val for val in range(1, n+1, 2)]
print(sum(result))
"""

print(sum([val for val in range(1, int(input()) + 1, 2)]))

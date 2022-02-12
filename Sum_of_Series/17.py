# 17. Write a program to find the sum of series: 1 + (1+3) + (1+3+5) + ... + N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
sum = 0
while (i <= n):
    for j in range(1, i + 1,2):
        sum += j
    i += 2
print("The sum of the series =",sum)
"""

"""
n = int(input())
result = [v for val in range(1, n+1, 2) for v in range(1, val+1, 2)]
print(sum(result))
"""

print(sum([v for val in range(1, int(input()) + 1, 2) for v in range(1, val+1, 2)]))

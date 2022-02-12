# 19. Write a program to find the sum of series: 1/1 + 1/3 + 1/5 + 1/7 + ... + 1/(N+2)
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
sum = 0.0
while i <= n:
    sum += 1 / i
    i += 2
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [1 / val for val in range(1, n+1, 2)]
print(sum(result))
"""

print(sum([1 / val for val in range(1, int(input()) + 1, 2)]))

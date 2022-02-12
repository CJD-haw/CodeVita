# 9. Write a program to find the sum of series: (1 + (1+2) + (1+2+3) + ... + till N)
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
i = 1
while i <= n:
    for j in range(1, i+1):
        sum += j
    i += 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
result = [v for val in range(1, n+1) for v in range(1, val+1)]
print(sum(result))
"""

print(sum([v for val in range(1, int(input()) + 1) for v in range(1, val+1)]))

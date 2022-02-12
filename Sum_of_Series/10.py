# 10. Write a program to find the sum of series: (1 + (1*2) + (1*2*3) + ... + till N)
"""
print("Enter the range of number : ")
n = int(input())
sum_series = 0
i = 1
while i <= n:
    multiply = 1
    for j in range(1, i+1):
        multiply *= j
    sum_series += multiply
    i += 1
print("The sum of the series =", sum_series)
"""

n = int(input())
result = 0
for val in range(1, n+1):
    temp = 1
    for v in range(1, val+1):
        temp *= v
    result += temp
print(result)

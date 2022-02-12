# 11. Write a Program to find the sum of series: 1! + 2! + 3! + ... + N!
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += fact
print("The sum of the series =", sum)
"""


def fact(num):
    f = 1
    for v in range(1, num+1):
        f *= v
    return f


n = int(input())
result = [fact(val) for val in range(1, n+1)]
print(sum(result))

# print(sum([fact(val) for val in range(1, n+1)]))

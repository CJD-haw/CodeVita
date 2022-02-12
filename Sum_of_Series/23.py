# 23. Write a Program to Find the sum of series: 1 - 2 + 3 - 4 + 5 - 6 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print("The sum of the series =", sum)
"""

"""
n = int(input())
odd = [val for val in range(1, n+1, 2)]
even = [-val for val in range(2, n+1, 2)]
result = odd + even
print(sum(result))
# print(sum([val for val in range(1, n+1, 2)] + [-val for val in range(2, n+1, 2)]))
"""

print(sum([val if val % 2 != 0 else -val for val in range(1, int(input()) + 1)]))

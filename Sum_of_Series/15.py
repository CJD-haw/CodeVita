# 15. Write a program to find the sum of series: 1/2 - 2/3 + 3/4 - 4/5 + 5/6 + ... + N/N+1
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
sum = 0.0
while i <= n:
    if i%2 == 0:
        sum -= i / (i+1)
    else:
        sum += i / (i+1)
    i += 1
print("The sum of the series =", sum)
"""

"""
n = int(input())
odd = [val / (val+1) for val in range(1, n+1) if val % 2 != 0]
even = [-val / (val+1) for val in range(1, n+1) if val % 2 == 0]
result = odd + even
print(sum(result))
"""

print(sum([val / (val+1) if val % 2 != 0 else -val / (val+1) for val in range(1, int(input()) + 1)]))

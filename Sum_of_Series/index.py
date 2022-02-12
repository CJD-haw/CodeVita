# 1. Write a program to find the sum of series: 1 + 2 + 3 + ... + N
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of the series = ",sum)
"""
# 2. Write a program to find the sum of series: 1 + 3 + 5 + 7 + ... + N
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
i = 1
while i <= n:
    sum += i
    i += 2
print("The sum of the series = ",sum)
"""
# 3. Write a Program to find the sum of series: 1^2 + 2^2 + 3^2 + ... + N^2
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i ** 2
print("The sum of the series = ",sum)
"""
# 4. Write a Program to find the sum of series: 1^1 + 2^2 + 3^3 + ... + N^N
"""
import math
print("Enter the range of number : ")
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += pow(i, i)
print("The sum of the series = ",sum)
"""
# 5. Write a Program to find the sum of series: 1/1 + 1/2 + 1/3 + ... + 1/N
"""
print("Enter the range of number : ")
n = int(input())
sum = 0
i = 1
while i <= n:
    sum += 1 / i
    i += 2
print("The sum of the series = ",sum)
"""
# 6. Write a Program to find the sum of series: X^1 + X^2 + X^3 + ... + X^N
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ");
x = int(input())
sum = 0
i = 1
while i <= n:
    sum += pow(x, i)
    i += 2
print("The sum of the series = ",sum)
"""
# 7. Write a Program to find the sum of series: 1+ X + X^2/2 + ...+ X^N/N
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ")
x = int(input())
sum = 1.0
i = 1
while i <= n:
    sum += pow(x, i) / i
    i += 1
print("The sum of the series = ",sum)
"""
# 8. Write a Program to find the sum of series: 1 + X + X^2/2! + X^3/3! + ... + X^N/N!
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ")
x = int(input())
sum = 1.0
i = 1
while i <= n:
    fact = 1
    for j in range(1, i+1):
        fact *= j
        sum += pow(x, i) / fact
    i += 1
print("The sum of the series = ",sum)
"""
# 9. Write a program to find the sum of series: (1 + (1+2) + (1+2+3) + ... + till N)
"""
print("Enter the range of number : ")
n = int(input())
print("Enter the value of x : ")
x = int(input())
sum = 0
i = 1
while i <= n:
    for j in range(1, i+1):
        sum += j
    i += 1
print("The sum of the series = ",sum)
"""
# 10. Write a program to find the sum of series: (1 + (1*2) + (1*2*3) + ... + till N)
"""
n = int(input("Enter the range of number:"))
sum_series = 0
i = 1
while i <= n:
    multiply = 1
    for j in range(1, i+1):
        multiply *= j
    sum_series += multiply
    i += 1
print("The sum of the series = ",sum_series)
"""
# 11. Write a Program to find the sum of series: 1! + 2! + 3! + ... + n!
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
# 12. Write a program to find the sum of series: 1!/1 + 2!/2 + 3!/3 + ... + n!/n
"""
print("Enter the range of number : ")
n = int(input())
sum = 0.0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += fact / i
print("The sum of the series =", sum)
"""
# 13. Write a program to find the sum of series: 1^1/1 + 2^2/2 + 3^3/3 + ... + n^n/n
"""
import math
print("Enter the range of number : ")
n = int(input())
sum = 0.0
for i in range(1, n+1):
    sum += pow(i, i) / i
print("The sum of the series =", sum)
"""
# 14. Write a program to find the sum of series: 1^1/1! + 2^2/2! + 3^3/3! + ... + n^n/n!
"""
import math
print("Enter the range of number : ")
n = int(input())
sum = 0.0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += pow(i, i) / fact
print("The sum of the series =", sum)
"""
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
# 16. Write a Program to the find sum of series: 5^2 + 10^2 + 15^3 + ... + N^2
"""
import math
print("Enter the range of number(Limit) : ")
n = int(input())
i = 5
sum = 0
while i <= n:
    sum += pow(i, 2)
    i += 5
print("The sum of the series =", sum)
"""
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
# 18. Write a program to find the sum of series: 1 + 4 - 9 + 16 - 25 + ... + N
"""
import math
print("Enter the range of number(Limit) : ")
n = int(input())
i = 2
sum = 1
while i <= n:
    if i % 2 == 0:
        sum += pow(i, 2)
    else:
        sum -= pow(i, 2)
    i += 1
print("The sum of the series =", sum)
"""
# 19. Write a program to find the sum of series: 1 + 1/3 + 1/5 + 1/7 + ... + 1/(N+2)
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
# 20. Write a Program to find the sum of series: 1 + 4 + 9 + 16 + 25 + ... + N
"""
import math
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
sum = 0.0
while i <= n:
    sum += pow(i, 2)
    i += 1
print("The sum of the series =", sum)
"""
# 21. Write a program to find the sum of series: 1/2! + 2/3! + 3/5! + 4/6! + ... + N/(N+1)!
"""
n = int(input("Enter the range of number(Limit):"))
i = 1
sum = 0.0
while i <= n:
    sum += float(i / fact(i + 1))
    i += 1
print("The sum of the series =", sum)
"""
# 22. Write a Program to Find the sum of series: 1/1! + 2/2! + 3/3! + ... + N/N!
"""
n = int(input("Enter the range of number : "))
sum = 0.0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += i / fact
print("The sum of the series =", sum)
"""
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
# 24. Write a Program to Find the sum of series: 1 + 11 + 111 + 1111 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
p = 1
for i in range(1, n+1):
    sum += p
    p = (p * 10) + 1
print("The sum of the series =", sum)
"""
# 25. Write a Program to Find the sum of series: 1/2 + 2/3 + 3/4 + 4/5 + ... + (N-1)/N
"""
n = int(input("Enter the range of number : "))
sum = 0.0
for i in range(1, n+1):
    sum += i / (i + 1)
print("The sum of the series =", sum)
"""
# 26. Write a Program to Find the sum of series: 2 + 4 + 6 + 8 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
i = 0
while i <= n:
    sum += i
    i += 2
print("The sum of the series =", sum)
"""
# 27. Write a Program to Find the sum of series: 9 + 99 + 999 + 9999 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
p = 9
for i in range(1, n+1):
    sum += p
    p = (p * 10) + 9
print("The sum of the series =", sum)
"""
# 28. Write a Program to Find the sum of series: 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/N!
"""
n = int(input("Enter the range of number : "))
sum = 0.0
fact = 1
for i in range(1, n+1):
    fact *= i
    sum += 1 / fact
print("The sum of the series =", sum)
"""
# 29. Write a Program to Find the sum of series: 3 + 33 + 333 + 3333 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
p = 3
for i in range(1, n+1):
    sum += p
    p = (p * 10) + 3
print("The sum of the series =", sum)
"""
# 30. Write a Program to Find the sum of series: 3 + 7 + 13 + 21 + 31 + ... + N
"""
n = int(input("Enter the range of number : "))
sum = 0
for i in range(2, n+2):
    sum += 1 + (i * (i-1))
print("The sum of the series =", sum)
"""
# 31. Write a Program to Find the sum of series: 1³ + 2³ + 3³ + 4³ + ... + N³
"""
n = int(input("Enter the range of number : "))
sum = 0
for i in range(1, n+1):
    sum += pow(i, 3)
print("The sum of the series =", sum)
"""

# 1. Write a program Program to print Arithmetic series 1 4 7 10 ...
"""
print("Enter the First Number : ")
first_num = int(input())
print("Enter the range of number(Limit) : ")
n = int(input())
print("Enter the Difference Between two Number : ")
diff = int(input())
while first_num <= n:
     print(first_num, end=" ")
     first_num += diff
"""
# 2. Write a Program to Print Square Number series 1 4 9 16 ...
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
while i <= n:
    print(i * i, end=" ")
    i += 1
"""
# 3. Write a Program to print Cube Number series 1 8 27 64 ...
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
while i <= n:
    print(i * i * i, end=" ")
    i += 1
"""
# 4. Write a Program to print Triangular Number series 1 3 6 10 15 ...
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
while i <= n:
    print((int) ((i * (i + 1)) / 2), end=" ")
    i += 1
"""
# 5. Write a Program to print the Fibonacci series.
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
a = 0
b = 1
c = a + b
while i <= n:
    print(c, end=" ")
    c = a + b
    a = b
    b = c
    i += 1
"""
# 6. Write a program to print series: -1 4 -7 10 -13 16 -19 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
se = 1
while i <= n:
    if i % 2 == 0:
        print(se, end=" ")
    else:
        print(-1 * se, end=" ")
    se += 3
    i += 1
"""
# 7. Write a program to print series: 2 15 41 80 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
value = 2
while i <= n:
    print(value, end=" ")
    value += i * 13
    i += 1
"""
# 8. Write a program to print series: 10 5 60 15 110 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
a = 10
b = 5
i = 1
while i <= n:
    if i%2 == 0:
        print(b, end=" ")
        b += 10
    else:
        print(a, end=" ")
        a += 50
    i += 1
"""
# 9. Write a program to print series: 0 6 10 17 22 30 36 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
a = 0
b = 6
k = 10
p = 11
while i <= n:
    if i % 2 == 0:
        print(b, end=" ")
        b += p
        p += 2
    else:
        print(a, end=" ")
        a += k
        k += 2
    i += 1
"""
# 10. Write a program to print series: 6 9 14 21 30 41 54 ... N
"""
print("Enter the range of number(Limit) : ")
n = int(input())
i = 1
j = 3
value = 6
while i <= n:
    print(value, end=" ")
    value += j
    j += 2
    i += 1
"""
# 11. Write a Program to print series: 1 2 4 8 16 32 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
while i <= n:
    print(i, end=" ")
    i *= 2
"""
# 12. Write a Program to print series: 1 3 7 15 31 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 0
while i <= n:
    pr = (pr * 2) + 1
    print(pr, end=" ")
    i += 1
"""
# 13. Write a Program to print series: 1 -2 6 -15 31 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 1
while i <= n:
    if i % 2 == 0:
        print(-1 * pr, end=" ")
    else:
        print(pr, end=" ")
    pr += pow(i, 2)
    i += 1
"""
# 14. Write a Program to print series: 6 11 21 36 56 ...N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 6
diff = 5
while i <= n:
    print(pr, end=" ")
    pr = pr + diff
    diff = diff + 5
    i += 1
"""
# 15. Write a Program to print series: 1 22 333 4444 ... N
"""
n=int(input("Enter the range of number(Limit) : "))
for out in range(n+1):
    for i in range(out):
        print(out, end="")
    print(end=" ")
"""
# 16. Write a Program to print series: 0 2 8 14 24 34 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 0
while i <= n:
    if i % 2 == 0:
        pr=pow(i, 2) - 2
        print(pr, end=" ")
    else:
        pr = pow(i, 2) - 1
        print(pr, end=" ")
    i += 1
"""
# 17. Write a Program to print series: 1 2 5 8 15 28 51 94 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 4
if n >= 1:
    print("1  ", end=" ")
if n >= 2:
    print("2", end=" ")
if n >= 3:
    print("5", end=" ")
a = 1
b = 2
c = 5
while i <= n:
    d = a + b + c
    a = b
    b = c
    c = d
    print(d, end=" ")
    i += 1
"""
# 18. Write a Program to print series: 0 2 6 12 20 30 42 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
while i <= n:
    print((i * i) - i, end=" ")
    i += 1
"""
# 19. Write a Program to print series: 2 4 7 12 21 38 71 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 0
pr = 2
print("2 ", end=" ")
while i < n-1:
    pr = (pr * 2) - i
    print(pr, end = " ")
    i += 1
"""
# 20. Write a Program to print series: 1 9 17 33 49 73 97 ... N
"""
n = int(input("Enter the range of number(Limit) : "))
i = 1
pr = 0
while i <= n:
    if i % 2 == 0:
        pr = 2 * pow(i, 2) + 1
        print(pr, end=" ")
    else:
        pr = 2 * pow(i, 2) - 1
        print(pr, end=" ")
    i += 1
"""

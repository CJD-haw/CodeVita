
"""
Problem Statement
    A parking lot in a mall has RxC number of parking spaces.
    Each parking space will either be  empty(0) or full(1).
    The status (0/1) of a parking space is represented as the element of the matrix.
    The task is to find index of the row(R) in the parking lot that has the most of the parking spaces full(1).

Note :
    RxC- Size of the matrix
    Elements of the matrix M should be only 0 or 1.
"""

"""r=int(input())
c=int(input())
sum=0
m=0
id=0
for i in range(r):
    for j in range(c):
        sum+=int(input())
    if sum>m:
        m=sum
        id=i+1
    sum=0
print(id)"""

row, col = int(input('Rows : ')), int(input('Columns : '))
w = []
s = []
for r in range(row):
    p = []
    for c in range(col):
        p.append(int(input()))
    w.append(p)
    s.append(sum(p))

# print(w)
# print(s)

result = s.index(max(s)) + 1
print('Maximum Cars in Slot Number ', result)

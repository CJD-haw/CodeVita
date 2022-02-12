
"""
Problem Statement
    Given an integer array Arr of size N.
    Task is to find the count of elements whose value is greater than all of its prior elements.

Note : 1st element of the array should be considered in the count of the result.

For example,
    Arr[]={7,4,8,2,9}
    As 7 is the first element, it will consider in the result.
    8 and 9 are also the elements that are greater than all of its previous elements.
    Since total of  3 elements is present in the array that meets the condition.
    Hence the output = 3.
"""

"""
nd array or list of length N <= 20
count the element > first element
each element < 10,000
"""

N = int(input())
if N >= 1 | N <= 20:
    A = [int(input()) for i in range(N)]
    c = 0
    for v in A:
        if v < 10000:
            if v >= A[0]:
                c += 1
        else:
            print('Invalid Input')
            exit()
    print(c)
else:
    print('Invalid Input')

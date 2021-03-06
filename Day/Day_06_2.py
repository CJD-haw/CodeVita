
"""
Airport security officials have confiscated several item of the passengers at the security check point.
All the items have been dumped into a huge box (array).
Each item possesses a certain amount of risk[0,1,2].
Here, the risk severity of the items represent an array[] of N number of integer values.
The task here is to sort the items based on their levels of risk in the array.
The risk values range from 0 to 2.

Example 1:
Input:
7                       -> Value of N
[1,0,2,0,1,0,2]         -> Element of arr[0] to arr[N-1], while input each element is separated by new line.
Output:
0 0 0 1 1 2 2           -> Element after sorting based on risk severity

Example 2:
input: 10               -> Value of N
[2,1,0,2,1,0,0,1,2,0]   -> Element of arr[0] to arr[N-1], while input each element is separated by a new line.
Output:
0 0 0 0 1 1 1 2 2 2     ->Elements after sorting based on risk severity.

Explanation:
    In the above example, the input is an array of size N consisting of only 0’s, 1’s and 2s.
    The output is a sorted array from 0 to 2 based on risk severity.
"""

"""
n = int(input())
a = list(map(int, input().split()))
r = 0
m = 0
h = n-1
while m <= h:
    if a[m] == 0:
        a[r], a[m] = a[m], a[r]
        r += 1
        m += 1
    elif a[m] == 1:
        m += 1
    else:
        a[m], a[h] = a[h], a[m]
        h -= 1
for i in a:
    print(i, end=" ")
"""

n = int(input())
a = [int(input()) for v in range(n)]
a.sort()

# print(a)
for v in a:
    print(v, end=' ')

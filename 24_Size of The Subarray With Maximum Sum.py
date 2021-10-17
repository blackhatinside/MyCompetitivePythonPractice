'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


def MaxSumContSubArr(arr, size):	# KADANE'S ALGORITHM
    maxSum = -1e9
    curSum = beg = end = start = 0
    for i in range(size):
        curSum = curSum + arr[i]
        if curSum > maxSum:
            maxSum = curSum
            beg = start
            end = i
        if curSum < 0:
            curSum = 0
            start = i + 1
    return end - beg + 1

for ii in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	ans = MaxSumContSubArr(arr, n)
	print(ans)


'''

#----INPUT----

1
6
1 -2 1 1 -2 1

#----OUTPUT----

2

'''

''' EXPLANATION
KADANE'S ALGORITHM IMPLEMENTED FOR BOTH POSITIVE & NEGATIVE ARRAYS
# '''
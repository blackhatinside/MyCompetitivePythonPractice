'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


tcs = int(input())
for tc in range(tcs):
	n = int(input())
	arr = list(map(int, input().split()))
	xorsum = 0
	for i in range(n):
		xorsum = xorsum ^ arr[i]
	print(xorsum)


'''

#----INPUT----

2
5
5 2 4 3 1
7
-5 -12 87 2 88 20 11

#----OUTPUT----

-9
0

'''

''' SHORTER CODE
for tc in range(int(input())):
	n, xorsum = int(input()), 0
	arr = list(map(int, input().split()))
	for x in arr:
		xorsum ^= x
	print(xorsum)
# '''
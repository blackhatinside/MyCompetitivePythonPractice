'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


def myComp(a):	# EVEN-ODD SORT
	return a % 2
tcs = 1
for i in range(tcs):
	n = int(input())
	arr = list(map(int, input().split()))
	arr = sorted(arr, key = myComp)
	print(*arr)


'''

#----INPUT----

8
2 4 3 1 8 6 5 7

#----OUTPUT----

2 4 8 6 3 1 5 7

'''

#SHORTER CODE
# n = int(input())
# print(*sorted(list(map(int, input().split())), key = lambda a : a % 2))


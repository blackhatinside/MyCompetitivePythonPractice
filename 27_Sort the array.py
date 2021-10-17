'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for ii in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	print(*arr)


'''

#----INPUT----

2
8
2 -4 3 -1 8 -5 0 6
8
-2 -4 -8 -6 -3 -1 -5 -7

#----OUTPUT----

-5 -4 -1 0 2 3 6 8
-8 -7 -6 -5 -4 -3 -2 -1

'''

''' SHORTER CODE
for _ in range(int(input())):
	n = int(input())
	print(*sorted(map(int, input().split())))
# '''
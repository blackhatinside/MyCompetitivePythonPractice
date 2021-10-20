'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for tc in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort(key = None, reverse = True)
	print(arr)


'''

#----INPUT----

2
8
2 -4 3 -1 8 -5 0 6
8
-2 -4 -8 -6 -3 -1 -5 -7

#----OUTPUT----

8 6 3 2 0 -1 -4 -5
-1 -2 -3 -4 -5 -6 -7 -8

'''

''' SHORTER CODE
for tcs in range(int(input())):
	n = int(input())
	print(sorted(list(map(int, input().split())), reverse = True))
# '''
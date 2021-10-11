'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = sorted(list(map(int, input().split())))
	print(arr[k - 1], arr[n - k])


'''

#----INPUT----

2
8 3
2 -4 3 -1 8 -5 0 6
9 5
-2 -4 -8 -6 -3 -1 -5 -7 0

#----OUTPUT----

-1 3
-4 -4

'''

#SHORTER CODE
# for _ in range(int(input())):
# 	n, k = map(int, input().split())
# 	arr = sorted(map(int, input().split()))
# 	print(arr[k - 1], arr[n - k])
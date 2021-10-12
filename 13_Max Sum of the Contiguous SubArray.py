'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	ans = curmax = arr[0]
	for i in range(1, n):	#DP APPROACH
		curmax = max(arr[i], curmax + arr[i])
		ans = max(ans, curmax)
	print(ans)


'''

#----INPUT----

1
8
-2 -3 4 -1 -2 1 5 -3

#----OUTPUT----

7

'''

#SHORTER CODE
# for _ in range(int(input())):
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	ans = curmax = arr[0]
# 	for i in range(i, n):	#DP APPROACH
# 		curmax = max(a[i], curmax + a[i])
# 		ans = max(ans, curmax)
# 	print(ans)

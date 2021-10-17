'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


# for _ in range(int(input())):
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	k = int(input())
# 	for i in range(k, k + n):
# 		print(arr[i % n], end = " ")
# 	print()


'''

#----INPUT----

1
5
21 22 23 24 25
3

#----OUTPUT----

24 25 21 22 23

'''

''' SHORTER CODE
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	k = int(input())
	print(*arr[k:] + arr[:k])
# '''
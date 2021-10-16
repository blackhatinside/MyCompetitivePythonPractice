'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	for i in range(n // 2):
		arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
	for i in range(n):
		print(arr[i], end = " ")
	print()


'''

#----INPUT----

2
8
2 4 3 1 8 6 5 7
9
2 4 3 1 8 6 9 5 7

#----OUTPUT----

8 6 5 7 2 4 3 1
7 5 9 6 8 1 3 4 2

'''

''' SHORTER CODE
for _ in range(int(input())):
	n = int(input())
	print(*list(map(int, input().split()))[::-1])
# '''
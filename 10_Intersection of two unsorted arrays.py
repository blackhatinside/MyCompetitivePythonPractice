'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n1 = int(input())
	n2 = int(input())
	arr1 = set(map(int, input().split()))
	arr2 = set(map(int, input().split()))
	ans = set()
	for x in arr1:
		if x in arr2:
			ans.add(x)
	print(*ans)


'''

#----INPUT----

1
7
9
1 2 5 6 2 3 5
2 4 5 6 8 9 4 6 5

#----OUTPUT----

2 5 6

'''

#SHORTER CODE
# for _ in range(int(input())):
# 	n1 = int(input())
# 	n2 = int(input())
# 	arr1 = set(map(int, input().split()))
# 	arr2 = set(map(int, input().split()))
# 	print(*arr1.intersection(arr2))
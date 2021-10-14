'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for tc in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	for i in range(n):
		print(arr[i], end = " ")
		print(arr[i + n], end = " ")
	print()


'''

#----INPUT----

2
7
3 7 90 20 10 50 40
5
1 4 5 9 1

#----OUTPUT----

4
1

'''

''' SHORTER CODE
for tc in range(int(input())):
	n = int(input())
	arr = sorted(map(int, input().split()))
	for i in range(n):
		print(arr[i], arr[i + n], end = " ")
	print()
# '''

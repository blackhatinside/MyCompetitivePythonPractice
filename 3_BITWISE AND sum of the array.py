'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


tcs = int(input())
for i in range(tcs):
	n = int(input())
	arr = list(map(int, input().split()))
	ans = -1	# -1 IS IDENTITY ELEMENT
	for i in range(n):
		ans = ans & arr[i]
	print(ans)


'''

#----INPUT----

4
4
3 11 3 7
5
11 7 15 3 7
8
2 -4 3 -1 8 -5 0 6
8
-2 -4 -8 -6 -3 -1 -5 -7

#----OUTPUT----

3 -1 8 -5 0 6 2 -4
-6 -3 -1 -5 -7 -2 -4 -8

'''

#SHORTER CODE
# for i in range(int(input())):
# 	n, ans = int(input()), -1
# 	arr = list(map(int, input().split()))
# 	for i in range(n): ans &= arr[i]
# 	print(ans)
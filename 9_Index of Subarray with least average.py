'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	cursum = res_ind = 0
	# cursum = sum(x for x in arr[:k])
	for i in range(k):
		cursum += arr[i]
	minsum = cursum
	for i in range(k, n):
		cursum = cursum + arr[i] - arr[i - k]
		if cursum < minsum:
			minsum = cursum
			res_ind = i - k + 1
	print(res_ind, res_ind + k - 1)


'''

#----INPUT----

1
7 3
3 7 90 20 10 50 40

#----OUTPUT----

3 5

'''

#SHORTER CODE
# for _ in range(int(input())):
# 	n, k = map(int, input().split())
# 	arr = list(map(int, input().split()))
# 	minsum = cursum = sum(arr[:k])
# 	res_ind = 0
# 	for i in range(k, n):
# 		cursum += arr[i] - arr[i - k]
# 		if cursum < minsum:
# 			minsum = cursum
# 			res_ind = i - k + 1
# 	print(res_ind, res_ind + k - 1)

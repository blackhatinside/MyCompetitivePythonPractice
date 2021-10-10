'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


tcs = 1
for i in range(tcs):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	presum = 0
	for i in range(0, k, 1):
		# PRECOMPUTE SUM TO SAVE TIME
		presum += arr[i]
	ans = [presum, ]
	for i in range(k, n, 1):
		presum += arr[i]
		presum -= arr[i - k]
		ans.append(presum)
	print(*ans)


'''

#----INPUT----

8 3
2 -4 3 -1 8 -5 0 6

#----OUTPUT----

1 -2 10 2 3 1

'''

#SHORTER CODE
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = [0, ]
# for i in range(0, k, 1):
# 	ans[0] += arr[i]
# for i in range(k, n, 1):
# 	ans.append(ans[-1] + arr[i] - arr[i - k])
# print(*ans)
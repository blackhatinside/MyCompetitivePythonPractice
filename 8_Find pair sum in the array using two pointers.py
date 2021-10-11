'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


def isPairSum(a, n, k):
	global x, y
	i, j = 0, n - 1
	while i < j:
		if a[i] + a[j] == k:
			x, y = i, j
			return 1
		elif a[i] + a[j] > k:
			j = j - 1
		else:
			i = i + 1
	return 0
for _ in range(int(input())):
	sz, key = map(int, input().split())
	arr = list(map(int, input().split()))
	x, y = -1, -1
	if isPairSum(arr, sz, key):
		print("YES")
		print(arr[x], arr[y])
	else:
		print("NO")


'''

#----INPUT----

1
7 14
1 3 5 7 9 10 11

#----OUTPUT----

YES
3 11

'''

#SHORTER CODE
# import collections as col
# for _ in range(int(input())):
# 	hp = col.defaultdict(lambda: 0)
# 	n, k = map(int, input().split())
# 	arr = list(map(int, input().split()))
# 	ans, i, j = 0, 0, 0
# 	hp = col.defaultdict(lambda: 0)
# 	for x in arr:
# 	    if x >= k:
# 	        continue
# 	    if hp[k - x] != 0:
# 	        ans += hp[k - x]
# 	        i, j = x, k - x
# 	    hp[x] += 1
# 	if ans:
# 		print("YES\n", i, " ", j, "\n", sep = "", end = "")
# 	else:
# 		print("NO")

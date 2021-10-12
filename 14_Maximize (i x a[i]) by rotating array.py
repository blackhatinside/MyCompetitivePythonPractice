'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	tot = curval = 0
	for i in range(n):	#PRECOMPUTATION
		tot += arr[i]
		curval += i * arr[i]
	ans = curval
	for i in range(n):	# UPTO n - 1 ENOUGH, AFTER THAT CYCLE REPEATS
		nxtval = curval - (tot - arr[i]) + (arr[i] * (n - 1))
		ans = max(ans, nxtval)
		curval = nxtval
	print(ans)


'''

#----INPUT----

4
4
8 3 1 2
5
11 7 15 3 7
8
2 -4 3 -1 8 -5 0 6
9
-2 -4 -8 -6 -3 -9 -1 -5 -7

#----OUTPUT----

29
110
67
-156

'''

'''
EXPLANATION
index: 1 2 3 4
array: 8 3 1 2

index: 1 2 3 4
array: 3 1 2 8

index: 1 2 3 4
array: 1 2 8 3

index: 1 2 3 4
array: 2 8 3 1

index: 1 2 3 4
array: 8 3 1 2

precomputation saves time of calculating arr[i] * i for each iteration

first element goes to last and its i value becomes maximum on left shift.
for rest of the elements in the array i value reduces by 1 on left shift.
'''
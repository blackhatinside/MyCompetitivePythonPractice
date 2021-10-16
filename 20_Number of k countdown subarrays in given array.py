'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	ctr = ans = 0
	for i in range(n):
		if arr[i] == arr[i - 1] - 1:
			ctr = ctr + 1
		else:
			ctr = 0
		if arr[i] == 1 and ctr >= k - 1:
			ans = ans + 1
	print(ans)


'''

#----INPUT----

3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100

#----OUTPUT----

2
0
1

'''

''' EXPLANATIONS
to find the total number of countdown 
subarrays with exactly k elements in it
eg. {3,2,1} is a decreasing subarray of 
{4,3,2,1} with exactly 3 elements in it 
'''
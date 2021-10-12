'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


# for _ in range(int(input())):	# KADANE'S ALGORITHM
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	maxsum = cursum = 0
# 	lowsum = -1000000007
# 	for i in range(n):
# 		if arr[i] > lowsum:		# FOR NEGATIVE ARRAYS
# 			lowsum = arr[i]
# 		cursum = cursum + arr[i]
# 		if cursum > maxsum:
# 			maxsum = cursum
#		maxsum = cursum if cursum > maxsum else maxsum
# 		if cursum < 0:
# 			cursum = 0 	# RESETTING THE STARTING POINTER
# 	print(maxsum if maxsum > 0 else lowsum)


'''

#----INPUT----

1
8
-2 -3 4 -1 -2 1 5 -3

#----OUTPUT----

7

'''


''' 
SHORTER CODE
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	maxsum = cursum = 0
	lowsum = -1000000007
	for i in range(n):
		lowsum = arr[i] if arr[i] > lowsum else lowsum		# FOR NEGATIVE ARRAYS
		cursum += arr[i]
		maxsum = max(cursum, maxsum)
		cursum = 0 if cursum < 0 else cursum
	print(maxsum if maxsum > 0 else lowsum)
'''

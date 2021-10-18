'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


from collections import Counter, defaultdict
for tcs in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	hp = defaultdict(lambda : 0)
	for i in range(n):
		hp[arr[i]] = [i, 0]
	for i in range(n):
		hp[arr[i]][1] = hp[arr[i]][1] + 1
	freq = list(); sz = 0;
	for k in hp.keys():
		freq.append([k, hp[k]])
		sz = sz + 1
	freq.sort(key = lambda ele : (-ele[1][1], ele[1][0]))
	for i in range(sz):
		count = freq[i][1][1]
		while count > 0:
			print(freq[i][0], end = " ")
			count = count - 1


'''

#----INPUT----

1
10
2 5 2 6 -1 9999999 5 8 8 8

#----OUTPUT----

8 8 8 2 2 5 5 6 -1 9999999

'''

''' SHORTER CODE
# from collections import Counter, defaultdict
# for tcs in range(int(input())):
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	hp = dict(defaultdict(int, Counter(arr)))
# 	arr.sort(key = lambda ele : (-hp[ele], ele))	# first sort by decr. freq. then sort by incr. elem.
# 	print(*arr)
# '''
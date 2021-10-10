'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


import math
tcs = int(input())
for i in range(tcs):
	n = int(input())
	arr = list(map(int, input().split()))
	cnteve, cntodd = 0, 0
	for i in range(n):
		if arr[i] % 2 == 0:
			cnteve += 1
		else:
			cntodd += 1
	eveind = math.floor(n / 2)
	oddind = math.ceil(n / 2)
	# EVEN + ODD = ODD
	x = min(cnteve, oddind)
	y = min(cntodd, eveind)
	ans = x + y
	print(ans)


'''

#----INPUT----

3
3
1 2 3
3
2 4 5
2
2 4

#----OUTPUT----

2
3
1

'''

#SHORTER CODE
# from math import floor as fF, ceil as cC
# for _ in range(int(input())):
# 	n = int(input())
# 	ie, io, co, ce = fF(n/2), cC(n/2), 0, 0
# 	arr = list(map(int, input().split()))
# 	for e in arr:
# 		co += (e % 2 == 1)
# 		ce += (e % 2 == 0)
# 	print(min(ce, io) + min(co, ie))

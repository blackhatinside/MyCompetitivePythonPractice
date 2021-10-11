'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n, cost = map(int, input().split())
	item = tot = 0
	arr = list(map(int, input().split()))
	arr.sort()
	for x in arr:
		if tot + x > cost:
			break
		tot += x
		item += 1
	print(item)


'''

#----INPUT----

1
5 66
24 21 23 25 22

#----OUTPUT----

3

'''

#SHORTER CODE
# for _ in range(int(input())):
# 	n, c = map(int, input().split())
# 	i = t = 0
# 	for x in sorted(map(int, input().split())):
# 		if t + x > c:
# 			break
# 		t += x
# 		i += 1
# 	print(i)

'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for tc in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	hp = list()
	ans = hp[:]
	odd = hp[:]
	eve = hp[:]
	for i in range(n):
		if arr[i] % 2 == 0:
			eve.append(arr[i])
		else:
			odd.append(arr[i])
		hp.append([i, arr[i] % 2])
	eve.sort()
	odd.sort(reverse = True)
	for i in range(len(hp)):
		if hp[i][1] == 0:
			ans.append(eve.pop())
		else:
			ans.append(odd.pop())
	print(*ans)


'''

#----INPUT----

2
5
5 2 4 3 1
7
-5 -12 87 2 88 20 11

#----OUTPUT----

8 6 3 2 0 -1 -4 -5
-1 -2 -3 -4 -5 -6 -7 -8

'''

''' SHORTER CODE
for tc in range(int(input())):
	n, hp = int(input()), list()
	arr = list(map(int, input().split()))
	ans = hp[:]; odd = hp[:]; eve = hp[:];
	for i in range(n):
		if arr[i] % 2 == 0:
			eve.append(arr[i])
		else:
			odd.append(arr[i])
		hp.append([i, arr[i] % 2])
	eve.sort()
	odd.sort(reverse = True)
	for i in range(len(hp)):
		if hp[i][1] == 0:
			ans.append(eve.pop())
		else:
			ans.append(odd.pop())
	print(*ans)
# '''
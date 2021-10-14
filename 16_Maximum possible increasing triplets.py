'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	brr = list(map(int, input().split()))
	crr = list(map(int, input().split()))
	arr.sort()
	brr.sort()
	crr.sort()
	cnt = i = j = k = 0
	while i < n:
		while j < n and brr[j] <= arr[i]:
			j = j + 1
		if j == n:
			break
		while k < n and crr[k] <= brr[j]:
			k = k + 1
		if k == n:
			break
		cnt = cnt + 1
		i += 1
		j += 1
		k += 1
	print(cnt)


'''

#----INPUT----

3
5
9 6 14 1 8
2 10 3 12 11
15 13 5 7 4
1
10
20
30
3
1 1 1
1 1 2
2 2 2

#----OUTPUT----

3
1
0

'''


''' SHORTER CODE
for _ in range(int(input())):
	n = int(input())
	arr = sorted(map(int, input().split()))
	brr = sorted(map(int, input().split()))
	crr = sorted(map(int, input().split()))
	cnt = i = j = k = 0
	while i < n:
		while j < n and brr[j] <= arr[i]:
			j = j + 1
		if j == n:
			break
		while k < n and crr[k] <= brr[j]:
			k = k + 1
		if k == n:
			break
		cnt, i, j, k = cnt + 1, i + 1, j + 1, k + 1
	print(cnt)
# '''

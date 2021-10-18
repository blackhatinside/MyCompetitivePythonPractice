'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


tcs = int(input())
for tcs in range(tcs):
	m = int(input())
	n = int(input())
	p = int(input())
	arr1 = list(map(int, input().split()))
	arr2 = list(map(int, input().split()))
	arr3 = list(map(int, input().split()))
	arr1.sort()
	arr2.sort()
	arr3.sort()
	diff = 1e9
	i = j = k = 0
	maxx = minn = summ = 0
	while i < n and j < n and k < n:
		vals = arr1[i], arr2[j], arr3[k]
		summ = sum(vals)
		maxx = max(vals)
		minn = min(vals)
		if minn == arr1[i]:
			i = i + 1
		elif minn == arr2[j]:
			j = j + 1
		else:
			k = k + 1
		if maxx - minn < diff:
			diff = maxx - minn
			res_mid = summ - (maxx + minn)
			res_max = maxx
			res_min = minn
	print(res_max, res_mid, res_min)


'''

#----INPUT----

1
3
3
3
5 2 8
10 7 12
9 14 6

#----OUTPUT----

7 6 5

'''

''' SHORTER CODE
ii = lambda : int(input())
sli = lambda : sorted(list(map(int, input().split())))
for tcs in range(int(input())):
	m, n, p, diff = ii(), ii(), ii(), 1e9
	arr1, arr2, arr3 = sli(), sli(), sli()
	i = j = k = maxx = minn = summ = 0
	while i < n and j < n and k < n:
		vals = arr1[i], arr2[j], arr3[k]
		summ, maxx, minn = sum(vals), max(vals), min(vals)
		i = i + (minn == arr1[i])
		j = j + (minn == arr2[j])
		k = k + (minn == arr3[k])
		if maxx - minn < diff:
			diff = maxx - minn
			res_mid = summ - (maxx + minn)
			res_max = maxx
			res_min = minn
	print(res_max, res_mid, res_min)
# '''
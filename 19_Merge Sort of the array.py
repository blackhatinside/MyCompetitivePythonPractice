'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


def mergeSort(arr):
	sz = len(arr)
	if sz > 1:
		mid = sz // 2
		l = arr[:mid]
		r = arr[mid:]
		mergeSort(l)
		mergeSort(r)
		i = j = k = 0
		while i < len(l) and j < len(r):
			if l[i] < r[j]:
				arr[k] = l[i]
				i = i + 1
			else:
				arr[k] = r[j]
				j = j + 1
			k = k + 1
		print("L:",l)
		while i < len(l):
			arr[k] = l[i]
			i = i + 1
			k = k + 1
		print("R:",r)
		while j < len(r):
			arr[k] = r[j]
			j = j + 1
			k = k + 1
	return arr
n = int(input())
arr = list(map(int, input().split()))
print(mergeSort(arr))


'''

#----INPUT----

6
4 6 5 1 3 2

#----OUTPUT----

1 2 3 4 5 6

'''

''' SHORTER CODE
for tc in range(int(input())):
	r = int(input())
	arr = sorted(map(int, input().split()))
	for i in range(r):
		print(arr[i], arr[i + r], end = " ")
	print()
# '''

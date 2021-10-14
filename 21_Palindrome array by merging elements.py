'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for tc in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	i, j = 0, n - 1; ans = 0;
	while i <= j:
		if arr[i] == arr[j]:
			i = i + 1
			j = j - 1
		elif arr[i] > arr[j]:
			j = j - 1
			arr[j] = arr[j] + arr[j + 1]
			ans = ans + 1
		else:
			i = i + 1
			arr[i] = arr[i] + arr[i - 1]
			ans = ans + 1
	print(ans)


'''

#----INPUT----

2
7
3 7 90 20 10 50 40
5
1 4 5 9 1

#----OUTPUT----

4
1

'''

''' SHORTER CODE
for tc in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	i, j, ans = 0, 0, n - 1
	while i <= j:
		if arr[i] == arr[j]:
			i += 1; j -= 1;
		elif arr[i] > arr[j]:
			j -= 1
			arr[j] = arr[j] + arr[j + 1]
			ans += 1
		else:
			i += 1
			arr[i] = arr[i] + arr[i - 1]
			ans += 1
	print(ans)
# '''

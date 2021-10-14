'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	max_value=arr[0]
	min_value=arr[0]
	ans=arr[0]
	for i in range(1,n):
	    choice1=arr[i]*max_value
	    choice2=arr[i]*min_value
	    # if -ve ele then min * ele, else max * ele, also compare ele alone by itself
	    max_value=max(arr[i],choice1,choice2)
	    min_value=min(arr[i],choice1,choice2)
	    ans=max(ans,max_value)
	print(ans)


'''

#----INPUT----

4
5
6 -3 -10 0 2
10
8 -2 -2 0 8 0 -6 -8 -6 -1
7
9 0 8 -1 -2 -2 6
9
2 4 3 1 8 -6 9 5 7

#----OUTPUT----

180
288
24
315

'''

''' SHORTER CODE
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	maxval = minval = ans = arr[0]
	for i in range(1, n):
		x = arr[i] * maxval
		y = arr[i] * minval
		maxval = max(arr[i], x, y)
		minval = min(arr[i], x, y)
		ans = max(ans, maxval)
	print(ans)
# '''

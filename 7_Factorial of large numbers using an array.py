'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


MAXDIGITS = 50000
def multiply(x, res, res_size):
	carry = 0 	# INITIALLY CARRY IS ZERO
	i = 0
	while i < res_size:		# MULTIPLY ALL DIGITS of (n-1)! WITH n
		prod = res[i] * x + carry	# MULTIPLY AND ADD PREVIOUS CARRY
		res[i] = prod % 10	# STORE ONLY LAST DIGIT OF PRODUCT
		carry = prod // 10	# PASS THE CARRY OVER TO NEXT PLACE
		i = i + 1
	while carry > 0:	# DEALING WITH THE LEFT OVER CARRY
		res[res_size] = carry % 10
		carry = carry // 10
		res_size = res_size + 1
	return res_size
def factorial(n):
	res = [None] * MAXDIGITS
	res[0] = 1
	res_size = 1
	x = 2
	while x <= n:	# FACTORIAL FORMULA n!
		res_size = multiply(x, res, res_size)
		x = x + 1
	def printFactorial():
		i = res_size - 1
		while i >= 0:
			print(str(res[i]),sep="", end="")
			i = i - 1
	printFactorial()
tcs = int(input())
for i in range(tcs):
	n = int(input())
	factorial(n)
	print()


'''

#----INPUT----

3
10
20
50

#----OUTPUT----

3628800
2432902008176640000
30414093201713378043612608166064768844377641568960512000000000000

'''

#SHORTER CODE
# def multiply(x, res, digcnt):
# 	carry = 0 						# INITIALLY CARRY IS ZERO
# 	for i in range(digcnt):		# MULTIPLY ALL DIGITS of (n-1)! WITH n
# 		prod = res[i] * x + carry	# MULTIPLY AND ADD PREVIOUS CARRY
# 		res[i] = prod % 10			# STORE ONLY LAST DIGIT OF PRODUCT
# 		carry = prod // 10			# PASS THE CARRY OVER TO NEXT PLACE
# 	while carry:					# DEALING WITH THE LEFT OVER CARRY
# 		res[digcnt] = carry % 10
# 		carry //= 10
# 		digcnt += 1
# 	return digcnt
# def factorial(n):
# 	res = [None] * 50000			# INITIALIZE MAXIMUM NUMBER OF DIGITS IN ANSWER
# 	res[0] = digcnt = 1
# 	for x in range(2, n + 1):
# 		digcnt = multiply(x, res, digcnt)
# 	print(*res[:digcnt][::-1], sep="", end="\n")
# for tc in range(int(input())):
# 	factorial(int(input()))

'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


# GET ARRAY SIZE
n = int(input())

# GET ARRAY IN SINGLE LINE
arr = list(map(int, input().split()))

# PRINT ARRAY WITHOUT [,,,]
print(*arr)


'''

#----INPUT----

8
2 4 3 1 8 6 5 7

#----OUTPUT----

2 4 3 1 8 6 5 7

'''

#ONE LINER CODE FOR THE SAME
# n = int(input()); print(*list(map(int, input().split())));
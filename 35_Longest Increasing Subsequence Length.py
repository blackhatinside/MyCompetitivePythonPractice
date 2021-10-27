#!/usr/bin/env python

#INTRODUCTION
# '''           Meet my Codechef Doggie
#      |\_/|                  
#      | @ @   Woof! 
#      |   <>              _  
#      |  _/\------____ ((| |))
#      |               `--' |   
#  ____|_       ___|   |___.' 
# /_/_____/____/_______|
# I am here to guard this code, woof!
# Name : Cyberkid05 | Country : India
# '''

'''
    Author : Cyberkid
    Language : Python3
    email : thehappymentorkid@gmail.com
'''


#CODE
# import io, os, sys, 
# import math, functools, collections
# import bisect, heapq, numpy

# input = raw_input
# input = sys.stdin.readline
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# from statistics import mode
# from functools import reduce
# from bisect import bisect
# from collections import defaultdict
# from collections import Counter
# hp = defaultdict(lambda: 0)
# hp = collections.defaultdict(int, collections.Counter(arr))
# input = lambda: sys.stdin.readline().strip()
# imap = lambda: map(int,input().split())
# ilist = lambda: list(map(int, input().split()))
# sys.stdout.write(str(ans) + "\n")
# for line in sys.stdin

import sys, functools, collections
input = sys.stdin.readline
alp = "abcdefghijklmnopqrstuvwxyz"

def lis(arr, n):
    ans = [1] * n
    for i in range(1, n):
        subans = [ans[k] for k in range(i) if arr[k] < arr[i]]
        ans[i] = 1 + max(subans, default = 0)
    return max(ans, default = 0)

tcs = 1
# tcs = int(sys.stdin.readline())

def solve():
    sz = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(str(lis(arr, sz)) + "\n")

for tc in range(tcs):
    solve()

#     if solve():
#         print('Case #{}: {}'.format(tc, "YES"))
#     else:
#         print('Case #{}: {}'.format(tc, "NO"))


'''

#----INPUT----

9
10 22 9 33 21 50 41 60 80

#----OUTPUT----

6

'''

''' SHORTER CODE
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = [1] * n
for i in range(1, n):
    subans = [ans[k] for k in range(i) if arr[k] < arr[i]]
    ans[i] = 1 + max(subans, default = 0)
sys.stdout.write(str(max(ans, default = 0)) + "\n");
# '''
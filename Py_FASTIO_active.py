#!/usr/bin/env python

'''
    Name : cyberkid05 | Country : India
    Language : Python3
    email : thehappymentorkid@gmail.com
'''

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
# '''

#--MODULES BEGINS--
''' --python 2 and pypy begins--
from __future__ import division, print_function
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
# --python 2 and pypy ends-- '''
import io, os, re, sys, time
from io import BytesIO, IOBase
import math, functools, collections
# import bisect, heapq, numpy
# from contextlib import contextmanager
# from jinja2 import Template
#--MODULES ENDS--

#--SHORTHANDS BEGINS--
# input = raw_input
# input = sys.stdin.readline
# sys.stdout.flush()
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# from statistics import mode
# from functools import reduce
# from bisect import bisect
# from collections import defaultdict
# from collections import Counter
# hp = defaultdict(lambda: 0)
# hp = collections.defaultdict(int, collections.Counter(arr))
# arr = sorted(hp.items(), key = lambda kv:(kv[1], kv[0]))
# arr = list(filter(lambda a: a[1] != min(hp.values()), arr))
# input = lambda: sys.stdin.readline().strip()
# imap = lambda: map(int,input().split())
# ilist = lambda: list(map(int, input().split()))
# sys.stdout.write(str(ans) + "\n")
# for line in sys.stdin
# except: print(f'Unknown Error: {sys.exc_info()[1]}')
# w = int(input()); print("YNEOS"[(w > 2 and not w % 2)::2]);

# return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else list()
#--SHORTHANDS ENDS--

#----    CODE BEGINS    ----->
class Node:
    # __slots__ = ['data', 'next',]
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    # __slots__ = ['head', 'size',]
    def __init__(self):
        self.head = None
        self.size = 0
    def push_front(self, val):      #INSERT AT BEGINNING
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
    def push_back(self, val):       #INSERT AT END
        node = Node(val)
        if self.head == None:
            self.head = node
            #node.next = None BY DEFAULT
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            #node.next = None BY DEFAULT
        self.size += 1
    def pop_front(self):        #DELETION AT BEGINNING
        self.head = self.head.next
        self.size -= 1
    def pop_back(self):         #DELETION AT ENDING
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None # OR temp.next.next
        self.size -= 1
    def rotate_list(self, n):       #CLOCKWISE ROTATION
        if n == 0:
            return
        n = n % self.size
        temp = self.head
        cnt = 1
        while cnt < n:
            temp = temp.next
            cnt = cnt + 1
        beg = temp
        while temp.next != None:
            temp = temp.next
        temp.next = self.head
        self.head = beg.next
        beg.next = None
    def reverse_list(self):     #REVERSAL USING ITERATIVE APPROACH
        prv = nxt = None
        cur = self.head
        while cur != None:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        self.head = prv
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
#--GLOBAL VALUES BEGINS--
# C:\Users\ezhuvath\Desktop\CP\CPP\placement.py

class ConstantMod:
    ''' Constant Values for Competitive Programming '''
    # __slots__ = ['_modd', '_maxx', ]  # for fixed number of attributes in __dict__ of the class's instance object
    def __init__(self, n = None, *args, **kwargs):
        self._modd = n
        # self.minn = -(n)
        self._maxx = kwargs['maxvalue'] if 'maxvalue' in kwargs else int(1e9 + 7)
        self._maxx *= -1 if 'negative' in kwargs and kwargs['negative'] == True else 1
    # def __str__(self):    # DEBUG
    #     return f'The value of the modulo is {self._maxx}'
    def value(self, vv=None):
        if vv: self._modd = vv
        try: return self._modd
        except AttributeError: return None

# @contextmanager
# def simple_context_manager(obj):
#     try:
#         obj.maxx = INF
#         obj.minn = -(INF)
#         yield
#     finally:
#         obj.maxx = 10 ** 9 + 7
#         obj.minn = -(10 ** 9 + 7)
# StartTime = time.time()
# print("\nExecution Time: ",time.time()-StartTime)
# input = lambda : sys.stdin.readline()
alp = "abcdefghijklmnopqrstuvwxyz"
modobj = ConstantMod()
# modobj = ConstantMod(negative = True)
modobj = ConstantMod(maxvalue = 10 ** 5 + 9)
INF = 10 ** 15     # Change as per need
#--GLOBAL VALUES ENDS--

#--FUNCTIONS BEGINS--
def solve():
    # YOUR CODE HERE
    # global modobj
    # print(modobj.value(int(1e15)))  #setting modobj._modd from None to given param
    # print("Hello World")
    (n, k) = map(int, input().split(' '))
    ans = 0
    ans = sum(1 for i in range(n) if not int(input()) % k)
    sys.stdout.write("{}".format(ans))
    # sys.stdout.write(str(ans))
    # os.write(1,"%d"%ans)
    # print("YES" if ans else "NO")
    # pass

def main():
    tcs = 1
    # tcs = int(input())
    for tc in range(tcs):
        # with simple_context_manager(modobj):    # temporary environment
        solve()

    # OUTPUT - GOOGLE KICKSTART
    # if solve():
    #     print('Case #{}: {}'.format(tc, "YES"))
    # else:
    #     print('Case #{}: {}'.format(tc, "NO"))
#--FUNCTIONS ENDS--

# # REGION FASTIO
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")
# # END REGION

if __name__ == "__main__":
    main()
#<-----    CODE ENDS    ----


'''

#----INPUT----

# INPUT DATA HERE

#----OUTPUT----

# OUTPUT DATA HERE

'''

''' SHORTER CODE - comment this line to run the below code

# YOUR NOTES HERE

# '''                  

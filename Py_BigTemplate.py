#!/usr/bin/env python

'''

//////////////////////////////////////////////////
//                                              //
//                                              //
//          C++ Competitive Programming         //
//              Template by Cyberkid            //
//                                              //
//            Meet my Codechef Doggie           //
//                                              //
//                                              //
//      |\_/|                                   //
//      | @ @   Woof!                           //
//      |   <>              _                   //
//      |  _/\------____ ((| |))                //
//      |               `--' |                  //
//  ____|_       ___|   |___.'                  //
// /_/_____/____/_______|                       //
//                                              //
//                                              //
//   I am here to guard this code, woof!        //
//   Name : Cyberkid05 | Country : India        //
//                                              //
//                                              //
//////////////////////////////////////////////////

'''

from __future__ import division, print_function
# from statistics import mode
import io, os, sys, math
from io import BytesIO, IOBase

# input = raw_input
# alphabets = "abcdefghijklmnopqrstuvwxyz"

# from collections import defaultdict
# hp = defaultdict(lambda: 0)

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

class Solution:      
    def primeRange(self,m,n):
        if n == 0 or n == 1:
            return []
        primes = [1] * (n + 1) # INITIALIZE ALL THE NUMBERS AS PRIMES FROM 0 TO N
        primes[0] = primes[1] = 0 # ZERO AND ONE ARE NOT PRIMES
        for i in range(4, n + 1, 2):    # ALL EVEN NUMBERS FROM 4 ARE NOT PRIME
            primes[i] = 0
        # print(primes)
        for i in range(3, n + 1, 2):
            if primes[i] == 1:
                for j in range(2 * i, n + 1, i):
                    primes[j] = 0
        return [x for x in range(m, n + 1) if primes[x]]

def solve():
    n, m = map(int, input().split())
    ans = 0
    c = list()
    for i in range(n):
        temp = input()
        c.append(temp)
        if i == 0 or i == n - 1:
            ans = max(ans, temp.count("#"))
    for i in range(n):
        cnt, up, down = 0, 0, 0
        if i != 0 and i != n - 1:
            for j in range(m):
                if c[i][j] == "#":
                    if c[i - 1][j] == ".":
                        up += 1
                    else:
                        ans = max(ans, up)
                        up = 0
                    if c[i + 1][j] == ".":
                        down += 1
                    else:
                        ans = max(ans, down)
                        down = 0
            ans = max(up, max(down, ans))
    for j in range(m):
        cnt, up, down = 0, 0, 0
        for i in range(n):
            if j != 0 and j != m - 1:
                if c[i][j] == "#":
                    if c[i][j - 1] == ".":
                        up += 1
                    else:
                        ans = max(ans, up)
                        up = 0
                    if c[i][j + 1] == ".":
                        down += 1
                    else:
                        ans = max(ans, down)
                        down = 0
            else:
                right, left = 0, 0
                cnt2, cnt3 = 0, 0
                if j == 0:
                    for i in range(n):
                        if c[i][j] == "#":
                            cnt2 += 1
                            if c[i][1] == ".":
                                right += 1
                            else:
                                ans = max(ans, right)
                                right = 0
                        else:
                            ans = max(ans, cnt2)
                            cnt2 = 0
                if j == m - 1:
                    for i in range(n):
                        if c[i][j] == "#":
                            cnt3 += 1
                            if c[i][m - 2] == ".":
                                left += 1
                            else:
                                ans = max(ans, left)
                                left = 0
                        else:
                            ans = max(ans, cnt3)
                            cnt3 = 0
            ans = max(up, max(down, ans))
    print(ans)
    # pass

def main():
    # Contest Code:ABC123 | Problem Code:CODEXYZ
    testcases = 1
    # testcases = int(input())
    for _ in range(testcases):   #solve()
        # 														---> YOUR CODE HERE <---
        print("Hello World")
        # word = input()
        # arr = list(map(int, input().split()))
        # x, y = map(int, input().split())
        # print("YNEOS"[not solve()::2])
        # print(ans)

# REGION FASTIO

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

# END REGION

if __name__ == "__main__":
    main()


'''
#NEW DATA TYPES

class myNode:
    def __init__(self, val):
        self.data = val
        self.next = None

class myLinkedList:
    def __init__(self):
        #----CREATE HEAD PTR----
        self.head = None
    def push_front(self, val):
        #----PUSH AT BEGIN----
        node = myNode(val)
        node.next = self.head
        self.head = node
    def push_back(self, val):
        #----PUSH AT END----
        node = myNode(val)
        if self.head == None:
            self.head = node
            #node.next is already initialized to None
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
            #node.next is already initialized to None
    def pop_back(self):
        #----POP AT END----
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = temp.next.next
    def pop_front(self):
        #----POP AT BEGIN----
        self.head = self.head.next
    def print_list(self):
        #----PRINT LIST----
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

class myStack:
    def __init__(self):
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        self.arr.pop()
    def print_stack(self):
        print(*(self.arr))

class myQueue:
    def __init__(self):
        self.arr = []
    def enqueue(self, val):
        self.arr.append(val)
    def dequeue(self):
        self.arr.pop(0)
    def print_queue(self):
        print(*(self.arr))

class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True
 
    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False
 
    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1
 
    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()
 
        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x
 
    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()
 
        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k
 
    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
 
        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1
 
        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True
 
    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0
 
        _lists = self._lists
        _mins = self._mins
 
        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi
 
        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1
 
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi
 
        return pos, idx
 
    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0
 
        _lists = self._lists
        _mins = self._mins
 
        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi
 
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi
 
        return pos, idx
 
    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
 
        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True
 
    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)
 
    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))
 
    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value
 
    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx
 
    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx
 
    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)
 
    def __len__(self):
        """Return the size of the sorted list."""
        return self._len
 
    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]
 
    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)
 
    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False
 
    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)
 
    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))
 
    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))

'''

'''
#USEFUL FUNCTIONS

# This function finds factorial of large
# numbers and prints them
def factorial( n) :
    ans = [None]*500
    # Initialize result
    ans[0] = 1
    res_size = 1

    # Apply simple factorial formula
    # n! = 1 * 2 * 3 * 4...*n
    x = 2
    while x <= n :
        res_size = multiply(x, ans, res_size)
        x = x + 1
        print(ans)
    
    print ("Factorial of given number is")
    i = res_size-1
    while i >= 0 :
        sys.stdout.write(str(ans[i]))
        sys.stdout.flush()
        i = i - 1
        

# This function multiplies x with the number
# represented by ans[]. res_size is size of ans[]
# or number of digits in the number represented
# by ans[]. This function uses simple school
# mathematics for multiplication. This function
# may value of res_size and returns the new value
# of res_size
def multiply(x, ans,res_size) :
    carry = 0 # Initialize carry

    # One by one multiply n with individual
    # digits of ans[]
    i = 0
    while i < res_size :
        prod = ans[i] *x + carry
        ans[i] = prod % 10; # Store last digit of
                            # 'prod' in ans[]
        # make sure floor division is used
        carry = prod//10; # Put rest in carry
        i = i + 1

    # Put carry in ans and increase result size
    while (carry) :
        ans[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1
        
    return res_size

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def gcdsmall(a, b):
    while(b):
        a, b = b, a % b
    return a

def gcdbig(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    k = 0
    while(((a | b) & 1) == 0):
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ((a & 1) == 0):
        a = a >> 1
    while(b != 0):
        while ((b & 1) == 0):
            b = b >> 1
        if (a > b):
            temp = a
            a = b
            b = temp
        b = (b - a)
    return (a << k)

def lcm(a, b):
    # for small numbers
    if a < 1e5 and b < 1e5:
        return int(a * b / gcdsmall(a, b))
    # for large numbers
    else:
        return int(a * b / gcdbig(a, b))

def findmodpow(a, b, m = 1):    #non recursive [Binary Exponentiation] -> a pow b mod m
    res = 1 
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

def decimal_to_binary(x, n):  #decimal to binary
    return bin(x).replace("0b", "").zfill(n)

def toBaseSum(a, b):
    ps = ""      #    presum
    while a:
        ps += str(a % b)
        a = a // b
    return ps

def checkDivisible(a, b):
    gcd = math.gcd(a, b)
    if b == 1: return 1;
    elif gcd == 1: return 0;
    else: return checkDivisible(a, b // gcd);

def read_all_nums_from_input_stream():      # https://acm.timus.ru/problem.aspx?space=1&num=1001
    nums = list()
    for line in sys.stdin:
        for word in line.split():
            nums.append(float(word))
    return nums

def product_of_list_elements(arr):
    return reduce((lambda x, y: x * y), arr)

'''

'''
#POWERFUL ONE LINERS

# primesieve = reduce((lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))
# eveodd = ["e" if x % 2 == 0 else "o" for x in range(n)]
# facts = reduce(lambda x, y: x * y, range(1, n))
# getsubsets = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

'''

'''
#BOILER PLATES

# input = raw_input
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# from statistics import mode
# from functools import reduce
# from bisect import bisect
# from collections import defaultdict
# hp = defaultdict(lambda: 0)
# import io, os, sys, math, functools
# input = sys.stdin.readline()
# output = sys.stdout.write()
# input = lambda: sys.stdin.readline().strip()
# imap = lambda: map(int,input().split())
# ilist = lambda: list(map(int, input().split()))
# sys.stdout.write(str(ans) + "\n")

'''

'''
#IMPORTANT PYTHON LIBRARIES FOR PROGRAMMING

heapq
collections
bisect
array
itertools
numpy

'''

'''
sample eg. aabbb = "a*b*"
let's assume A times a and B times b

a
aa
A times

b
bb
bbb
Btimes

ab
abb
abbb
aab
aabb
aabbb
A * B times

total = A + B + (A * B) >= N
can be written as
(A * B) + A + B + 1 = (A + 1)(B + 1) >= N + 1
'''




# CALL YOUR MODULES HERE    -------------------->
# import bisect, heapq
# import fractions, math, numpy
# import atexit, io, os, sys, time
#       <----------------------------------------

# DEFINE YOUR FASTIO HERE   -------------------->
# # 0 in os.read() indicated file descriptor for standard input (STDIN)
# # os.fstat(0).st_size will tell Python how many bytes are currently waiting in the STDIN buffer
# # Then os.read() will read those bytes in bulk from STDIN, producing a bytestring
# inputt = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# # A lambda function to get integer input and return it
# input = lambda: inputt()   # integers
# # A lambda function to get string input and return it
# input = lambda: inputt().decode().strip()   # strings
# # ss = sys.stdout
# ss = io.BytesIO()
# _write = ss.write
# ss.write = lambda s: _write(s.encode())
# atexit.register(lambda: os.write(1, ss.getvalue()))
#       <----------------------------------------

# DEFINE YOUR FUNCTIONS HERE    -------------------->
# def readnumbers(zero=0):
#     _ord, nums, num, neg = lambda nbr: nbr, [], zero, False
#     i, s = 0, io.BytesIO(os.read(0,os.fstat(0).st_size)).read()
#     try:
#         while True:
#             if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
#             elif s[i] == b"-"[0]:neg = True
#             elif s[i] != b"\r"[0]:
#                 nums.append(-num if neg else num)
#                 num, neg = zero, False
#             i += 1
#     except IndexError:
#         pass
#     if s and s[-1] >= b"0"[0]: nums.append(-num if neg else num)
#     return nums
# def FastInt(zero=0):
#     _ord, nums, num, neg = lambda nbr: nbr, [], zero, False
#     i, s = 0, io.BytesIO(os.read(0,os.fstat(0).st_size)).read()
#     try:
#         while True:
#             if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
#             elif s[i] == b"-"[0]:neg = True
#             elif s[i] != b"\r"[0]:
#                 nums.append(-num if neg else num)
#                 num, neg = zero, False
#             i += 1
#     except IndexError:
#         pass
#     if s and s[-1] >= b"0"[0]: nums.append(-num if neg else num)
#     return nums
#       <----------------------------------------

# ENTER YOUR CODE HERE  -------------------->
from collections import defaultdict

class Queue:
    queue = []
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def __len__(self):
        return len(self.queue)

class Graph:    # using adjacency lists
    V = 0   # number of vertices
    l = [[], ]  # adjacency list
    def __init__(self, v = 0):  # constructor
        self.V = v  # len(self.l)
        self.l = [list() for _ in range(self.V)]

    def addEdge(self, i, j, undir = True):
        self.l[i].append(j)
        if undir:   # undirected graph has both A -> B and B -> A connections
            self.l[j].append(i)

    def BFS(self, graph, source):   # O(vertices + edges)
        visited = defaultdict(lambda:False)
        # visited = set()
        ans = list()
        q = Queue()
        q.enqueue(source)
        visited[source] = True
        # visited.add(source)
        while len(q) > 0:
            ele = q.dequeue()
            ans.append(ele)
            for x in self.l[ele]:
                if not visited[x]:
                # if x not in visited:
                    q.enqueue(x)
                    visited[x] = True
                    # visited.add(x)
        return ans

    def printAdjList(self):
        for ii in range(self.V):
            x = self.l[ii]
            print(ii, *x)

try:
    import time
    sample = open('outputf.txt', 'w')
    start = time.time()
except Exception as e:
    print("Failed to import module")
    pass

def main():
    g = Graph(7)
    g.addEdge(1, 2)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(0, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    print(*g.BFS(g, 1))
    return

if __name__ == '__main__':
    main()
    try:
        stop = time.time()
        print("Seconds used: ", stop - start)
    except Exception as e:
        pass

#       <----------------------------------------

# ENTER YOUR NOTES HERE -------------------->
'''     # NOTES - uncomment line to run this block

Python Competitive Programming Template for FAST I/O 

# '''
#       <----------------------------------------

# https://www.codechef.com/problems/TALLER
tcs = int(input())
for tc in range(tcs):
    x, y = map(int, input().split())
    print("A" if x > y else "B")

# https://www.codechef.com/problems/PRESENTS
tcs = int(input())
for tc in range(tcs):
    n = int(input())
    print((n // 5) * 4 + (n % 5))

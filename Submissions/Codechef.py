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

# https://www.codechef.com/problems/SEMCOURSES
tcs = int(input())
for tc in range(tcs):
    arr = tuple(map(int, input().split()))
    print(arr[0] * arr[1] * arr[2])

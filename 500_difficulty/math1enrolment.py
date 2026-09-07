t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(max(0, y - x))

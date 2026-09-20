for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(z * min(y, 10*x))
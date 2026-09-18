for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    print(w + z*(x-y))
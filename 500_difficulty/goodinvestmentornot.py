for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if 2*y <= x else 'No')
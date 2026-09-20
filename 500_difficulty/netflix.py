for _ in range(int(input())):
    a, b, c, x = map(int, input().split())
    print('Yes' if max(a+b, a+c, b+c) >= x else 'No')
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('Yes' if 2*max(a, b, c) > a+b+c else 'No')
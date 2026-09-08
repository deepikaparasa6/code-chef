for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if y <= 5*x else 'No')
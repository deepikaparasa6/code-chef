for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d = max(a, b, c)
    if d == a:
        print("Alice")
    elif d == b:
        print("Bob")
    else:
        print("Charlie")

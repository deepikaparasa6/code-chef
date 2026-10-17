t = int(input())

while t > 0:
    n = int(input())
    s = input()
    r = input()
    c = 0

    for j in range(n):
        if s[j] != r[j]:
            c += 1

    if c % 2 == 0:
        print(1)
    else:
        print(0)

    t -= 1
    

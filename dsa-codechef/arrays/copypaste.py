# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()

    # pref[i] = suf[i+1]
    # pref[i] + suf[i+1] = S
    # pref[i] = S/2
    tot = s.count('1')
    target = tot * m
    if target % 2 == 1:
        print(0)
        continue
    if target == 0:
        print(n * m)
        continue

    target //= 2
    cur = 0
    while m > 0:
        if cur + tot < target:
            m -= 1
            cur += tot
            continue
        else:
            break
    ans = 0
    for j in range(min(m, 2)):
        for i in range(n):
            ans += cur == target
            cur += s[i] == '1'
    print(ans)
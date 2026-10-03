import bisect

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    arr = list(map(int, input().split()))
    barr = list(map(int, input().split()))
    xarr = list(map(int, input().split()))

    pairs = list(zip(arr, barr))
    pairs.sort()

    arr = []
    prefix = []

    total = 0

    for a, b in pairs:
        arr.append(a)
        total += b
        prefix.append(total)

    ans = []

    for x in xarr:
        pos = bisect.bisect_right(arr, x)

        if pos == 0:
            ans.append(0)
        else:
            ans.append(prefix[pos - 1])

    print(*ans)
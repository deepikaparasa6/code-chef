# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    print(maxi)
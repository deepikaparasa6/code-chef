# cook your dish here
t = int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    if n*x <= k:
        print("YES")
    else:
        print("NO")
# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    res = x - y 
    if res < 0:
        print(0)
    else:
        print(res)
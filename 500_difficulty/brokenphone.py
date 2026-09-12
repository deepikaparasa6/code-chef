# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if x < y:
        print("REPAIR")
    elif y < x:
        print("NEW PHONE")
    else:
        print("ANY")
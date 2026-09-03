# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if (y-x) > 0:
        print("PROFIT")
    elif y - x < 0:
        print("LOSS")
    else:
        print("NEUTRAL")
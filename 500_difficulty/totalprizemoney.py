# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    ans1 = 10 * x
    ans2 = 90 * y
    print(ans1 + ans2)
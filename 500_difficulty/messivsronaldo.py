# cook your dish here
a,b,x,y = map(int,input().split())
messi = (2 * a) + (1 * b)
ronaldo = (2 * x) + (1 * y)
if messi == ronaldo:
    print("Equal")
elif messi > ronaldo:
    print("Messi")
else:
    print("Ronaldo")
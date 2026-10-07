# cook your dish here
n = int(input())
arr = list(map(int,input().split()))
prefix = [0]*n
prefix[0] = arr[0]
for i in range(1,n):
    prefix[i] = prefix[i-1] + arr[i]
print(*(prefix))

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    cur = 0
    
    for i in range(n):
        # Check if both sent at least one snap on the i-th day
        if a[i] > 0 and b[i] > 0:
            cur += 1
        else:
            cur = 0  # Streak breaks, reset to 0
            
        ans = max(ans, cur) # Keep track of the maximum streak
        
    print(ans)
    t -= 1
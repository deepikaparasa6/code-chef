# Cook your dish here
t = int(input())
for _ in range(t):
    # Read C, X, and Y from the single line of input
    c, x, y = map(int, input().split())
    
    # Calculate the minimum money needed
    ans = (c - x) * y
    
    # Print the answer for the current test case
    print(ans)
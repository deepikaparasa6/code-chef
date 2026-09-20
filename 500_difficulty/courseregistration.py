# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read N, M, and K for each test case
    n, m, k = map(int, input().split())
    
    # Check if the remaining capacity is enough for all N friends
    if n + k <= m:
        print("Yes")
    else:
        print("No")
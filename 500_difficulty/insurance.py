# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X and Y
    x, y = map(int, input().split())
    
    # Print the minimum of X and Y
    print(min(x, y))
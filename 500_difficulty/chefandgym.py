# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X, Y, and Z for each testcase
    x, y, z = map(int, input().split())
    
    # Check conditions based on the budget
    if x + y <= z:
        print(2)
    elif x <= z:
        print(1)
    else:
        print(0)
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read W, X, Y, Z for each test case
    W, X, Y, Z = map(int, input().split())
    
    # Calculate total water after Z hours
    total_water = W + (Y * Z)
    
    # Compare with capacity X
    if total_water > X:
        print("overflow")
    elif total_water == X:
        print("filled")
    else:
        print("unfilled")
# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the battery level
    x = int(input())
    
    # Check if battery level is 15% or less
    if x <= 15:
        print("Yes")
    else:
        print("No")
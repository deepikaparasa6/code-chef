# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X, Y, Z for each test case
    x, y, z = map(int, input().split())
    
    # Calculate the maximum number of mangoes
    max_mangoes = (z - y) // x
    
    # Print the result
    print(max_mangoes)
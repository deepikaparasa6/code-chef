# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the value of X
    X = int(input())
    # Read the results string of 14 games
    s = input()
    
    carlsen_points = 0
    chef_points = 0
    
    # Calculate the points for each player
    for char in s:
        if char == 'C':
            carlsen_points += 2
        elif char == 'N':
            chef_points += 2
        else: # Draw ('D')
            carlsen_points += 1
            chef_points += 1
            
    # Determine the prize money based on the points
    if carlsen_points > chef_points:
        print(60 * X)
    elif carlsen_points == chef_points:
        print(55 * X)
    else:
        print(40 * X)
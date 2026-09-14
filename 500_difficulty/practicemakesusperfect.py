# Read the 4 integers from the input line
P = list(map(int, input().split()))

# Count how many weeks Chef solved at least 10 problems
count = 0
for problems in P:
    if problems >= 10:
        count += 1

# Print the final count
print(count)
# cook your dish here
s = input()
t = input()

found = False
# Loop through all possible starting indices in s
for i in range(len(s) - len(t) + 1):
    # Check if the substring of s matches t
    if s[i : i + len(t)] == t:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
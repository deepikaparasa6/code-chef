t = int(input())

for _ in range(t):
    binary_string = input()
    
    if "010" in binary_string or "101" in binary_string:
        print("Good")
    else:
        print("Bad")

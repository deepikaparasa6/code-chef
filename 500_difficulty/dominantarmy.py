# Function to process each test case
def solve():
    na, nb, nc = map(int, input().split())
    
    # Check if any army is dominant over the other two combined
    if na > nb + nc or nb > na + nc or nc > na + nb:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
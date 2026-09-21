# Function to solve a single test case
def solve():
    X = int(input())
    # Calculate 10% of the bill amount
    discount_percentage = X // 10
    # The flat discount is 100
    flat_discount = 100
    
    # Print the maximum of the two discounts
    print(max(discount_percentage, flat_discount))

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
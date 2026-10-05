# cook your dish here
import sys

def solve():
    # Read all standard input at once (fastest for competitive programming)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        
        # Extract the A array (deadlines)
        A = [int(x) for x in input_data[idx : idx+N]]
        idx += N
        
        # Extract the B array (required cooking times)
        B = [int(x) for x in input_data[idx : idx+N]]
        idx += N
        
        count = 0
        prev_time = 0  # The first student starts at time 0
        
        # Iterate through each student to check their time
        for i in range(N):
            available_time = A[i] - prev_time
            
            # If they have enough time, increment the count
            if available_time >= B[i]:
                count += 1
            
            # The next student's slot starts exactly when this one ends
            prev_time = A[i]
            
        results.append(str(count))
        
    # Print the output for all test cases, separated by a newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
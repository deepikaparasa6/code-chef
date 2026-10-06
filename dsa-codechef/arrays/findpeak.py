def findPeaks(A, n):
    # write your code here 
    hasPeak = False
    
    # Handle the case where the array has only 1 element
    if n == 1:
        print(A[0])
        return

    for i in range(n):
        # Check if the current element is greater than its neighbor(s)
        if (i == 0 or A[i] > A[i - 1]) and (i == n - 1 or A[i] > A[i + 1]):
            print(A[i], end=" ")
            hasPeak = True

    # If no peak element was found, print -1
    if not hasPeak:
        print(-1)
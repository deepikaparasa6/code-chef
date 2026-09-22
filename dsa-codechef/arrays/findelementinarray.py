def solve(N, X, A):
    # write your code here
    for i in A:
        if i == X:
            return "YES"
    return "NO"
import sys

def solve():
    # Read the full standard input including spaces
    line = sys.stdin.readline()
    if not line:
        return
    
    # Remove newline at the end
    if line.endswith('\n'):
        line = line[:-1]
        
    freq = [0] * 26
    for c in line:
        code = ord(c)
        if 97 <= code <= 122:   # 'a'...'z'
            freq[code - 97] += 1
        elif 65 <= code <= 90:  # 'A'...'Z'
            freq[code - 65] += 1
            
    maxFreq = 0
    bestLetter = 'a'
    for i in range(26):
        if freq[i] > maxFreq:
            maxFreq = freq[i]
            bestLetter = chr(97 + i)
            
    print(bestLetter)

if __name__ == '__main__':
    solve()
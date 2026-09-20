# cook your dish here
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        N = int(input_data[idx])
        X = int(input_data[idx+1])
        idx += 2
        
        # Total complete songs listened to is N // X.
        # Song C appears once every 3 songs.
        total_songs = N // X
        ans = total_songs // 3
        
        print(ans)

if __name__ == '__main__':
    solve()
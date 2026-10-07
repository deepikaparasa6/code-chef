def mostFrequent(N: int, A: list) -> list:
    freq = {}
    
    # Count frequencies correctly
    for i in A:
        freq[i] = freq.get(i, 0) + 1
        
    best_elem = -1
    max_freq = -1
    
    # Iterate through items to find the most frequent element,
    # ensuring we pick the smallest element in case of a tie.
    for num, count in freq.items():
        if count > max_freq:
            max_freq = count
            best_elem = num
        elif count == max_freq:
            if num < best_elem:
                best_elem = num
                
    return [best_elem, max_freq]
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Calculate max streak for Om (array a)
    max_cnt1 = 0
    cnt1 = 0
    for i in a:
        if i != 0:
            cnt1 += 1 
            if cnt1 > max_cnt1:
                max_cnt1 = cnt1
        else:
            cnt1 = 0
            
    # Calculate max streak for Addy (array b)
    max_cnt2 = 0
    cnt2 = 0
    for j in b:
        if j != 0:
            cnt2 += 1 
            if cnt2 > max_cnt2:
                max_cnt2 = cnt2
        else:
            cnt2 = 0
            
    # Compare streaks and print the correct output
    if max_cnt1 > max_cnt2:
        print("OM")
    elif max_cnt1 < max_cnt2:
        print("ADDY")
    else:
        print("DRAW")
    t -= 1
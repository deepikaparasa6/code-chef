t = int(input())
for _ in range(t):
    disposable_price, cloth_price = map(int, input().split())
    if (100 * disposable_price) < (10 * cloth_price):
        print("Disposable")
    else:
        print("Cloth")

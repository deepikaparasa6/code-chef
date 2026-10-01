class Solution:
    def check_coupon(self, n, x, y, prices):
        # write your code here
            total = sum(prices)
            applyans = 0
            for i in prices:
                if i > y:
                    applyans = applyans + (i - y)
            # print(applyans)
            if x+applyans < total:
                return "COUPON"
            else:
                return "NO COUPON"
                    

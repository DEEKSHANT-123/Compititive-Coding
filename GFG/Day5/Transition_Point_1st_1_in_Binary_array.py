class Solution:
    def transitionPoint(self, arr, n):
        LB, UB = 0, (n-1)
        if arr[0] == 1:
            return 0
        while LB <= UB:
            mid = (LB + UB) // 2
            if arr[mid] == 1:
                if arr[mid-1] == 0:
                    return mid
                else:
                    UB = mid - 1
            else:    
                LB = mid + 1
        return -1
            
class_instance = Solution() 
result = class_instance.transitionPoint([0,0,0,1,1], 5)
print(result)
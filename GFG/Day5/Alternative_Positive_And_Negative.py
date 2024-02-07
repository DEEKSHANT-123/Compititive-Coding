class Solution:
    def rearrange(self,arr, n):
        arr_pos = []
        arr_neg = []
        for i in range(n):
            if arr[i] >= 0:
                arr_pos.append(arr[i])
            else:
                arr_neg.append(arr[i])
                
        for i in range(n):
            arr[i] = arr_pos[i]
            arr[i+1] = arr_neg[i]
            
        return arr

class_instance = Solution()    
result = class_instance.rearrange(list(map(int, input().split())), int(input()))
print(result)
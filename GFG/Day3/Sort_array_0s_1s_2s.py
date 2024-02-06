class Solution:
    def sort012(self,arr,n):
        c0 = 0
        c1 = 0
        c2 = 0
        for i in range(n):
            if arr[i] == 0:
                c0 += 1
            elif arr[i] == 1:
                c1 += 1
            else:
                c2 += 1
        for i in range(c0):
            arr[i] = 0
        for i in range(c0, c0+c1):
            arr[i] = 1
        for i in range(c0+c1, c0+c1+c2):
            arr[i] = 2
        
        return arr    
        
solution_instance = Solution()
result = solution_instance.sort012([0,1,2,1,0], 5)
print(result)
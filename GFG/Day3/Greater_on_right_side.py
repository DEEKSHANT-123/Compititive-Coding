class Solution:
    	def nextGreatest(self,arr, n):
            max_right = -1 
            for i in range(n-1, -1, -1):
                current_element = arr[i]
                arr[i] = max_right  
                max_right = max(max_right, current_element)

            return arr

instance_solution = Solution()            
result = instance_solution.nextGreatest([16, 17, 4, 3, 5, 2], 6)
print(result)

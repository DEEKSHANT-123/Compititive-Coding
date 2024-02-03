class Solution:
    def findMissing(self, arr, n):
        a = arr[0]
        l = arr[n-1]
        d = (l-a)//(n)
        for i in range(n-1):
            if arr[i+1] - arr[i] != d:
                return (arr[i+1] - d)
instance_solutions = Solution()
result = instance_solutions.findMissing([2,4,6,10,12], 5)
print(result)



######Method2 (Using Binary Search)
class Solution():
    def flindMissing(self, arr, n):
        a = arr[0]
        l = arr[-1]
        d = (l - a)//n
        lb, ub = 0, n-1
        while lb < ub:
            mid = (lb + ub)//2 
            expected_val = a + mid * d

            if expected_val != arr[mid]:
                ub = mid
            else:
                lb = mid + 1
        return a + lb * d
    
instance_solution = Solution()
result = instance_solution.flindMissing([2,4,6,10,12], 5)
print(result)
        
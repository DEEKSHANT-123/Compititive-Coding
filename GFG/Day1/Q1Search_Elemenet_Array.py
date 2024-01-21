class Solution:
    def search(self,arr, N, X):

        for i in range(N):
            if arr[i] == X:
                return i
        else:
            return -1

# Create an instance of the Solution class      
solution_instance = Solution()

# Call the search method on the instance
result = solution_instance.search(list(map(int, input().split())), int(input()), int(input()))
print(result)




#########2nd method use of self#############
class Solution:
    def __init__(self,arr, N, X):
        self.arr = arr
        self.N = N
        self.X = X

    def search(self):
        for i in range(self.N):
            if self.arr[i] == self.X:
                return i
        else:
            return -1

#in case of init creation of instance of class like this.      
solution_instance = Solution(list(map(int, input().split())), int(input()), int(input()))
result = solution_instance.search()
print(result)
        

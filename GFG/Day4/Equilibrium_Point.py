########Method1 T.C. = O(N^2)
class Solution:
    def equilibriumPoint(self,A, N):
        totalSum = sum(A)
        if len(A) == 1:
            return A[0]
        else:
            
            for i in range(1, N):
                sumLeft = sum(A[:i])
                sumRight = sum(A[i+1:])

                if sumLeft == sumRight:
                    return i+1
            return -1
            
solution_instance = Solution()
result = solution_instance.equilibriumPoint(list(map(int, input().split())), int(input()))
print(result)


#######Method2 T.C. = O(N)
class Solution:
    def equilibriumPoint(self, A, N):
        total_sum = sum(A)
        sum_left = 0

        for i in range(N):
            total_sum -= A[i]

            if sum_left == total_sum:
                return i + 1

            sum_left += A[i]

        return -1
            

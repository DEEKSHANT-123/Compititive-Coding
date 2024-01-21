# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# set1 = set(arr1)
# set2 = set(arr2)
# if set1 == set2:
#     print (1)
# else:
#     print (0)



#using function same logic as normal code 

# class Solution:
#     def check(self,A,B,N):
#         A.sort()
#         B.sort()
#         if A == B:
#             return 1
#         else:
#             return 0
        
# instance_solution = Solution()
# result = instance_solution.check([8,9,7,5,3,1] , [5,4,2,5,1,7] , 6)
# print(result)


#2nd method using dictionary
class Solution:
    def check(self,A,B,N):
        freq_A, freq_B = {}, {}
        for i in range(N):
            if A[i] in freq_A:
                freq_A[A[i]] += 1
            else:
                freq_A[A[i]] = 1

        for j in range(N):
            if B[j] in freq_B:
                freq_B[B[j]] += 1
            else:
                freq_B[B[j]] = 1 

        for key, value in freq_A.items():
            if freq_B.get(key) != value:
                    return 0
        return 1
        
    
instance_solution = Solution()
result = instance_solution.check([8,9,7,5,3,1] , [5,4,2,5,1,7] , 6)
print(result)




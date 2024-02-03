# class Solution:
#     def binSort(self, A, N):
#         b = []
#         for i in range(N):
#             if A[i] == 0:
#                 b.append(0)

#         for i in range(N - len(b)):
#             b.append(1)

#         return ' '.join(map(str, b))

# def main():
#     T = int(input())
#     while T > 0:
#         N = int(input())
#         A = list(map(int, input().split()))
#         obj = Solution()
#         result = obj.binSort(A, N)
#         print(result)
#         T -= 1

# if __name__ == "__main__":
#     main()
# 0





class Solution:
    def binSort(self, A, N):
        count = 0
        for i in range(N):
            if A[i] == 0:
                count += 1
        for i in range(count):
            A[i] = 0
        for i in range(count, N):
            A[i] = 1

        return ' '.join(map(str, A))
    

def main():
    T = int(input())
    while T > 0:
        N = int(input())
        A = list(map(int, input().split()))
        obj = Solution()
        result = obj.binSort(A, N)
        print(result)
        T -= 1

if __name__ == "__main__":
    main()
0


n=int(input())
arr=list(map(int, input().split()))
for i in range(n):
    j=n-i-1
    print(arr[j], end=" ")     #i and j define positions of elements of array.

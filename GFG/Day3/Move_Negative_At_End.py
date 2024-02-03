#########Method 1
class Solution:
    def segregateElements(self, arr, n):
        arr2 = [x for x in arr if x < 0]
        arr = [x for x in arr if x >= 0]
        arr.extend(arr2)
        return ' '.join(map(str, arr))
    
class_instance = Solution()
result = class_instance.segregateElements(list(map(int, input().split())), int(input()))
print(result)



##METHOD2
class Solution:
    def segregateElements(self, arr, n):
        newArr = []
        for i in range(n):
            if arr[i] >= 0:
                newArr.append(arr[i])

        for j in range(n):
            if arr[j] < 0:
                newArr.append(arr[j])

        return ' '.join(map(str, newArr))
    
class_instance = Solution()
result = class_instance.segregateElements(list(map(int, input().split())), int(input()))
print(result)



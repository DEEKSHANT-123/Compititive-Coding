class Solution:
    
    def findUnion(self, a, b, n, m):
        arr = []
        i = j = 0
        
        while i < n and j < m:
            if a[i] < b[j]:
                arr.append(a[i])
                i += 1
            elif a[i] > b[j]:
                arr.append(b[j])
                j += 1
            else:
                # Skip duplicates in both arrays
                arr.append(a[i])
                i += 1
                j += 1
                
                # Skip duplicates in array 'a'
                while i < n and a[i] == a[i - 1]:
                    i += 1
                
                # Skip duplicates in array 'b'
                while j < m and b[j] == b[j - 1]:
                    j += 1

        # Add remaining elements from both arrays
        arr.extend(a[i:])
        arr.extend(b[j:])

        return sorted(set(arr))

class_instance = Solution()
result = class_instance.findUnion([1, 35], [6, 9, 13, 15, 22, 22, 29, 46], 2, 8)
print(result)

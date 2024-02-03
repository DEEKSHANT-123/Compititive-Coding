def rotate (arr, n):
    last = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = last
    return arr

result = rotate ([1,2,3,4,5], 5)
print(' '.join(map(str, result)))
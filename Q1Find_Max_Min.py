def getMinMax(a, n):
    min = a[0]
    max = a[0]
    
    for i in range(1, n):
        if a[i] < min:
            min = a[i]
    
        if a[i] > max:
            max = a[i]
    return (min, max)

result = getMinMax (list(map(int, input().split())), int(input()))
print(result)
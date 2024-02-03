n = int(input())
print(max(len(length) for length in bin(n)[2:].split('0')))

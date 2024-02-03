a = str(input())
a.lower()
b = ''.join(reversed(a))
if b==a:
    print("YES")
else:
    print("NO")

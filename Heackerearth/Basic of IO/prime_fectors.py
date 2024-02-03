#Progam for find all prime numbers 

num=int(input())
a=[]
d=2
while num>1:
    if num%d==0:
        a.append(d)
        num=num/d
        continue
    d = d+1  
print(a)

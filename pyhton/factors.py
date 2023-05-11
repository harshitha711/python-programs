def factors(n):
    s=1
    for j in range(2,n+1):
        if(n%j==0):
            s=s+j
    return s
l=list(map(int,input().split()))
res=[]
for i in range(0,len(l)):
    h=factors(l[i])
    if h in l:
        res.append(l[i])
if(len(res)==0):
    print("-1")
else:
    print(sorted(res))
        
        

s=input()
res=0
h=[]
for i in range(0,len(s)):
    for j in range(i,len(s)):
        if j in h:
            h.clear()
            break
        else:
            h.append(j)
            c=len(h)
        res=max(res,c)
            
print(res)
        

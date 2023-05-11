s=input()
l=sorted(set(s.upper()))
print(l)
res=[]
for i in range(len(l)):
    newsstr=""
    for j in s:
        if(l[i]==j.upper()):
            newsstr+=j
    res.append(newsstr)
print(res)
i=0
j=len(res)-1
out=""
while i<=j:
    if i==j:
        out+=res[i]
    else:
        out+=res[i]+res[j]
    i+=1
    j-=1
print(out)

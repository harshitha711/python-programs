def sumofsqaures(n):
    s=0
    l=[]
    while(n>0):
        r=n%10
        s=s+pow(r,2)
        n=n//10
    l.append(s)
    if(s==1):
        print("happy")
    elif(s<10):
        print("unhappy")
    else:
        sumofsqaures(s)
n=int(input())
a=sumofsqaures(n)
        

n=int(input())
x=list(map(int,input().split()))
s =0
y =0
for i in x:
    if i==-1:
        if s>0:
            s -=1
        else:
            y +=1
    else:
        s+=i
print(y)

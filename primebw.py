# sama
n,k=map(int,input("").split())
i=n+1

while(i<k):
    sam=0
    for j in range(2,i):
        if(i%j==0):
            sam=1
            break
        j+=1
    if(sam==0):
        print(i,end=" ")
    i+=1

# sama
num=int(input(""))
p=num
a=0
d=0
while(p!=0):
    k=p
    d=k%10
    a=a+pow(d,3)
    p=p//10    
if(num==a):
    print("yes")
else:
    print("no")

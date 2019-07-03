p=int(input())
q=0
while 2**q < p:
    q=q+1
if 2**q == p:
    print(0)
elif p-2**(q-1)<=2**q-p:
    print(p-2**(q-1))
else:
    print(2**q-p)

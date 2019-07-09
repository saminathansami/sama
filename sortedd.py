a=int(input())
b=list(map(int,input().split()))
b.sort()
for n in b:
    print(n,end=' ')

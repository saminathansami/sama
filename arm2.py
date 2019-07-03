# sama
a,sam=map(int,input().split())
for n in range(a,sam):
  vj=n
  sum=0
  while vj>0:
      digit=vj%10
      sum=sum+digit**3
      vj=vj//10
      if sum==n:
           print(n, end="  ")

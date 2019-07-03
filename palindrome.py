# sama
a=int(input())
n=a
rev=0
while(a>0):
  digit=a%10
  rev=rev*10+digit
  a=a//10
if(n==rev):
  print("yes")
else:
  print("no")

n=int(input())
sam=list(map(int,input().split()))[:n]
a=sam.sort()
middleIndex =int( (len(sam))/2)
print(sam[middleIndex])

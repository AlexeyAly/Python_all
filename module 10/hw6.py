n=int(input())
f=1
sumf=0
for i in range(1,n+1):
  f*=i
  sumf+=f
print(sumf)

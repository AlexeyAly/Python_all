l=int(input())
t=int(input())
s=int(input())
print("C","F", sep="\t")
for i in range(l,t+1,s):
    print(i,int(32+i*1.8), sep="\t")
if i < t:
    print(t,int(32+t*1.8), sep="\t")
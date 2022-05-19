a=1
b=25

lst=[i for i in range(a,b+1)]

print(*[i for i in lst if all([i%int(str(i)[g])==0 if int(str(i)[g])!=0 else False for g in range(len(str(i)))])     ])




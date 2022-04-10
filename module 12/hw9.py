def num_replacer(a):
  a1=""
  for i in range(len(str(a))):
    if i == 0:
      a1+=str(a)[len(str(a))-1]
    elif i == len(str(a))-1:
      a1 += str(a)[0]
    else:
      a1+=str(a)[i]
  return int(a1)


d=int(input())
b=int(input())
if len(str(d))<3 or len(str(b))<4:
  print("Mistake")
else:
  print(num_replacer(d),num_replacer(b),(num_replacer(d)+num_replacer(b)))





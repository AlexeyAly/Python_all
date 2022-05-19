a=input()
print(["NO","YES"][all([any(map(lambda x: x.isdigit(), a)), any(map(lambda x: x.islower(), a)), any(map(lambda x: x.isupper(), a)), len(a)>6])])


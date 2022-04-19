def greet(*args):
   return "Hello, "+" ".join([args[i]+" and " if i <len(args)-1 else args[i]+"!" for i in range(len(args))])

print(greet("Timur", "Petya"))
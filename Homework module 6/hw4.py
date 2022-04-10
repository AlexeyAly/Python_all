qty=0
while True:
   day=int(input("days qty: "))
   if day==0:
       break
   elif day%2==0:
       qty=qty+1
print(qty)

try:
    print(all(map(lambda x:int(x)<256, input().split(".") )))
except:
    print(False)
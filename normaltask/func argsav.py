def mean(*args):
    b=[i for i in args if type(i) is int or type(i) is float]  
    if len(b) == 0:
        return sum(b)
    else:
        return sum(b)/len(b) 
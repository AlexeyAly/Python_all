def matrix_x(n=1,m=None,value=0):
    if m==None:
        m=n

    return [[value for j in range(m)]for i in range(n)]


print(matrix_x(5,8,8))
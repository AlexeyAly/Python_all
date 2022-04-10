def payments(sf,nf,ifu):
    k=(ifu*((1+ifu)**nf))/((1+ifu)**nf-1)
    a=k*sf
    pe=sf*ifu
    return int(a)

s=40000000
n=5
i=0.06
qty=3
n_2=n-qty+2
i_2=0.1

ppp0=payments(s, n, i)

def each_y(qtyy,su, ppp,ifu): #qty - количество лет до изменения условий
    for j in range(1,qtyy+1):
        print("Период:", j)
        print()
        print("Остаток долга на начало периода: ", su)
        print("Выплачено процентов: ", ifu*su)
        print("Выплачено тела кредита: ",ppp-su*ifu)
        print()
        su-=ppp-su*ifu
    print()
    print("Остаток долга: ", su)
    print()
    return su

each_y(qty,s,ppp0,i)
s1=each_y(qty,s, ppp0,i)

ppp1=payments(s1, n_2, i_2)
each_y(n_2,s1,ppp1,i_2)



l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
n_list=[]
def cevir(a):

    for k in a:
        if isinstance(k,list):
            cevir(k)
        else:
            n_list.append(k)

cevir(l)
print(n_list)
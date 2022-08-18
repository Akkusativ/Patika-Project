l=[[1, 2], [3, 4], [5, 6, 7]]
n_l=[]
def rvrs(a):
    a=a[::-1]
    for i in a:
        if isinstance(i,list):
            b=i[::-1]
            n_l.append(b)
        else:
            n_l.append(i)
    return n_l
print(rvrs(l))
# -*- coding -*-
def product(x, *kw):
    sum=x
    if kw == None:
        return sum
    for n in kw:
        sum=sum*n
    return sum

"""
Bir listeyi düzleştiren (flatten) fonksiyon yazin. Elemanlari birden çok katmanli listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""
flatten_list = []
def make_flatten(l):
    for i in l:
        if type(i) == list:
            make_flatten(i)
        else:
            flatten_list.append(i)

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
make_flatten(l)

print(flatten_list)






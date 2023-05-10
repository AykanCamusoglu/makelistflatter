"""
2- Verilen listenin içindeki elemanlari tersine döndüren bir fonksiyon yazin. Eğer listenin içindeki elemanlar da liste içeriyorsa onlarin elemanlarini da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def reverse(l):
    l.reverse()
    for e in l:
        e.reverse()

l = [[1, 2], [3, 4], [5, 6, 7]]

reverse(l)

print(l)
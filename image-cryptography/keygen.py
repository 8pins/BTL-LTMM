import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#tạo khóa

def genkey(x,r,size):
    key = []
    for i in range(size):
        x = r*x*(1-x)
        key.append(int((x* pow(10,16)) % 256))
    print(key)
    return key

def indexgen(x, r, n):
    index = []
    k = []
    for i in range(n):
        x = r*x*(1-x)
        k.append(x)
        index.append(i)

    for i in range(n):
        for j in range(n):
            if (k[i] > k[j]):
                k[i], k[j] = k[j], k[i]
                index[i], index[j] = index[j], index[i]
    print(index)
    return index


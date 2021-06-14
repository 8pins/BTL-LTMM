import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keygen as kg
import numpy as np

def decryption(img, key1, key2):
    deimg1 = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    deimg2 = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# unsubstitution
    z = 0
    for i in range(height):
        for j in range(width):
            deimg1[i, j] = img[i, j] ^ key2[z]
            z += 1

#reshuffling
    for i in range(height):
        k = 0
        for j in range(width):
            deimg2[i,key1[k]] = deimg1[i,j]
            k += 1
    plt.imshow(deimg2)
    plt.show()
    plt.imsave('Ảnh/ảnh giải mã.bmp', deimg2)
    return deimg2

# test

img = mpimg.imread('Ảnh/ảnh mã hóa.bmp')

height = img.shape[0]
width = img.shape[1]
key2 = kg.genkey(0.01,3.95, height*width)
key1 = kg.indexgen(0.01,3.95, width)

decryption(img, key1, key2)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keygen as kg
import numpy as np
import  math

def histogram (img):
    h = np.zeros((256,))
    for i in range(height):
        for j in range(width):
            h[img[i,j]] += 1
    h = h/(height*width)
    entropy = 0
    for i in range(256):
        entropy = entropy + (-h[i]*math.log2(h[i]))
    print(entropy)
    plt.figure()
    plt.bar(range(256), h)
    plt.show()
    return h


img = mpimg.imread('Ảnh/MRI-brain.bmp')
height = img.shape[0]
width = img.shape[1]
enimg2 = np.zeros(shape=[height, width, 3], dtype=np.uint8)
enimg2 = img
histogram(enimg2)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keygen as kg
import numpy as np

def histogram (img):
    h = np.zeros((256,))
    for i in range(height):
        for j in range(width):
            h[img[i,j]] += 1

    plt.figure()
    plt.plot(range(256),h)
    plt.holdon
    plt.bar(range(256), h)
    plt.show()
    return h

img = mpimg.imread('Ảnh/ảnh mã hóa.bmp')

height = img.shape[0]
width = img.shape[1]

histogram(img)
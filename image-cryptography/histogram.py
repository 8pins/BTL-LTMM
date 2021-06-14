import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keygen as kg
import numpy as np

def histogram (img):
    h = np.zeros((256,))
    for i in range(height):
        for j in range(width):
            h[img[i,j]] += 1
    return h



img1 = mpimg.imread('Ảnh/MRI-brain.jpeg')
img2 = mpimg.imread('Ảnh/ảnh mã hóa.bmp')
height = img1.shape[0]
width = img1.shape[1]

h1 = histogram(img1)
h2 = histogram(img2)

plt.subplot(1, 2, 1)
plt.bar(range(256), h1)
plt.subplot(1, 2, 2)
plt.bar(range(256), h2)
plt.show()
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keygen as kg
import numpy as np

def encryption(img, key1, key2):
	enimg1 = np.zeros(shape=[height, width, 3], dtype=np.uint8)
	enimg2 = np.zeros(shape=[height, width, 3], dtype=np.uint8)
	enimg3 = np.zeros(shape=[1, height*width, 3], dtype=np.uint8)

# shuffling
	for i in range(height):
		k = 0
		for j in range(width):
			enimg1[i, j] = img[i, key1[k]]
			k += 1

#substitution
	z = 0
	for i in range(height):
		for j in range(width):
			enimg2[i,j] = enimg1[i,j]^key2[z]
			z += 1

	enimg3[0,2] = enimg2[2,3]
	plt.imshow(enimg2)
	plt.show()
	plt.imsave('Ảnh/ảnh mã hóa.bmp', enimg2)

	return enimg2

img = mpimg.imread('Ảnh/MRI-brain.jpeg')
height = img.shape[0]
width = img.shape[1]
key2 = kg.genkey(0.01,3.95, height*width)
key1 = kg.indexgen(0.01,3.95, width)

encryption(img, key1, key2)






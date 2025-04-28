import numpy as np
import matplotlib.pyplot as plt

""" 2 a)"""
data = np.load('upb.npy')
#print(data.shape) It prints (770, 1894, 3) height * width * depth/channels (3 for RGB)


""" 2 b)""" 
#plt.imshow(data)
#plt.axis('off')
#plt.show()      # shows image of UPB logo

""" 2 c)"""      # shows total number of elements in the array which is 770 * 1894 * 3
print(data.size)
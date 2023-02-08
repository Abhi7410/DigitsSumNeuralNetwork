import numpy as np
import matplotlib.pyplot as plt


train_data1 = np.load('data2.npy')
train_lab1 = np.load('lab2.npy')

# save in csv file 
n,m,k = train_data1.shape


# size of train_data1 is (10000,40,168)
# print(train_data1.shape)
# print(train_data1[23])
# i = 59
# plt.imshow(train_data1[i])
# plt.savefig('img.png')
# print(train_lab1[i])
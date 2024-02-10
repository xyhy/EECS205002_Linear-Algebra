
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import math
import csv

def getData(fname):
    
    # -------- inner function of getData ------------
    def getValue(s):
        if not s:     # an empty string
            return 0
        else:
            return float(s)

    # -------- open data file ---------------------     
    with open(fname, newline='') as csvfile:
        # count the lines in CSV file
        N = sum(1 for line in csvfile)
        
        # prepare the space for data
        X = np.zeros((N-1, 3))

        # reset the file iterator
        csvfile.seek(0)

        # read the data from CSV file
        rows = csv.DictReader(csvfile)
        # the first line contains the titles
        i = 0
        for row in rows:
            X[i,0] = getValue(row['Weight'])
            X[i,1] = getValue(row['Height'])
            X[i,2] = getValue(row['Degree'])
            i = i + 1

    return N-1, X

#------------- main -----------------

N, X = getData('data_collect.csv')
i = 0
print(row['Height'])

# # compute means of W and H and D        
# means = np.mean(X, axis= 0)
# Y = np.zeros((N,3))
# Y[:,0] = [x - means[0] for x in X[:,0]]
# Y[:,1] = [x - means[1] for x in X[:,1]]
# Y[:,2] = [x - means[2] for x in X[:,2]]

# # compute the covariance matrix Sigma
# Sigma = np.dot(Y.T, Y)
# L, U = LA.eig(Sigma)  # L is eigenvalue, U is eigenvector


# # decide which vector is the pc
# pci = 0
# if (L[1] > L[0]):
#     pci = 1
# if(L[2] > L[0]):
#     if(L[2] > L[1]):
#         pci = 2
# var = math.sqrt(L[pci])/3.
# pc = U[:, pci]*var

# # a is the projected coordinate on the line 
# a  = np.dot(Y, U[:, pci])
# print(a)

# # Z is the projected coordinate on the original space
# A = np.reshape(a, (N, 1))
# u = np.reshape(U[:,pci], (1, 2))
# Z = np.dot(A, u) + np.dot(np.ones((N,1)), np.reshape(means, (1,2)))


# # plot the figures 
# plt.figure()
# plt.plot(X[:,0], X[:,1], 'bo') 
# plt.plot(Z[:,0], Z[:,1], 'kx') 
# for i in range(N):
#     plt.plot([])
# plt.plot([means[0]-pc[0], means[0]+pc[0]], [means[1]-pc[1], means[1]+pc[1]], 'r-')
# plt.xlabel("Weight")
# plt.ylabel("Height")
# plt.show()


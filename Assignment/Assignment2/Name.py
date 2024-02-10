
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


def solve_poly_2(x, y):
    ''' define the Vandermonde matrix
        solve the linear system
    '''
    A = [[1, x[0], x[0]**2],
         [1, x[1], x[1]**2],
         [1, x[2], x[2]**2]]
    c = np.linalg.solve(A, y)
    return c

def ploy_curve_2(c, x):
    ''' plot y = c[0] + c[1]x + c[2]x^2
    '''
    y = c[0] + c[1]*x + c[2]*x**2
    return y

# ----------- main ----------------

# define the transformation matrix
#A = [[0.5, 1.732/2],[-1.732/2, 0.5]]
#A = [[1, 1/2],     [0, 1]]
#A = [[1, 0],[0, 1.5]]
A = [[1,0],[0,1]]

# n is the number of line segments in a curve
n = 10
fig = plt.figure() 
ax = fig.add_subplot(111) 

# line 1 and line 2
L1 = np.dot(A, [[20, 80], [80, 80]])
plt.plot(L1[0, :], L1[1, :], "-o")
L2 = np.dot(A, [[50, 50], [100, 50]])
plt.plot(L2[0, :], L2[1, :], "-o")


# the left curve
coef = solve_poly_2([0, 20, 50], [50, 55, 80])
x = np.linspace(0, 50, n)
y =  ploy_curve_2(coef, x)
C1 = np.dot(A, [x, y])
plt.plot(C1[0,:], C1[1,:], "-")
plt.plot(C1[0,[0,n-1]], C1[1,[0,n-1]], "o")

# the right curve
coef = solve_poly_2([50, 80, 100], [80, 55, 50])
x = np.linspace(50, 100, n)
y =  ploy_curve_2(coef, x)
C2 = np.dot(A, [x, y])
plt.plot(C2[0,:], C2[1,:], "-")
plt.plot(C2[0,[0,n-1]], C2[1,[0,n-1]], "o")


# line 3 and line 4
L3 = np.dot(A, [[35, 65], [50, 50]])
plt.plot(L3[0,:], L3[1,:], "-o")
L4 = np.dot(A, [[65, 50], [50, 40]])
plt.plot(L4[0,:], L4[1,:], "-o")

# the buttom curve 
coef = solve_poly_2([40, 20, 0], [50, 55, 50])
y = np.linspace(0, 40, n)
x =  ploy_curve_2(coef, y)
C3 = np.dot(A, [x, y])
plt.plot(C3[0,:], C3[1,:], "-")
plt.plot(C3[0,[0,n-1]], C3[1,[0,n-1]], "o")

# lines
L5 = np.dot(A, [[10, 90], [25, 25]])
plt.plot(L5[0,:], L5[1,:], "-o")
L6 = np.dot(A, [[50, 40], [0, 10]])
plt.plot(L6[0,:], L6[1,:], "-o")

ax.set_aspect(1)
plt.show()


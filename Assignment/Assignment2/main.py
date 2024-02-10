
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
# A = [[-1, 0], [0, -1]]
# A = [[-1, 0], [0, 1]]
# A = [[3, -1], [-1, 3]]
# A = [[1,0], [-0.2,1.2]]
A = [[1,0], [0,1]]

# B = [[2,0], [0,2]]
# B = [[-1,0], [0,-1]]
B = [[1,0], [0,1]]

# n is the number of line segments in a curve
n = 10
fig = plt.figure(facecolor="#A9A9A9") 
ax = fig.add_subplot(111)
# plt.gcf().set_size_inches(5, 5)




# bd1, bd2 is up and down borders
# bd3, bd4 is middle line to apart the scene
# bd1 = np.dot(B, [[0,100], [100,100]])
# plt.plot(bd1[0, :], bd1[1, :], "-", linewidth=1, color="#ffffff")
# bd2 = np.dot(B, [[0,100], [0,0]])
# plt.plot(bd2[0, :], bd2[1, :], "-", linewidth=1, color="#ffffff")
bd3 = np.dot(B, [[50,50], [0,100]])
plt.plot(bd3[0, :], bd3[1, :], "-.", linewidth=1, color="#A9A9A9")
bd4 = np.dot(B, [[0,100], [50,50]])
plt.plot(bd4[0, :], bd4[1, :], "-.", linewidth=1, color="#A9A9A9")

# Stroke 1
S1 = np.dot(A, [[41,43], [71.5,68]])
plt.plot(S1[0, :], S1[1, :], "-", linewidth=4, color="#FA8072")

# Stroke 2
S2 = np.dot(A, [[30, 50.5], [65.5, 67.5]])
plt.plot(S2[0, :], S2[1, :], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 3(left curve)
coef = solve_poly_2([50, 40, 30], [69, 59, 54])
x = np.linspace(48, 32, n)
y =  ploy_curve_2(coef, x)
S3 = np.dot(A, [x, y])
plt.plot(S3[0,:], S3[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 4(right curve)
coef = solve_poly_2([30, 40, 50], [69, 61, 55.5])
x = np.linspace(35, 48, n)
y =  ploy_curve_2(coef, x)
S4 = np.dot(A, [x, y])
plt.plot(S4[0,:], S4[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 5
S5 = np.dot(A, [[30, 50.5], [53, 54]])
plt.plot(S5[0, :], S5[1, :], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 6 (left curve)
coef = solve_poly_2([32.7, 31, 27], [80, 53, 40])
x = np.linspace(31, 28.5, n)
y =  ploy_curve_2(coef, x)
S6 = np.dot(A, [x, y])
plt.plot(S6[0,:], S6[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 7 (left curve)
coef = solve_poly_2([55, 50, 42.5], [49, 46, 32.5])
y = np.linspace(51, 43, n)
x =  ploy_curve_2(coef, y)
S7 = np.dot(A, [x, y])
plt.plot(S7[0,:], S7[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 8 (left curve)
coef = solve_poly_2([48, 43, 35.5], [50, 46, 31.5])
y = np.linspace(45, 37, n)
x =  ploy_curve_2(coef, y)
S8 = np.dot(A, [x, y])
plt.plot(S8[0,:], S8[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 9 (left curve)
coef = solve_poly_2([38, 33, 25.5], [49.5, 41.5, 22.5])
y = np.linspace(38.5, 28.5, n)
x =  ploy_curve_2(coef, y)
S9 = np.dot(A, [x, y])
plt.plot(S9[0,:], S9[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 10
S10 = np.dot(A, [[53, 66], [65.5, 66.5]])
plt.plot(S10[0, :], S10[1, :], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 11
S11 = np.dot(A, [[58.5, 54.5], [65.7, 58.2]])
plt.plot(S11[0, :], S11[1, :], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 12
S12 = np.dot(A, [[53, 53], [58, 40]])
plt.plot(S12[0, :], S12[1, :], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 13
S13 = np.dot(A, [[53.5, 66.5], [58, 58.5]])
plt.plot(S13[0,:], S13[1,:], "-", linewidth=3.5, color="#FFE4E1")
# Stroke 13_2
S13b = np.dot(A, [[66.5, 66.5], [58.2, 39]])
plt.plot(S13b[0,:], S13b[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 14
S14 = np.dot(A, [[54.5, 66.5], [51.5, 52]])
plt.plot(S14[0,:], S14[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 15
S15 = np.dot(A, [[54.5, 66.5], [44.5, 45]])
plt.plot(S15[0,:], S15[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 16
S16 = np.dot(A, [[53.5, 66.5], [39.3, 39.8]])
plt.plot(S16[0,:], S16[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 17 (left curve)
coef = solve_poly_2([45, 39, 25], [62.5, 59.5, 45.5])
y = np.linspace(38.5, 29.5, n)
x =  ploy_curve_2(coef, y)
S17 = np.dot(A, [x, y])
plt.plot(S17[0,:], S17[1,:], "-", linewidth=3.5, color="#FFE4E1")

# Stroke 18
S18 = np.dot(A, [[62.5, 68.5], [35, 29.5]])
plt.plot(S18[0,:], S18[1,:], "-", linewidth=3.5, color="#FFE4E1")

ax.set_aspect(1)
plt.show()
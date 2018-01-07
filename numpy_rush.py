
# coding: utf-8

# In[4]:


#ckrommen:ztisnes


# In[1]:


import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.image as img


# In[2]:


#question 1
def gen_arr(r, c):
    rng = range(r*c)
    count = 0
    mtrx = np.ones(shape=(r, c))
    for i in range(r):
        for x in range(c):
            mtrx[i][x] = rng[count]
            count += 1
    return (mtrx)
                
    
matrx = gen_arr(10,10)


# In[3]:


#question 2
seq = gen_arr(4, 3)
print(seq)


# In[4]:


#question 3
def gen_nsize(n):
    new = np.linspace(0, 1, n)
    if (new.shape[0] == n):
        return (new)
    else:
        error = "error"
        return (error)

arr = gen_nsize(10)
print(arr)


# In[5]:


#question 4
def extract_arr(arr):
    if (arr.shape != (10, 12)):
        return (arr)
    else:
        grid = gen_arr(5, 5)
        x = 0
        for i in range(5):
            y = 7
            for j in range(5):
                grid[i][j] = arr[x][y]
                y += 1
            
            x += 1
        return (grid)

matrx1 = gen_arr(10, 12)
matrx2 = extract_arr(matrx1)
print(matrx1, '\n', matrx2)


# In[19]:


#question 5
def bind_vectors(m, n):
    matrix = gen_nsize(n)
    tmp = gen_nsize(n)
    i = 0
    while i < m:
        tmp = np.vstack((matrix, tmp))
        i += 1
        
    return (tmp)
    

matrx3 = bind_vectors(10, 10)
mpl.imshow(matrx3)


# In[61]:


#question 6

image = img.imread('marvin.png')
matrx4 = bind_vectors(3, 4)
xform = np.dot(image, matrx4)
mpl.imshow(xform)


# In[ ]:


def rgb2gray(rgb):
    fil = [0.299, 0.587, 0.144, 0]
    return np.dot(rgb,fil)


# In[106]:




#xform = np.dot(image, vector)
#xform = np.dot(image, bind_vectors(3, 3).T)
#for i in range(0, 4):
#    image[:,:,i] *= matrx4
#mpl.imshow(image)

#res = mult_matrices(image, matrx3);
#matrx4 = matrx * image
#lum_img = image[:,:,0]
#mpl.imshow(image)
#image = rgb2gray(image)
#mpl.imshow(image,cmap='gray')


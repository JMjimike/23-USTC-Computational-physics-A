
# a=16807
# m=2147483647
# N=10000000

# def azmodm(z):
#     q=int(m/a)
#     r=m%a
#     tmp=a*(z%q)-r*int(z/q)
#     if tmp>=0:
#         return tmp
#     else:
#         return tmp+m
    
# Xn1=[]
# Xn2=[]
# Xn3=[]
# Xn4=[]
# In=[]
# z1=666665
# z2=816812
# z3=11155
# z4=92556

# In.append(z1)
# for i in range(0,N):
#     In.append(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn1.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn1[i]))######              #######生成【0，1】随机数Xn1


# In[0]=z2  
# for i in range(0,N):
#     In[i+1]=(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn2.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn2[i])) ############        ###############生成【0，1】随机数Xn2 

# In[0]=z3
# for i in range(0,N):
#     In[i+1]=(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn3.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn2[i])) ############ 

# In[0]=z4
# for i in range(0,N):
#     In[i+1]=(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn4.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn2[i])) ############ 


import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor
from numba import njit

aaaaaaaaa = 16807
m = 2147483647

def azmodm(z):
    global m, aaaaaaaaa
    q = int(m / aaaaaaaaa)
    r = m % aaaaaaaaa
    tmp = aaaaaaaaa * (z % q) - r * int(z / q)
    if tmp >= 0:
        return tmp
    else:
        return tmp + m

bbbsssbbb = 0
aaasssaaa = 0
cccsssccc = 0

def random01():
    global bbbsssbbb, aaasssaaa, m, cccsssccc
    z1 = 668461  
    z2 = 816815
    z3 = 116560
    z4 = 4813144
    if aaasssaaa == 0 and cccsssccc == 0:
        bbbsssbbb = z1
    if aaasssaaa == m - 10000000 and cccsssccc == 0:
        bbbsssbbb = z2
        aaasssaaa = 1
        cccsssccc = 1
    if aaasssaaa == m - 10000000 and cccsssccc == 1:
        bbbsssbbb = z3
        aaasssaaa = 1
        cccsssccc = 2
    if aaasssaaa == m - 10000000 and cccsssccc == 2:
        bbbsssbbb = z4
        aaasssaaa = 1
        cccsssccc = 3
    bbbsssbbb = azmodm(bbbsssbbb)
    aaasssaaa += 1
    return bbbsssbbb / m

import numpy as np
import matplotlib.pyplot as plt
xn=[]
for i in range(100000):
    xn.append(round((10+5)*np.cos(2*np.pi*random01())))

x=np.array(xn)
plt.figure() #初始化一张图
width = 100 #区间数
n, bins, patches = plt.hist(x,bins = width,density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(Xn)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('x')  
plt.ylabel('f(x)')  
# plt.title(r'频率分布直方图')
# plt.xticks(np.arange(0,1.1,0.25))
plt.show()
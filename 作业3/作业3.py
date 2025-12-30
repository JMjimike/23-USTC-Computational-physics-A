
a=16807
m=2147483647
N=10000

def azmodm(z):
    q=int(m/a)
    r=m%a
    tmp=a*(z%q)-r*int(z/q)
    if tmp>=0:
        return tmp
    else:
        return tmp+m
    
Xn1=[]
Xn2=[]
Xn3=[]
Xn4=[]
In=[]
z1=666665
z2=816812
z3=11155
z4=92556

In.append(z1)
for i in range(0,N):
    In.append(azmodm(In[i]))
    # print("{0}".format(In[i+1]))
    Xn1.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
    # print("{0}".format(Xn1[i]))######              #######生成【0，1】随机数Xn1


In[0]=z2  
for i in range(0,N):
    In[i+1]=(azmodm(In[i]))
    # print("{0}".format(In[i+1]))
    Xn2.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
    # print("{0}".format(Xn2[i])) ############        ###############生成【0，1】随机数Xn2 

In[0]=z3
for i in range(0,N):
    In[i+1]=(azmodm(In[i]))
    # print("{0}".format(In[i+1]))
    Xn3.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
    # print("{0}".format(Xn2[i])) ############ 

In[0]=z4
for i in range(0,N):
    In[i+1]=(azmodm(In[i]))
    # print("{0}".format(In[i+1]))
    Xn4.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
    # print("{0}".format(Xn2[i])) ############ 



import numpy as np
import matplotlib.pyplot as plt

Xn1=np.array(Xn1)
Xn2=np.array(Xn2)
X=[N]
Y=[N]
Z=[N]
Z=np.array(Z)
X=np.array(X)
Y=np.array(Y)
X=pow(1-Xn1**2,1/2)*np.cos(2*np.pi*Xn2)
Y=pow(1-Xn1**2,1/2)*np.sin(2*np.pi*Xn2)
Z=Xn1

Xn3=np.array(Xn3)
Xn4=np.array(Xn4)
X2=[N]
Y2=[N]
Z2=[N]
Z2=np.array(Z2)
X2=np.array(X2)
Y2=np.array(Y2)
X2=pow(1-Xn3**2,1/2)*np.cos(2*np.pi*Xn4)
Y2=pow(1-Xn3**2,1/2)*np.sin(2*np.pi*Xn4)
Z2=Xn3

plt.figure(figsize=(7,7),facecolor='white')#大小和背景颜色
plt.scatter(X,Y,s=1,color='b')
# from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(figsize=(7,7),facecolor='white')
# plt.xlim((-1,1))
# plt.ylim((-1,1))
ax=plt.axes(projection='3d')
# ax.set_zlim(-1,1)
# ax.set_xlim(-1,1)
# ax.set_ylim(-1,1)
ax.set_box_aspect((1,1,1))########调整x，y，z轴比例
ax.scatter3D(X,Y,Z,s=0.1,color='b')
ax.scatter3D(X2,Y2,-Z2,s=0.1,color='b')
plt.show()
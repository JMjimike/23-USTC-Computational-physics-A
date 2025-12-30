import numpy as np
import matplotlib.pyplot as plt

a=16807
m=2147483647
N=20000

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

N0=2900
N1=2994
N2=3013
i=0
j=0
X=[]
Y=[]
Z=[]
In2=[]  
In1=[]
In3=[]
In1.append(z4)
In2.append(z3)
while(not(i==N)):
    In2.append(azmodm(In2[j]))
    Xn2.append(2*(In2[j+1]/(m))-1)     ##生成【-1，1】的均匀采样点:2x-1（x为【0，1】均匀采样点）
    In1.append(azmodm(In1[j]))
    Xn3.append(2*(In1[j+1]/m)-1)

    if(Xn3[j]**2+Xn2[j]**2<=1):
        X.append(2*Xn2[j]*np.power(1-(Xn3[j]**2+Xn2[j]**2),0.5))
        Y.append(2*Xn3[j]*np.power(1-(Xn3[j]**2+Xn2[j]**2),0.5))
        Z.append(1-2*(Xn3[j]**2+Xn2[j]**2))
        j+=1
        i+=1
    else:
        j+=1     
print(j,i)

plt.figure(figsize=(7,7),facecolor='white')#大小和背景颜色
plt.scatter(X,Y,s=1,color='b')

fig1=plt.figure(figsize=(7,7),facecolor='white')
## plt.xlim((-1,1))
## plt.ylim((-1,1))
ax=plt.axes(projection='3d')
## ax.set_zlim(-1,1)
## ax.set_xlim(-1,1)
## ax.set_ylim(-1,1)
ax.set_box_aspect((1,1,1))########调整x，y，z轴比例
ax.scatter3D(X,Y,Z,s=0.1,color='b')
## ax.scatter3D(X2,Y2,-Z2,s=0.1,color='b')

X1=np.array(X)
Y1=np.array(Y)
a=X1[:]
b=Y1[:]
P=1/(2*np.pi)*np.power(1-a**2-b**2,-0.5)
q=np.array([a,b,P])
# print(q)
q=q[:,P<=2]  ###此处这个限制本不应该加，因为概率密度可以大于一，但是图像在边界发散，为了直观只取这些
# print(q)
fig2=plt.figure(figsize=(7,7),facecolor='white')
# plt.xlim((-1,1))
# plt.ylim((-1,1))
ax=plt.axes(projection='3d')
# ax.set_zlim(-1,1)
# ax.set_xlim(-1,1)
# ax.set_ylim(-1,1)
# ax.set_box_aspect((1,1,1))########调整x，y，z轴比例
ax.scatter3D(q[0],q[1],q[2],s=1,color='b')

x=np.array(Y)
plt.figure() #初始化一张图
width = 50 #区间数
n, bins, patches = plt.hist(x,bins = width,range=(-1,1),density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('Y')  
plt.ylabel('f(Y)')  
# plt.title(r'频率分布直方图')
plt.xticks(np.arange(-1,1.1,0.25))

x=np.array(X)
plt.figure() #初始化一张图
width = 50 #区间数
n, bins, patches = plt.hist(x,bins = width,range=(-1,1),density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel('f(X)')  
# plt.title(r'频率分布直方图')
plt.xticks(np.arange(-1,1.1,0.25))


# from scipy.stats import gaussian_kde

# x = X
# y = Y

# # Calculate the point density
# xy = np.vstack([x,y])  #  将两个维度的数据叠加
# z = gaussian_kde(xy)(xy)  # 建立概率密度分布，并计算每个样本点的概率密度

# # Sort the points by density, so that the densest points are plotted last
# idx = z.argsort()
# x=np.array(x)
# y=np.array(y)
# z=np.array(z)
# print(idx)
# x, y, z = x[idx], y[idx], z[idx]
# print(x,y,z)
# fig3=plt.figure(figsize=(7,7),facecolor='white')
# ## plt.xlim((-1,1))
# ## plt.ylim((-1,1))
# ax=plt.axes(projection='3d')
# ## ax.set_zlim(-1,1)
# ## ax.set_xlim(-1,1)
# ## ax.set_ylim(-1,1)
# ax.set_box_aspect((1,1,1))########调整x，y，z轴比例
# ax.scatter3D(x,y,z,s=0.1,color='b')
# ## ax.scatter3D(X2,Y2,-Z2,s=0.1,color='b')

# fig, ax = plt.subplots()
# plt.scatter(x, y,c=z, s=1,cmap='Spectral') # c表示标记的颜色
# plt.colorbar()

plt.show()
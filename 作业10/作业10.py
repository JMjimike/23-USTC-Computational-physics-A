import numpy as np
import matplotlib.pyplot as plt

a=16807
m=2147483647

def azmodm(z):
    q=int(m/a)
    r=m%a
    tmp=a*(z%q)-r*int(z/q)
    if tmp>=0:
        return tmp
    else:
        return tmp+m



# Xn1=[]
# Xn2=[]
# Xn3=[]
# Xn4=[]
# Xn5=[]

# z1=666665
# z2=816812
# z3=11155
# z4=92556
# z5=554116
# In2=[]  
# In1=[]
# In3=[]
# In4=[]
# In5=[]
# In1.append(z1)
# In2.append(z2)
# In3.append(z3)
# In4.append(z4)
# In5.append(z5)

bbbsssbbb=0
aaasssaaa=0
def random01():
    global bbbsssbbb
    global aaasssaaa
    global m 
    z1=666955  
    z2=816815
    if aaasssaaa==0:
        bbbsssbbb=z1
    if aaasssaaa==m-100000000:#避免溢出和随机性下降，及时换下一个
        bbbsssbbb=z2
        aaasssaaa=1
    bbbsssbbb=azmodm(bbbsssbbb)
    aaasssaaa+=1
    return bbbsssbbb/m


N=2000 #系综总数
tao=100  ##特征时间
T=100  ###外力周期
fai=0 ##初相位，可以改变<V_{0}>的大小
tao_=0.2 ##与历史速度的相关比例
bu=8*tao ###总步数
w=2*np.pi/T  ###外力频率
# XY=np.zeros((N,2))##每个粒子最终的位置
xy=np.zeros((N,bu,2))##每个粒子每一步
for i in range(0,N):
    x=0
    y=0
    for j in range(1,bu):
        c1=random01()
        c2=random01()
        if c1>=0.5:
        #     if y<=0: ##尝试构造下一步的速度受上一步速度影响的系统，但失败，因为还是马可夫过程
        #         y+=1+0.1
        #     else:
        #         y+=1-0.1

            y+=1      +y/j*tao_ ###加上了与历史速度有关的碰撞项，此时不是马可夫过程了，tao_为比例，在前面调整，tao_为0时表示碰撞与历史速度无关,
                                ###此处也可以理解为使用数值方法解郎之万方程
        else:
        #     if y>=0:
        #         y-=1+0.1
        #     else:
        #         y-=1-0.1

            y-=1        -y/j*tao_
        if 2*c2>=1+np.sin(w*j+fai): ##此处简单认为力的大小就是概率，因为考虑到一次碰撞中力几乎不变（力的周期远大于碰撞时间）
        #     if x<=0:
        #         x+=1+0.1
        #     else:
        #         x+=1-0.1

            x+=1   +x/j*tao_
        else:
        #     if x>=0:
        #         x-=1+0.1
        #     else:
        #         x-=1-0.1     

            x-=1   -x/j*tao_
        xy[i][j][0]=x
        xy[i][j][1]=y

v=np.zeros((N,bu-tao,2))  ###每步速度，用tao步以后的位置减去当下位置除以tao
for i in range(0,N):
    for j in range(0,bu-tao):
        v[i][j][0]=(xy[i][j+tao][0]-xy[i][j][0])/tao
        v[i][j][1]=(xy[i][j+tao][1]-xy[i][j][1])/tao

vv=np.zeros((bu-tao,2))##系综平均速度
for j in range(0,bu-tao):
    tmp1=0
    tmp2=0
    for i in range(0,N):
        tmp1+=v[i][j][0]
        tmp2+=v[i][j][1]
    vv[j][0]=tmp1/N
    vv[j][1]=tmp2/N

ct=np.zeros((bu-tao,2))##系综平均相关系数
for j in range(0,bu-tao):
    tmp1=0
    tmp2=0
    for i in range(0,N):
        tmp1+=(v[i][j][0]-vv[j][0])*(v[i][0][0]-vv[0][0])##协方差
        tmp2+=(v[i][j][1]-vv[j][1])*(v[i][0][1]-vv[0][1])
    ct[j][0]=tmp1/N
    ct[j][1]=tmp2/N

plt.figure()
plt.plot(range(0,bu-tao),ct[:,0])
plt.plot(range(0,bu-tao),ct[:,1])


from scipy.stats import gaussian_kde

x =xy[:,-1,0]
y = xy[:,-1,1]
# Calculate the point density
xy = np.vstack([x,y])  #  将两个维度的数据叠加
z = gaussian_kde(xy)(xy)  # 建立概率密度分布，并计算每个样本点的概率密度
# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = x[idx], y[idx], z[idx]
fig, ax = plt.subplots()
plt.scatter(x, y,c=z, s=2,cmap='Spectral') # c表示标记的颜色
plt.colorbar()
ax = plt.gca()
ax.set_aspect(1)
plt.show()













            





import numpy as np
import matplotlib.pyplot as plt

a=16807
m=2147483647
N=5000

def azmodm(z):
    q=int(m/a)
    r=m%a
    tmp=a*(z%q)-r*int(z/q)
    if tmp>=0:
        return tmp
    else:
        return tmp+m
    
def PP(x):
    return 2/(np.pi*(1+4*x**4))
def FF(x):
    return (np.exp(-x**2/2))/np.sqrt(2*np.pi)


Xn1=[]
Xn2=[]
Xn3=[]
Xn4=[]
In=[]
z1=666665
z2=816812
z3=11155
z4=92556


i=0
j=0
x=0
c=1   ##初始的c值
p=[]
p=np.array(p)
In2=[]  
In1=[]
In3=[]
In1.append(z1)
In2.append(z2)
In3.append(z3)
while(not(len(p)>=N)):
    In2.append(azmodm(In2[j]))
    Xn2.append(In2[j+1]/(m))     ##生成【-1，1】的均匀采样点:2x-1（x为【0，1】均匀采样点）
    In1.append(azmodm(In1[j]))
    Xn3.append(In1[j+1]/m)
    In3.append(azmodm(In3[j]))
    Xn1.append(In3[j+1]/m)
    x=(np.sqrt(-2*np.log(Xn1[j]))*np.cos(2*np.pi*Xn2[j])) ####抽样高斯分布
    if c<PP(x)/FF(x):
        c=(PP(x)/FF(x))
        p_bool = c*FF(p)*Xn3[j]<=PP(p)
        # print(p_bool)
        p=p[p_bool]   ###重置p
        # print(p)
        print(c)
    if c*FF(x)*Xn3[j]<=PP(x):
        p=list(p)
        p.append(x)
        p=np.array(p)
    j+=1
print(j,len(p),c)
# print(p)

x=np.array(p)
plt.figure() #初始化一张图
width = 50 #区间数
n, bins, patches = plt.hist(x,bins = width,range=(min(p),max(p)),density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel('f(X)')  
# plt.title(r'频率分布直方图')
plt.xticks(np.arange(int(min(p)),int(max(p)),1))
z=np.linspace((min(p)),(max(p)))
z=np.array(z)
zz=FF(z)
zzz=PP(z)
plt.scatter(z,zz,color='black')
plt.scatter(z,zzz,color='orange')
plt.show()
import numpy as np
import math
import matplotlib.pyplot as plt


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
    z1 = 666955  
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

def FF(x,lam):##指数法分布
    return max(lam*np.exp(-lam*x),0)
def Gs(x,xbar):##高斯分布
    return (np.exp(-(x-xbar)**2/2))/np.sqrt(2*np.pi)


a=int(13) ##根据伽马函数的意义，此处设a为正整数
lam=0.5
E=a/lam
F=a/lam**2

def PP(x):  ##权重函数1
    # print(x)
    if x>=0:
       return (lam**a)*(x**(a-1))*np.exp(-lam*x)/math.factorial(a)
    else:
        return 0
def pp(x): ##画图用
       return (lam**a)*(x**(a-1))*np.exp(-lam*x)/math.factorial(a)

# def PP(x):  ##权重函数2
#     # print(x)
#     if x>=0:
#        return (lam**a)*(x**(a-1))*np.exp(-lam*x)/math.factorial(a)*(x-E)**2
#     else:
#         return 0
# def pp(x): ##画图用
#        return (lam**a)*(x**(a-1))*np.exp(-lam*x)/math.factorial(a)*(x-E)**2



i=0
j=0
x=0
c=1   ##初始的c值
N=100000
lam2=1/E

for j in range(3):
    p=[]
    p.append(E) ##设置初始值
    i=0
    while(not(len(p)>=N)):
        if j==0:
            x=np.log(random01())/(-1/p[i])
            c=min(PP(x)*FF(p[i],1/x)/(PP(p[i])*FF(x,1/p[i])),1) ##转移函数1
    
        if j==1:
            x=p[i]+(np.sqrt(-2*np.log(random01()))*np.cos(2*np.pi*random01()))
            c=min(PP(x)*Gs(p[i],x)/(PP(p[i])*Gs(x,p[i])),1) ##转移函数2

        if j==2:
            x=np.log(random01())/(-lam2)
            c=min(PP(x)*FF(p[i],lam2)/(PP(p[i])*FF(x,lam2)),1) ##转移函数3      
        R=random01()
        if c>R:
            p.append(x)
        else:
            p.append(p[i])
        i+=1

    h=sum((np.array(p)-E)**2)/len(p)
    d=sum((np.array(p)))/len(p)
    print((h),F,abs(F-h),d,E,abs(d-E))

    # h=sum((np.array(p)))/len(p)
    # d=sum((np.array(p)))/len(p)
    # print((h),E,abs(F-h))


    x=np.array(p)
    plt.figure() #初始化一张图
    width = 100 #区间数
    n, bins, patches = plt.hist(x,bins = width,range=(min(p),max(p)),density=True) ###density=False:返回频数，Ture返回概率,bins区间数
    # print(x)
    # print(n)
    # print(bins)
    # print(patches) 
    # plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
    plt.xlabel('X')  
    plt.ylabel('f(X)')  
    # plt.title(r'频率分布直方图')
    plt.xticks(np.arange(int(min(p)),int(max(p)),6))
    z=np.linspace((min(p)),(max(p)))
    z=np.array(z)
    zzz=pp(z)/max(pp(z))*max(n) ##此处将PP(x)放大，max为其最值，便于观察
    plt.scatter(z,zzz,color='orange')
plt.show()
import numpy as np
# import math
import matplotlib.pyplot as plt
# from concurrent.futures import ThreadPoolExecutor



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


def H(xy):
    x=xy[0]
    y=xy[1]
    return -(x**2+y**2)+0.5*(x**4+y**4)+1/3*(x-y)**4

def P(H0,H1,bt):
    return min(1,np.exp(-bt*(H1-H0)))


def addone():
    global xy1,xy2,xy3
    a=random01()
    b=random01()
    # dx=np.sqrt(-2*np.log(a))*np.cos(2*np.pi*b)
    # dy=np.sqrt(-2*np.log(a))*np.sin(2*np.pi*b)
    dx=(a-0.5)
    dy=(b-0.5)

    bt=0.2
    x=xy1[-1][0]+dx*d
    y=xy1[-1][1]+dy*d
    H0=H(xy1[-1])
    H1=H([x,y])
    c=random01()
    p=P(H0,H1,bt)
    if p>=c:
        xy1.append([x,y])
    else :
        xy1.append(xy1[-1])
        # print(1)

    bt=1
    x=xy2[-1][0]+dx*d
    y=xy2[-1][1]+dy*d
    H0=H(xy2[-1])
    H1=H([x,y])
    c=random01()
    p=P(H0,H1,bt)
    if p>=c:
        xy2.append([x,y])
    else :
        xy2.append(xy2[-1])
        # print(1)

    bt=5
    x=xy3[-1][0]+dx*d
    y=xy3[-1][1]+dy*d
    H0=H(xy3[-1])
    H1=H([x,y])
    c=random01()
    p=P(H0,H1,bt)
    if p>=c:
        xy3.append([x,y])
    else :
        xy3.append(xy3[-1])
        # print(1)


i=0
j=0
# x=0
# c=1   ##初始的c值
N=10000
d=2



xy1=[]
xy1.append([random01(),random01()])
xy2=[]
xy2.append([random01(),random01()])
xy3=[]
xy3.append([random01(),random01()])
# # lam2=1/E

x61=[]
y61=[]
x62=[]
y62=[]
x63=[]
y63=[]
x6jiay61=[]
x6jiay62=[]
x6jiay63=[]


plt.ion()  # 开启交互模式
figure,axes=plt.subplots(2,3,figsize=(12,7))
ax = axes.flatten() #子图展平,将ax由n*m的Axes组展平成1*nm的Axes组(二维变一维)


for k in range(N):
    addone()
    # n=len(xy)
    # print(n)
    # plt.clf()     # 清空画布
    xy1=np.array(xy1)
    xy2=np.array(xy2)
    xy3=np.array(xy3)
    ax[0].cla()     # 清空画布
    ax[1].cla()
    ax[2].cla()
    ax[3].cla()     # 清空画布
    ax[4].cla()
    ax[5].cla()

    ax[0].set_xlabel("β=0.2")
    ax[1].set_xlabel("β=1")
    ax[2].set_xlabel("β=5")

    # ax[0].set_xlim(min(xy1[:,0])-2,max(xy1[:,0])+2)
    # ax[0].set_ylim(min(xy1[:,1])-2,max(xy1[:,1])+2)
    x, y = xy1[:,0],xy1[:,1]
    ax[0].scatter(x, y,s=1)
    
    # ax[1].set_xlim(min(xy2[:,0])-2,max(xy2[:,0])+2)
    # ax[1].set_ylim(min(xy2[:,1])-2,max(xy2[:,1])+2)
    x, y = xy2[:,0],xy2[:,1]
    ax[1].scatter(x, y,s=1)
        
    # ax[2].set_xlim(min(xy3[:,0])-2,max(xy3[:,0])+2)
    # ax[2].set_ylim(min(xy3[:,1])-2,max(xy3[:,1])+2)
    x, y = xy3[:,0],xy3[:,1]
    ax[2].scatter(x, y,s=1)


    n=k+2    
    x61.append([n,sum((xy1[:,0])**2)/n])
    y61.append([n,sum((xy1[:,1])**2)/n])
    x6jiay61.append([n,x61[k][1]+y61[k][1]])
    x62.append([n,sum((xy2[:,0])**2)/n])
    y62.append([n,sum((xy2[:,1])**2)/n])
    x6jiay62.append([n,x62[k][1]+y62[k][1]])
    x63.append([n,sum((xy3[:,0])**2)/n])
    y63.append([n,sum((xy3[:,1])**2)/n])
    x6jiay63.append([n,x63[k][1]+y63[k][1]])
   
    x61 = np.array(x61)
    y61 = np.array(y61)
    x6jiay61 = np.array(x6jiay61)
    x62 = np.array(x62)
    y62 = np.array(y62)
    x6jiay62 = np.array(x6jiay62)
    x63 = np.array(x63)
    y63 = np.array(y63)
    x6jiay63 = np.array(x6jiay63)

    for i in [3,4,5]:
        ax[i].set_xlabel("number")
        ax[i].set_ylabel("value")
        x, y = [x61[:, 0], x62[:, 0], x63[:, 0]][i-3], [x61[:, 1], x62[:, 1], x63[:, 1]][i-3]
        ax[i].plot(x,y,label="<x^2>")
        x, y = [y61[:, 0], y62[:, 0], y63[:, 0]][i-3], [y61[:, 1], y62[:, 1], y63[:, 1]][i-3]
        ax[i].plot(x,y,label="<y^2>")
        x, y = [x6jiay61[:, 0],x6jiay62[:, 0], x6jiay63[:, 0]][i-3], [x6jiay61[:, 1], x6jiay62[:, 1], x6jiay63[:, 1]][i-3]
        ax[i].plot(x,y,label="<x^2+y^2>")
        ax[i].legend(  fontsize='small')


        
    x61 = x61.tolist()
    y61 = y61.tolist()
    x6jiay61 = x6jiay61.tolist()
    x62 = x62.tolist()
    y62 = y62.tolist()
    x6jiay62 = x6jiay62.tolist()
    x63 = x63.tolist()
    y63 = y63.tolist()
    x6jiay63 = x6jiay63.tolist()
    xy1=list(xy1)
    xy2=list(xy2)
    xy3=list(xy3)
    plt.pause(0.00000000001)

plt.ioff()
print("d={0}".format(d))
print("β=0.2,<x^2>={0},<y^2>={1},<x^2+y^2>={2}".format(x61[N-1][1],y61[N-1][1],x6jiay61[N-1][1]))
print("β=1,<x^2>={0},<y^2>={1},<x^2+y^2>={2}".format(x62[N-1][1],y62[N-1][1],x6jiay62[N-1][1]))
print("β=5,<x^2>={0},<y^2>={1},<x^2+y^2>={2}".format(x63[N-1][1],y63[N-1][1],x6jiay63[N-1][1]))

plt.show()        

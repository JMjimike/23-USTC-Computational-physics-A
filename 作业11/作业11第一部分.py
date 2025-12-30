
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

L = 10000 ##L*L网格
# xi = 3 ##速度参数
# fai0 = 100 ##边界电势
xy = np.zeros((L, L, 2), dtype='float64') ##第三维为（是否占据0/1，历史路劲0/1）
xy[int(L/2), int(L/2)] = (1, 0)
maxL=3
N1=[]
N2=[]
def calcu(indices):
    global maxL ,N1,N2
    # print(1)
    ii,jj= indices
    if (xy[ii][jj][0]==1) :
        tmp=(ii-int(L/2))**2+(jj-int(L/2))**2
        if tmp>=maxL**2:
            maxL=int(np.sqrt(tmp)+2)
            N1.append(maxL) ##更新maxL-n图
            N2.append(n)


def maxxy():
    with ThreadPoolExecutor() as executor:
        indices = [(i, j) for i in range(int(L/2)-(maxL+5),int(L/2)+(maxL+5)) for j in range(int(L/2)-(maxL+5),int(L/2)+(maxL+5))]
        executor.map(calcu, indices)
        



def addone():
    global xy
    maxxy() ##更新最大距离
    xy[:,:,1]=0 ###初始化历史路劲
    iftouch=0
    fai=random01()
    I=round((maxL+5)*np.cos(2*np.pi*fai)+L/2)
    J=round((maxL+5)*np.sin(2*np.pi*fai)+L/2)
    xy[I][J][1]=1
    while not(iftouch):
        # print(maxL)
        a = random01()
        # lastx=I
        # lasty=J
        # print(I,J,ii,jj)
        if a <= 0.25:
            I += 1
        elif 0.25 < a <= 0.5:
            I -= 1
            # print(a)
        elif 0.5 < a <= 0.75:
            J += 1
        elif 0.75 < a <=1:
            J -= 1
            # print(a)
        # print(I,J)    
        if ((I-int(L/2))**2+(J-int(L/2))**2>=(maxL*5)**2) or xy[I][J][0]==1 or  (I <= 1) or (I == L-2) or (J < 1) or (J == L-2):    ## (xy[I-1][J][1]+xy[I+1][J][1]+xy[I][J-1][1]+xy[I][J+1][1]==4)
            # print(I,J)    
            fai=random01()
            # print(2)
            I=round((maxL+5)*np.cos(2*np.pi*fai)+L/2)
            J=round((maxL+5)*np.sin(2*np.pi*fai)+L/2)
            # xy[:,:,1]=0 ###初始化历史路劲
            # xy[I][J][1]=1     
            continue  
        # if xy[I][J][1]==1:
        #     I=lastx
        #     J=lasty
        #     print(3)
        #     continue
        # else:
        #     xy[I][J][1]=1
        #     print(4)
        iftouch=sum(sum(xy[I-1:I+2,J-1:J+2,0])) ##判断有无接触
        if (iftouch):
            xy[I][J][0]=1
            # print(I,J)

        
def change(arr):
    x = []
    y = []
    for i in range(len(arr)):
        x.append(arr[i][0])
        y.append(arr[i][1])
    x = np.array(x)
    y = np.array(y)
    return x, y

def findarr():
    arr=np.array([[int(L/2),int(L/2)]])
    for i in range(int((L/2)-(maxL+10)),int((L/2)+(maxL+5))):
        for j in range(int((L/2)-(maxL+10)),int((L/2)+(maxL+5))):
            if xy[i][j][0]==1:
                arr=np.concatenate((arr,np.array([[i,j]])),axis=0)  ##将已占据的点的坐标加入数组
    return arr

n=0
nn=0
plt.ion()  # 开启交互模式
plt.subplots()
for k in range(30000):
    addone()
    n=sum(sum(xy[:,:,0]==1))
    print(n)
    plt.clf()     # 清空画布
    if(nn!=maxL):
        nn=maxL
        plt.scatter(N2,N1)  
        plt.pause(0.2)
        plt.clf()     # 清空画布
    plt.xlim(int((L/2)-(maxL+20)),int((L/2)+(maxL+20)))
    plt.ylim(int((L/2)-(maxL+20)),int((L/2)+(maxL+20)))
    arr=findarr()
    x, y = change(arr)
    plt.scatter(x, y,s=1)
    plt.pause(0.2)
    # plt.clf()     # 清空画布

plt.ioff()
plt.show()        


# plt.figure()
# plt.scatter(N2,N1)
# plt.show()
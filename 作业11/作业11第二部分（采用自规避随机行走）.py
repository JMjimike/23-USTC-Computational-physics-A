
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

N =50 ##系综数
L = 30 ##L*L网格
xi = 3 ##速度参数
fai0 = 100 ##边界电势
xy = np.zeros((L, L, 3), dtype='float64') ##第三维为（是否占据0/1，电势，历史路劲0/1）
xy[int(L/2)-1:int(L/2)+2, int(L/2)-1:int(L/2)+2] = (1, fai0,0)

# @njit
def walk( indices):
    ii,jj= indices
    if xy[ii][jj][0]==0:
        xy[ii][jj][2]=1
        # print(2)
        tmp = np.zeros(N)
        for k in range(N):
            I, J = ii, jj
            xy[:,:,2]=0 ###初始化历史路劲
            while xy[I][J][0] != 1:
                a = random01()
                lastx=I
                lasty=J
                # print(I,J,ii,jj)
                if a <= 0.25:
                    I += 1
                elif 0.25 < a <= 0.5:
                    I -= 1
                elif 0.5 < a <= 0.75:
                    J += 1
                else:
                    J -= 1
                # print(I,J)
                if (I < 0) or (I == L) or (J < 0) or (J == L):
                    I = -1
                    # print("触碰边界")
                    break
                if xy[I][J][2]==1:
                    I=lastx
                    J=lasty
                    # print("回到上一部")
                elif (1<=I<=L-2) & (1<=J<=L-2) & (xy[I][J][2]!=1) :###未到边界
                    if xy[I-1][J][2]+xy[I+1][J][2]+xy[I][J-1][2]+xy[I][J+1][2]==4: ##死胡同
                        I,J=ii,jj   ###回到原点
                        xy[:,:,2]=0 ###初始化历史路劲
                        # print("回到原点")
                    else:
                        xy[I][J][2]=1
                        # print("成功走一步")
                elif not((1<=I<=L-2) & (1<=J<=L-2)) & (xy[I][J][2]!=1):  ##到了边界
                    xy[I][J][2]=1
                    # print("到了边界")
            if not(I == -1): ##不是触碰边界
                tmp[k] = fai0
        xy[ii][jj][1] = np.mean(tmp)

def updatexy():
    global xy, N, fai0
    with ThreadPoolExecutor() as executor:
        indices = [(i, j) for i in range(L) for j in range(L)]
        executor.map(walk, indices)




def calcu(indicas):
    x,y=indicas
    global xy
    global p
    if xy[x][y][0]==0:
        tmp=0
        if x==0:
            tmp+=xy[x+1][y][0]
            if y==0:
                tmp+=xy[x][y+1][0]+xy[x+1][y+1][0]
            elif y==L-1:
                tmp+=xy[x][y-1][0]+xy[x+1][y-1][0]
            else:
                tmp+=xy[x][y+1][0]+xy[x][y+1][0]+xy[x+1][y+1][0]+xy[x+1][y+1][0]
        elif x==L-1:
            tmp+=xy[x-1][y][0]
            if y==0:
                tmp+=xy[x][y+1][0]+xy[x-1][y+1][0]
            elif y==L-1:
                tmp+=xy[x][y-1][0]+xy[x-1][y-1][0]
            else:
                tmp+=xy[x][y+1][0]+xy[x][y+1][0]+xy[x-1][y+1][0]+xy[x-1][y+1][0]            
        else:
            tmp+=xy[x-1][y][0]+xy[x+1][y][0]
            if y==0:
                tmp+=xy[x][y+1][0]+xy[x+1][y+1][0]+xy[x-1][y+1][0]
            elif y==L-1:
                tmp+=xy[x][y-1][0]+xy[x+1][y-1][0]+xy[x-1][y-1][0]
            else:
                tmp+=xy[x][y+1][0]+xy[x][y-1][0]+xy[x+1][y+1][0]+xy[x+1][y-1][0]+xy[x-1][y+1][0]+xy[x-1][y-1][0]
        if tmp>0:
            p[x][y][0]=1
            p[x][y][1]=tmp
            p[x][y][2]=tmp*(fai0-xy[x][y][1])**xi


p =np.zeros((L, L, 3), dtype='float64')
n=0
def updatep():
    global p,n
    p[:,:]=(0,0,0)
    n=sum(sum(xy[:,:,0]==1))
    with ThreadPoolExecutor() as executor:
        indices = [(i, j) for i in range(L) for j in range(L)]
        executor.map(calcu, indices)
    sumv=sum(sum(p[:,:,2]))
    p[:,:,2]=p[:,:,2]/sumv

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
    for i in range(L):
        for j in range(L):
            if xy[i][j][0]==1:
                arr=np.concatenate((arr,np.array([[i,j]])),axis=0)  
    return arr




plt.ion()  # 开启交互模式
plt.subplots()
# plt.xlim(0, L)
# plt.ylim(0, L)
# x, y = change(findarr())
# ax = plt.scatter(x, y)
for k in range(500):
    updatexy()
    updatep()   
    miu=random01()
    tmp=0
    for i in range(L):
        for j in range(L):
            tmp+=p[i][j][2]
            if miu<=tmp:
                xy[i][j]=(1,fai0,0)
                break
            else:
                continue
        else:
            continue
        break
    print(n)
    plt.clf()     # 清空画布
    plt.xlim(0, L)
    plt.ylim(0, L)
    arr=findarr()
    x, y = change(arr)
    plt.scatter(x, y,s=3)
    plt.pause(0.2)
plt.ioff()
plt.show()        
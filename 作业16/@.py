import numpy as np
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

L = 10000
xy = np.zeros((L, L, 2), dtype='float64')
xy[int(L/2), int(L/2)] = (1, 0)
maxL = 1

def addone():
    global xy, maxL
    xy[:,:,1] = 0  # 初始化历史路劲
    iftouch = 0
    fai = random01()
    I = round((maxL+5)*np.cos(2*np.pi*fai)+L/2)
    J = round((maxL+5)*np.sin(2*np.pi*fai)+L/2)
    xy[I][J][1] = 1
    while not(iftouch):
        a = random01()
        if a <= 0.25:
            I += 1
        elif 0.25 < a <= 0.5:
            I -= 1
        elif 0.5 < a <= 0.75:
            J += 1
        elif 0.75 < a <= 1:
            J -= 1
        if ((I-int(L/2))**2 + (J-int(L/2))**2 >= (maxL*5)**2) or xy[I][J][0] == 1 or \
           (I <= 1) or (I == L-2) or (J < 1) or (J == L-2):
            fai = random01()
            I = round((maxL+5)*np.cos(2*np.pi*fai)+L/2)
            J = round((maxL+5)*np.sin(2*np.pi*fai)+L/2)
            continue
        iftouch = np.sum(xy[I-1:I+2, J-1:J+2, 0])  # 判断有无接触
        if iftouch:
            xy[I][J][0] = 1
            tmp = (I-int(L/2))**2 + (J-int(L/2))**2
            if tmp >= maxL**2:
                maxL = int(np.sqrt(tmp))

def change(arr):
    arr = np.array(arr)
    x, y = arr[:, 0], arr[:, 1]
    return x, y

def findarr():
    arr = np.array([[int(L/2), int(L/2)]])
    for i in range(int((L/2)-(maxL+1)), int((L/2)+(maxL+1))):
        for j in range(int((L/2)-(maxL+1)), int((L/2)+(maxL+1))):
            if xy[i][j][0] == 1:
                arr = np.concatenate((arr, np.array([[i, j]])), axis=0)
    return arr


n = 0
for k in range(300):
    addone()
    n = k + 2


arr = findarr()    
x, y = change(arr)

f1 = plt.figure()
plt.scatter(x, y, s=1)

sandx = []
sandy = []
for r in range(1, maxL):
    k = np.sum((x-int(L/2))**2 + (y-int(L/2))**2 <= r**2)
    sandx.append(np.log(k))
    sandy.append(np.log(r))

f2 = plt.figure()
plt.title("sandbox")
plt.plot(sandx, sandy)

hex = []
hey = []
for r in range(1, maxL):
    max_x, max_y = np.max(x), np.max(y)
    min_x, min_y = np.min(x), np.min(y)
    k = 0
    for i in range(min_x, max_x+r, r):
        for j in range(min_y, max_y+r, r):
            t = np.sum(xy[i:i+r, j:j+r, 0])
            if t >= 1:
                k += 1
    hex.append(np.log(k))
    hey.append(-np.log(r))

f3 = plt.figure()
plt.title("box")
plt.plot(hex, hey)

plt.show()

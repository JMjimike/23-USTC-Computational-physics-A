import numpy as np
import matplotlib.pyplot as plt

aaaaa = 16807
m = 2147483647

def azmodm(z):
    global m, aaaaa
    q = m // aaaaa
    r = m % aaaaa
    tmp = aaaaa * (z % q) - r * (z // q)
    return tmp + m if tmp < 0 else tmp

bbbsssbbb = 0
aaasssaaa = 0
cccsssccc = 0

def random01():
    global bbbsssbbb, aaasssaaa, m, cccsssccc
    z1, z2, z3, z4 = 668461, 816815, 116560, 4813144
    if aaasssaaa == 0 and cccsssccc == 0:
        bbbsssbbb = z1
    if aaasssaaa == m - 10000000 and cccsssccc == 0:
        bbbsssbbb, aaasssaaa, cccsssccc = z2, 1, 1
    if aaasssaaa == m - 10000000 and cccsssccc == 1:
        bbbsssbbb, aaasssaaa, cccsssccc = z3, 1, 2
    if aaasssaaa == m - 10000000 and cccsssccc == 2:
        bbbsssbbb, aaasssaaa, cccsssccc = z4, 1, 3
    bbbsssbbb = azmodm(bbbsssbbb)
    aaasssaaa += 1
    return bbbsssbbb / m

L = 10000
xy = np.zeros((L, L, 2), dtype='float64')
xy[int(L/2), int(L/2)] = (1, 0)
maxL = 1

def addone():
    global xy, maxL
    xy[:, :, 1] = 0
    iftouch = 0
    fai = random01()
    I = np.round((maxL+5)*np.cos(2*np.pi*fai)+L/2).astype(int)
    J = np.round((maxL+5)*np.sin(2*np.pi*fai)+L/2).astype(int)
    xy[I, J, 1] = 1
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
        condition = ((I-int(L/2))**2 + (J-int(L/2))**2 >= (maxL*5)**2) or xy[I, J, 0] == 1 or \
                    (I <= 1) or (I == L-2) or (J < 1) or (J == L-2)
        if condition:
            fai = random01()
            I = np.round((maxL+5)*np.cos(2*np.pi*fai)+L/2).astype(int)
            J = np.round((maxL+5)*np.sin(2*np.pi*fai)+L/2).astype(int)
            continue
        iftouch = np.sum(xy[I-1:I+2, J-1:J+2, 0])
        if iftouch:
            xy[I, J, 0] = 1
            tmp = (I-int(L/2))**2 + (J-int(L/2))**2
            if tmp >= maxL**2:
                maxL = int(np.sqrt(tmp))

def change(arr):
    arr = np.array(arr)
    return arr[:, 0], arr[:, 1]

def findarr():
    indices = np.argwhere(xy[:, :, 0] == 1)
    return np.column_stack((indices[:, 0], indices[:, 1]))

n = 0
for k in range(60):
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

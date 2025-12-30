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



def xnn(x, lam):  # 迭代方程
    return lam * np.sin(np.pi * x)


def lx(x0, lam, lxs):# 计算最终状态
    results = [x0]
    for _ in range(lxs):
        x0 = xnn(x0, lam)
        results.append(x0)
    return np.array(results)


def findx(arr,i):  ##对重复x进行合并
    if len(np.unique(arr)) == 1:
        return 1
    # 对数组进行排序
    sorted_arr = np.sort(arr)
    # 找到相邻元素之间的差值
    differences = np.diff(sorted_arr)
    threshold = 0.1**(i+1)   ##间距按标度律递增
    # print(differences)
    
    # 使用差值小于等于阈值的索引，将相邻元素合并
    combined_indices = np.where(differences > threshold)[0]
    
    # 构建包含不同元素的新数组
    unique_elements = [sorted_arr[0]] + [sorted_arr[i + 1] for i in combined_indices]
    difference = np.diff(unique_elements)
    d=np.around(difference,6)
    d=np.unique(d)
    # print(d)
    return len(unique_elements) , d



mm=[]
lamm=[]
deta=[]
dd=[]
arf=[]
mm.append(1)

def F(lams, lxs, jump):
    global mm
    global lamm
    global deta
    global dd
    global arf
    all_x = []
    all_lam = []
    i=0
    for lam in lams:
        x = 2*random01()# 初始条件
        for _ in range(jump):      # 计算每个参数值下的状态
            x = xnn(x, lam)
        xn = lx(x, lam, lxs)
        xn=np.append(xn,-xn)
        n , d =findx(xn,i)
        # print(d)
        if(n==mm[i]*2 ):
            mm.append(n)
            i+=1
            lamm.append(lam)
            # dd.append()
            # d=np.unique(d)  ##去掉重复值
            # print(d)
            # print(i)
            if(i>=2):
                dd.append(d[1-i])   ##取第（i-1）大的间隔
                # print(d)
                # print(dd)
            if(i>=3):
                deta.append((lamm[i-2]-lamm[i-3])/(lamm[i-1]-lamm[i-2]))
                arf.append(dd[i-3]/dd[i-2])
        all_x.extend(xn)
        # all_x.extend(-xn)
        all_lam.extend([lam] * len(xn))
        # all_lam.extend([lam] * len(xn))

    print("分叉数m:")
    print(mm)
    print("分叉值")
    print(lamm)
    print("分叉间隔比值:")
    print(deta)
    print("分叉间距:")
    print(dd)
    print("间距比:")
    print(arf)

    plt.figure(figsize=(10, 6))
    plt.scatter(all_lam, all_x, s=0.00001, c='black')
    plt.xlabel('λ')
    plt.ylabel('x')
    plt.show()



lams=np.linspace(0.3, 1.2, 7000)  # 参数范围
lxs=400  # 每个参数值的迭代次数
jump =10000  # 跳过的迭代次数
F(lams, lxs, jump)


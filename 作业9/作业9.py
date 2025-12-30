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
    
def P(k,lam):##泊松分布
    return lam**k/np.math.factorial(k)*np.exp(-lam)

def F(x,lam):##指数法分布
    return lam*np.exp(-lam*x)

def P3(Xn):
    if(Xn<=0.3):
        return 1
    if (Xn>0.3 and Xn<=0.4):
        return 2
    if (Xn>0.4):
        return 3


def FF(x):
    return (np.exp(-x**2/2))/np.sqrt(2*np.pi)




Xn1=[]
Xn2=[]
Xn3=[]
Xn4=[]
Xn5=[]

z1=666665
z2=816812
z3=11155
z4=92556
z5=554116
In2=[]  
In1=[]
In3=[]
In4=[]
In5=[]
In1.append(z1)
In2.append(z2)
In3.append(z3)
In4.append(z4)
In5.append(z5)

样本容量=20000
lam=2
p2=np.array(np.zeros((2, 样本容量)))
f=np.array(np.zeros((2, 样本容量)))
p=np.array(np.zeros((2, 样本容量)))
p3=np.array(np.zeros((2, 样本容量)))


# print(1)

i=0
j=0
j1=0
k=0
N=10 #####每个样本变量数
z=0
for i in range(0,样本容量):
    # In2.append(azmodm(In2[j]))
    # Xn2.append(In2[j+1]/m)     ##生成【0，1】的均匀采样整数点:
    # In3.append(azmodm(In3[j]))
    # Xn3.append(In3[j+1]/m)     ##生成【0，1】的均匀采样整数点:
    # In4.append(azmodm(In4[j]))
    # Xn4.append(In4[j+1]/m)     ##生成【0，1】的均匀采样整数点:
    # In5.append(azmodm(In5[j]))
    # Xn5.append(In5[j+1]/m)     ##生成【0，1】的均匀采样整数点:
    # In1.append(azmodm(In1[j]))
    # Xn1.append(In1[j+1]/m)     ##生成【0，1】的均匀采样整数点:
    # print(1)
 
    tmp=0
    lam=4
    k=0
    while(not(k==N)):
        # In1.append(azmodm(In1[j]))
        # Xn1.append(int(In1[j+1]/m*(10+1)))    ##生成0,1,2,,,20的均匀采样整数点:
        In2.append(azmodm(In2[j1]))
        Xn2.append(In2[j1+1]/m*0.9991)    ##生成【0，0.9991】的均匀采样整数点:（查表知lam=4，累计函数k=11时为0.999，k=12可视为1
        # print(Xn2[j1])
        c=0
        b=0
        while(not(c>=Xn2[j1])):#c为0，1，2...的概率的累加值
            c+=P(b,lam)
            # print(P(b,lam))
            # print(Xn2[j1])
            b+=1 
        tmp+=b-1
        k+=1
        j1+=1      
    p[z][i]=(tmp/N-lam)/np.sqrt(lam/N) ###二维数组是因为原本要对N再做大循环的，为避免结果过于复杂，放弃
    
    tmp=0
    lam=1
    k=0
    while(not(k==N)):
        # print(1)
        In1.append(azmodm(In1[j]))
        Xn1.append(In1[j+1]/m)    ##生成【0,1】的均匀采样点:
        # In2.append(azmodm(In2[j1]))
        # Xn2.append(In2[j1+1]/m)     
        tmp+=np.log(Xn1[j])/(-lam)
        k+=1
        j+=1     
        # j1+=1 
    f[z][i]=(tmp/N-1/lam)/np.sqrt(1/(N*lam**2))

    tmp=0
    k=0
    while(not(k==N)):
        # print(1)
        In1.append(azmodm(In1[j]))
        Xn1.append(In1[j+1]/m)    ##生成0,1,2,,,N的均匀采样整数点:
        # In2.append(azmodm(In2[j1]))
        # Xn2.append(In2[j1+1]/m)   
        if (0.7>=Xn1[j]):  ##大于0.7，取0，小于0.7，取1
            tmp+=1
            k+=1
        else:
            tmp+=0
            k+=1    
        j+=1     
    p2[z][i]=(tmp/N-0.7)/np.sqrt(0.7*0.3/N)

    tmp=0
    k=0
    while(not(k==50)):
        # print(1)
        In1.append(azmodm(In1[j]))
        Xn1.append(In1[j+1]/m)    ##生成0,1,2,,,N的均匀采样整数点:
        # In2.append(azmodm(In2[j1]))
        # Xn2.append(In2[j1+1]/m)   
        tmp+=P3(Xn1[j])
        k+=1   
        j+=1  
    p3[z][i]=(tmp/N-0.3*1-0.1*2-0.6*3)/np.sqrt((0.3*(1-2.3)**2+0.1*(2-2.3)**2+0.6*(3-2.3)**2)/N)##中间求了方差和均值



x=np.array(p[z])
fig2=plt.figure() #初始化一张图
width = 100 #区间数   这里区间数要多取一点，使得每个离散值都能单独作为一个直方，避免出现前一个直方包含两个点而后一个直方只包含一个点，使得前一个为后一个的近两倍
n, bins, patches = plt.hist(x,bins = width,density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel("P(X)")  
# plt.title(r'频率分布直方图')
# plt.xticks(np.arange(int(min(x)),int(max(x)),10))
# plt.scatter(range(min(x),max(x)),FF(np.array(range(min(x),max(x)))),color='orange')
plt.scatter(np.arange(min(x),max(x),0.1),FF(np.array(np.arange(min(x),max(x),0.1))),color='orange')

# plt.show()

x=np.array(f[z])
fig3=plt.figure() #初始化一张图
width = 50 #区间数
n, bins, patches = plt.hist(x,bins = width,density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel("F(X)")  
# plt.title(r'频率分布直方图')
# plt.xticks(np.arange(int(min(x)),int(max(x)),10))
# plt.scatter(range(min(x),max(x)),FF(np.array(range(min(x),max(x)))),color='orange')
plt.scatter(np.arange(min(x),max(x),0.1),FF(np.array(np.arange(min(x),max(x),0.1))),color='orange')

# plt.show()

x=np.array(p2[z])
fig4=plt.figure() #初始化一张图
width = 50 #区间数
n, bins, patches = plt.hist(x,bins = width,density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel("P2(X)")    
# plt.title(r'频率分布直方图')
# plt.xticks(np.arange(int(min(x)),int(max(x)),10))
# 
plt.scatter(np.arange(min(x),max(x),0.1),FF(np.array(np.arange(min(x),max(x),0.1))),color='orange')


x=np.array(p3[z])
fig4=plt.figure() #初始化一张图
width = 200 #区间数
n, bins, patches = plt.hist(x,bins = width,density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel("P3(X)")   
# plt.title(r'频率分布直方图')
# plt.xticks(np.arange(int(min(x)),int(max(x)),10))
# 
plt.scatter(np.arange(min(x),max(x),0.1),FF(np.array(np.arange(min(x),max(x),0.1))),color='orange')
plt.show()
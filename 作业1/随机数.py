import matplotlib.pyplot as plt


a=16807
m=2147483647
z=6666
N=10000050
l=4

def azmodm(z):
    q=int(m/a)
    r=m%a
    tmp=a*(z%q)-r*int(z/q)
    if tmp>=0:
        return tmp
    else:
        return tmp+m
    
Xn=[]
In=[]
In.append(z)
for i in range(0,N):
    In.append(azmodm(In[i]))
  #  print("{0}".format(In[i+1]))
    Xn.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
  #  print("{0}".format(Xn[i]))


"""
fig1=plt.figure
plt.ylim((0,1))
plt.xlim((0,1))
for i in range(0,N-l):
    plt.scatter(Xn[i],Xn[i+l],s=0.1)   
plt.draw()
plt.pause(15)
plt.close
"""

import csv
with open("散点.csv","w") as csvfile:
    writer=csv.writer(csvfile)
    
    for i in range(0,100000):#只绘制100000个点
        writer.writerow([Xn[i],Xn[i+l]])


for N in [100,1000,10000,100000,1000000,10000000]  :   
    xnxnplusl=0   #代表<XnXn+l>
    xnxnz2=0   #代表<Xn>^{2}
    xnxn2z=0   #代表<Xn^{2}>
    tmp1=0
    tmp2=0
    for i in range(0,N-l):
        tmp1=tmp1+Xn[i]*Xn[i+l]
    xnxnplusl=tmp1/(N-l-1)
    tmp1=0
    for i in range(0,N):
        tmp1=tmp1+Xn[i]
        tmp2=tmp2+Xn[i]**2
    xnxnz2=(tmp1/N)**2
    xnxn2z=tmp2/N
    cl=(xnxnplusl-xnxnz2)/(xnxn2z-xnxnz2)#计算C_{l}
    print("N={0},c(l)={1},1/(N)^0.5={2}".format(N,cl,1/(N)**0.5))#独立性检验，使用PPT上的方法
  
    for k in [1,2,3]:
        tmp1=0
        for i in range(0,N):
            tmp1=tmp1+Xn[i]**k
        xk=tmp1/N
        print("N={0},k={1},|<x^k-1/(k+1)>|={2},1/(N)^0.5={3}".format(N,k,abs(xk-1/(k+1)),1/(N)**0.5))#随机性检验，对1，2，3阶都检验

input("\n") 
























 
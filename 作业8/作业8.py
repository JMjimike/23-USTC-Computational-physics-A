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

def f(x):
    return np.sqrt(x**2+2*np.sqrt(x))

def F(x,y,z,u,v):
    return 5+x**2-y**2+3*x*y-z**2+u**3-v**3

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


freal=15.439010735567484
Freal=5.67712
for N in [100,1000,10000,100000,1000000,10000000]:
    j=0
    fsum=0
    Fsum=0
    while(not(j==N)):
        In2.append(azmodm(In2[j]))
        Xn2.append(In2[j+1]/m)     ##生成【0，1】的均匀采样整数点:
        In3.append(azmodm(In3[j]))
        Xn3.append(In3[j+1]/m)     ##生成【0，1】的均匀采样整数点:
        In4.append(azmodm(In4[j]))
        Xn4.append(In4[j+1]/m)     ##生成【0，1】的均匀采样整数点:
        In5.append(azmodm(In5[j]))
        Xn5.append(In5[j+1]/m)     ##生成【0，1】的均匀采样整数点:
        In1.append(azmodm(In1[j]))
        Xn1.append(In1[j+1]/m)     ##生成【0，1】的均匀采样整数点:
        fsum+=5*f(Xn1[j]*5)
        Fsum+=0.7*4/7*0.9*2*13/11*F(Xn1[j]*0.7,Xn2[j]*4/7,Xn3[j]*0.9,Xn4[j]*2,Xn5[j]*13/11)
        j+=1
    print("N={0},计算值:{1}, {2}, 误差:{3}, {4}, 1/sqrt(N)={5}".format(N,fsum/N,Fsum/N,freal-fsum/N,Freal-Fsum/N,1/np.sqrt(N)))







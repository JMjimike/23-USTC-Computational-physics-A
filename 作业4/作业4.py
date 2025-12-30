
a=16807
m=2147483647
# N=20000000

def azmodm(z):
    q=int(m/a)
    r=m%a
    tmp=a*(z%q)-r*int(z/q)
    if tmp>=0:
        return tmp
    else:
        return tmp+m
    
Xn1=[]
Xn2=[]
Xn3=[]
Xn4=[]
In=[]
z1=666665
z2=816812
z3=11155
z4=92556


# In.append(z1)
# for i in range(0,N):
#     In.append(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn1.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn1[i]))######              #######生成【0，1】随机数Xn1


# In[0]=z2  
# for i in range(0,N):
#     In[i+1]=(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn2.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn2[i])) ############        ###############生成【0，1】随机数Xn2 

# In[0]=z3
# for i in range(0,N):
#     In[i+1]=(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn3.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn2[i])) ############ 

# In[0]=z4
# for i in range(0,N):
#     In[i+1]=(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn4.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn2[i])) ############ 





# from decimal import Decimal, getcontext
# getcontext().prec = 30  # 设置精度为30位
import numpy as np

num=20000000     ###抽样得到的总点数
n1=int(num*(1/3)) ###【-1，0】的点数
n2=num-n1         ###【0，1】的点数
Xn=[]

# In.append(z1)
# for i in range(0,N):
#     In.append(azmodm(In[i]))
#     # print("{0}".format(In[i+1]))
#     Xn1.append(In[i+1]/m)#Xn中没有计入一开始的z，而是从后面生成的开始计算
#     # print("{0}".format(Xn1[i]))######              #######生成【0，1】随机数Xn1
i=0
j=0
In.append(z1)
while(not(i==n1)):
    In.append(azmodm(In[j]))
    Xn1.append(In[j+1]/(3*m))  #####此处生成【0，1/3】随机列(分母为3m)

    if(Xn1[j]<=1/3 and -np.log2(2-3*Xn1[j])<=0 and -np.log2(2-3*Xn1[j])>=-1):##防止舍入精度带来的意外
        Xn.append(-np.log2(2-3*Xn1[j]))
        if(Xn[i]>=0 or Xn[i]<=-1):
            print(Xn[i])   
        j+=1
        i+=1        
    else:
        j+=1
print(j,i)

  
i=0
j=0
In2=[]  
In1=[]
In1.append(z2)
In2.append(z3)
while(not(i==n2)):
    In2.append(azmodm(In2[j]))
    Xn2.append(In2[j+1]/(m))     
    In1.append(azmodm(In1[j]))
    Xn3.append(In1[j+1]/m)

    if(Xn3[j]*(0.5+np.log(2)/3)<=0.5+(np.log(2)/3)*((0.5)**Xn2[j])):
        Xn.append(Xn2[j])
        # if(Xn[n1+i]<0 or Xn[n1+i]>=1):
        #     print(Xn[i]) 
        j+=1
        i+=1
    else:
        j+=1     
print(j,i)

import matplotlib.pyplot as plt

x=np.array(Xn)
plt.figure() #初始化一张图
width = 100 #区间数
n, bins, patches = plt.hist(x,bins = width,range=(-1,1),density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('x')  
plt.ylabel('f(x)')  
# plt.title(r'频率分布直方图')
plt.xticks(np.arange(-1,1.1,0.25))
plt.show()

        


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


with open('data.TXT') as f:
    line=f.readline()####去掉第一行
    line=f.readline()
    data_array=[]
    while line:
        num=list(map(int,line.split()))
        # print(num)
        data_array.append(num)
        line=f.readline()
        # print(line)

data_array=np.array(data_array)
# print(data_array)



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




n1=5672
n2=37630
N0=2900####2900	1158
N1=2994####2994	2664
N2=3013####3013	9
s1=(N1-N0+1)*n1
s2=(N2-N1)*n2
bi=s1/(s1+s2) ####落在第一区的概率（按面积比例）


#####直接采样法
N=20000
sum=sum(data_array[:,1])
p=[]
i=0
j=0
k=0
while(not(len(p)>=N)):
    In2.append(azmodm(In2[j]))
    Xn2.append(In2[j+1]/m)     ##生成【0，1】的均匀采样整数点:
    sum_tmp=0
    i=0
    while(Xn2[j]*sum>sum_tmp):
        sum_tmp+=data_array[:,1][i]
        i+=1
    p.append(data_array[:,0][i-1])
    j+=1

# print(p)

x=np.array(p)
fig1=plt.figure() #初始化一张图
width = max(p)-min(p) #区间数
n, bins, patches = plt.hist(x,bins = width,range=(min(p),max(p)),density=True) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel('f(X)')  
# plt.title(r'频率分布直方图')
plt.xticks(np.arange(int(min(p)),int(max(p)),10))
plt.scatter(data_array[:,0],data_array[:,1]/sum,color='orange')
# plt.show()


###拒绝采样法
N=sum
p=[]
i=0
j=0
k=0
while(not(len(p)>=N)):
    # In1.append(azmodm(In1[j]))
    # Xn1.append(int(In1[j+1]*(N1+1-N0)/m+N0))   ###生成【2900，2994】的整数点，由于后面要取整，故往后加1，保证2994取到的概率和别的一样
    # In3.append(azmodm(In3[j]))
    # Xn3.append(int(In3[j+1]*(N2+1-N1+1)/m+N1+1))  ###【2995，3013】
    In4.append(azmodm(In4[j]))
    In5.append(azmodm(In5[j]))
    Xn4.append(In4[j+1]/m)
    Xn5.append(In5[j+1]/m)
    if (Xn4[j]<=bi):
        In1.append(azmodm(In1[i]))
        Xn1.append(int(In1[i+1]*(N1+1-N0)/m+N0))   ###生成【2900，2994】的整数点，由于后面要取整，故往后加1，保证2994取到的概率和别的一样
        if(data_array[data_array[:,0]==Xn1[i],1]>=n1*Xn5[j]): ###data_array[:,0]==Xn1[i]生成bool数组，再带入得Xn1【i】对应的原来数据的值
            p.append(Xn1[i])
        i+=1
    else:
        In3.append(azmodm(In3[k]))
        Xn3.append(int(In3[k+1]*(N2-N1)/m+N1+1))  ###【2995，3013】
        if(data_array[data_array[:,0]==Xn3[k],1]>=n2*Xn5[j]): ###data_array[:,0]==Xn1[i]生成bool数组，再带入得Xn1【i】对应的原来数据的值
            p.append(Xn3[k])
        k+=1
    j+=1
print(j,len(p))      

x=np.array(p)
fig2=plt.figure() #初始化一张图
width = int(max(x)-min(x)) #区间数
n, bins, patches = plt.hist(x,bins = width,range=(min(x),max(x)),density=False) ###density=False:返回频数，Ture返回概率,bins区间数
# print(x)
# print(n)
# print(bins)
# print(patches) 
plt.grid(alpha=0.5,linestyle='-.') #网格线，更好看 
plt.xlabel('X')  
plt.ylabel('f(X)')  
# plt.title(r'频率分布直方图')
plt.xticks(np.arange(int(min(x)),int(max(x)),10))
plt.scatter(data_array[:,0],data_array[:,1],color='orange')
plt.show()



# plt.figure()
# plt.scatter(data_array[:,0],data_array[:,1])
# plt.show()
































































































































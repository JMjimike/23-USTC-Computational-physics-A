
a=16807
m=2147483647
z=6666
N=10000050


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
    Xn.append(In[i+1]/m)
  #  print("{0}".format(Xn[i]))


k=0
for i in range(0,N-2):
    if Xn[i]>Xn[i+2]:
        if Xn[i+2]>Xn[i+1]:
            k=k+1
print("16807产生器中比例:{0},独立性较好的理论比例: 1/3!={1}".format(k/(N-2),1/(3*2*1)))

p=2
q=1
# for (p,q) in [(2,1),(1,2),(3,1),(1,3),(10,1),(1,10),(100,1),(1,100),(100,2),(2,100),(100,3),(3,100),(100,50),(100,90),(100,99),(99,100),(40,20),(60,30),(6,3)]:
  # print("p={0},q={1}".format(p,q))
for q in range(1,5):
    for p in range(1,5):#对多个p，q进行检验，时间较长，结果已在附加文件中，可执行文件中设置的值为【1，5】，【1，5】避免时间过长
      if p==q:
          continue
      n0=666   #选定的In中的第几位作为初始
      n1=n0+p-q
      Inplus=[]
      Injian=[]
      Intime=[]
      Inxor=[]
      for i in range(0,max(p,q)):#对pq的大小无限制
          Inplus.append(((In[i+n1]+In[i+n0])%m) )#加
          if In[i+n1]-In[i+n0]>0:               #减
            Injian.append(((abs(In[i+n1]-In[i+n0]))%m) )
          else:
            Injian.append((((m+In[i+n1]-In[i+n0]))%m) ) #相减为负数时加m变为互补的数
          Intime.append(((In[i+n1]*In[i+n0])%m) )#乘
          Inxor.append(((In[i+n1]^In[i+n0])%m) )#异或

      for i in range(max(p,q),N):#之后不再使用In中的随机数，而是使用新生成的数继续生成，从这里也能看出，当原始数列的随机性较好时，令p，q大一些有优势
          Inplus.append((Inplus[i-p]+Inplus[i-q])%m)
          if Injian[i-p]-Injian[i-q]>0:
            Injian.append(((abs(Injian[i-p]-Injian[i-q]))%m) )
          else:
            Injian.append((((m+In[i-p]-In[i-q]))%m) ) 
          Intime.append((Intime[i-p]*Intime[i-q])%m)
          Inxor.append((Inxor[i-p]^Inxor[i-q])%m)



      import numpy as np

      Fnplus=np.array(Inplus)/m #进行广播操作，生成【0，1】的数列
      Fnjian=np.array(Injian)/m
      Fntime=np.array(Intime)/m
      Fnxor=np.array(Inxor)/m
      k=0
      for i in range(0,N-2):
          if Fnplus[i]>Fnplus[i+2]:
              if Fnplus[i+2]>Fnplus[i+1]:
                  k=k+1    
      if abs(k/(N-2)-1/(3*2*1))>0.001:            
        print("斐波拉契产生器(+)中比例:{0},p={1},q={2}".format(k/(N-2),p,q))
      k=0
      for i in range(0,N-2):
          if Fnjian[i]>Fnjian[i+2]:
              if Fnjian[i+2]>Fnjian[i+1]:
                  k=k+1   
      if abs(k/(N-2)-1/(3*2*1))>0.001:                
        print("斐波拉契产生器(-)中比例:{0},p={1},q={2}".format(k/(N-2),p,q))
      k=0
      for i in range(0,N-2):
          if Fntime[i]>Fntime[i+2]:
              if Fntime[i+2]>Fntime[i+1]:
                  k=k+1    
      if abs(k/(N-2)-1/(3*2*1))>0.001:  
        print("斐波拉契产生器(*)中比例:{0},p={1},q={2}".format(k/(N-2),p,q))
      k=0
      for i in range(0,N-2):
          if Fnxor[i]>Fnxor[i+2]:
              if Fnxor[i+2]>Fnxor[i+1]:
                  k=k+1    
      if abs(k/(N-2)-1/(3*2*1))>0.001:  
        print("斐波拉契产生器(^)中比例:{0},p={1},q={2}".format(k/(N-2),p,q))


# for i in range(0,10000):
#     print("{0}".format(Fnjian[i]))

input("\n")




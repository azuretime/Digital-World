ls=[1,2,3,4,5,6,7,8]
a=ls[-4:] #[5, 6, 7, 8]
b=ls[-4:-1] #[5, 6, 7]
c=ls[-1:-4] #[]
d=ls[-1:] #[8]

a=[[1,2],[2,44,3]]
b=a
b.append(100)
print a[2]==100 #True


a=[[1,2],[2,44,3]]
b=a[:]
b.append(100)
print a[2]==100 #false

#shallow copy
import copy
a=[1,2]
b=[10,a] 
c=copy.copy(b) #only copy address of a
c=b[:]         #only copy address of a
a[1]=100
print c[1][1]==100 #True

#deep copy
import copy
a=[1,2]
b=[10,a] 
c=copy.deepcopy(b) #copy content of a
a[1]=100
print c[1][1]==2 #True

l=[1,2,3] 
l[1:1]=[4] #zero width, insertion happens
print l # [1, 4, 2, 3]

x=[1,2,3] 
y1=[x,0] 
y2=y1[:] 
y2[0][0]=0 
y2[1]=1 
print y1[0][0] # 0
print y1[1] # 0 
print y2[0][0] # 0
print y2[1] # 1

x=[1,2,3] 
def f(l): 
    l[0]='a' 
f(x)
print x[0] # 'a'


('E',[1, 0],'E',[1, 2])
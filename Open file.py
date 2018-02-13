'''store the entire file in a list'''
f=open('gauss1.txt','r')

s1=f.readlines()   
print s1
    
f.close()

'''print each line of the file separately'''
f=open('gauss1.txt','r')

for line in f:
    print line

f.close()    

#or

f=open('gauss1.txt','r')

s2=f.readline()
while s2:
    print s2
    s2 = f.readline()
    
f.close()


'''store entire file in a single string'''
f=open('gauss1.txt','r')

s3=f.read()
print s3
    
f.close()
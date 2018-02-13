import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throw_dice(n, nExp):
    ls=[] 
    q=n
    w=nExp
    while w>0:
        while q>0:
            a=random.randint(1,6)
            ls.append(a)
            q-=1
        w-=1        
        
    not6 = 0.0
    for num in ls:        
        if num!=6:
            not6 += 1
            
    n6=n*nExp-not6
            
    return round(float(n6/(n*nExp)),2)
          
print throw_dice(1, 100000)
            
import random
from sys import argv

m = int(argv[1]) # performing the experiment with m dice n times
n = int(argv[2]) # Throwing m dice n times
s = 0            # Counts the number of times m dies shows at least one 6

print '%.g dice are thrown %.g times' % (m, n)

for i in xrange(n):
    list = []    # used to clear the list for new die count
    for q in xrange(m):
        r = random.randint(1,6)#Picks a random integer on interval [1,6]
        list.append(r)         #appends integer value
        if len(list) == m:     #when list is full, that is when m dice has been thrown
            for i in xrange(len(list)):
                #print list
                if list[i] == 6: #if the list of elements has a six add to the counter
                    s += 1
                    break #I want the loop to exit when it finds an element = 6

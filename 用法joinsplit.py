print'-------------------------------------------------------'
#spacing/gap 
print 'asd' , 'aswe'  #asd aswe
print 'asd' + '\n' + 'aswe' #转行
print'-------------------------------------------------------'
#spliting
string = '3 2 4'
(n, l, e) = string.split()            #minimally one spacing will work
print n,l,e
lists = ['2 3 4','3','4']             #minimally one spacing will work
(a, b, c) = lists[0].split()
print a,b,c
print'-------------------------------------------------------'
#joining
strings = ('me' , 'no' , 'douche')
lists = ['u', 'are', 'douche']
print ''.join(strings)  #menodouche
print ' '.join(strings) #me no douche
print ''.join(lists)    #uaredouche
print ' '.join(lists)   #u are douche
print'-------------------------------------------------------'
#EXERCISE Q5 STANDARD ANSWER
#C = open ('xy.dat','r')               #for testing, read the file at the start
class Coordinate:
    x=0
    y=0
def get_maxmin_mag(f):
    mag_min = None
    mag_max = None
    pmin = None
    pmax = None
    for line in f:
        coords = line.split()
        p = Coordinate()
        p.x = float(coords[0])
        p.y = float(coords[1])
        mag = (p.x*p.x+p.y*p.y)**0.5
        if (pmin is None) or (mag < mag_min):
            mag_min = mag
            pmin = p
        if (pmax is None) or mag > mag_max:
            mag_max = mag
            pmax = p

    return pmax,pmin

#pmax,pmin = get_maxmin_mag(C)         #for testing
#print pmax.x, pmax.y                  #for testing
#print pmin.x, pmin.y                  #for testing
'-----------------------------------------------------------------------------'
#HW Q4 STANDARD ANSWER
#C = open ('constants.txt','r')        #for testing, read the file at the start
def get_fundamental_constants(f):
    constants={}
    alist = f.readlines()
    length = len(alist)
    i = 2
    while i < length:
        (key, val, dim) = alist[i].split()
        constants[key] = float(val)
        i += 1
    return constants
#print get_fundamental_constants(C)    #for testing
'-----------------------------------------------------------------------------'
#HW Q5 STANDARD ANSWER
#C = open ('scores.txt','r')
def process_scores(f):                #for testing, read the file at the start
    total=0
    count=0
    data=f.read()
    scores=data.split()
    for s in scores:
        total+=float(s.strip())
        count+=1
    average=total/count
    return total,average
#print process_scores(C)               #for testing

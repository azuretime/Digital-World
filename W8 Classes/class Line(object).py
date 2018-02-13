class Line(object):
    
    def __init__(self,c0,c1):        
        self.c0=c0
        self.c1=c1
    
    def __call__(self,x):
        y= self.c0+self.c1*x
        return float(y)
        
    def table(self,L,R,n):
        stepsize=float(R-L)/(n-1)
        s=''
        if n==0:
            return 'Error in printing table'
        else: 
            if stepsize==0:
                x = L
                y = self(x)
                return "%10.2f%10.2f\n" %(x,y)
                
            for i in range(n):
                x = L + i*stepsize
                y =self(x)
                s+="%10.2f%10.2f\n" %(x,y)           
            return s
  #10empty spaces,2dp,float
  #each value formatted to 2 decimal places in
  #a ﬁeld of width 10
            
            
line = Line(-1,2)    
print line(2)   
print line.table(-1,5,10)  


##Anw
class Line:
    def __init__(self, c0, c1):
        self._c0 = float(c0)
        self._c1 = float(c1)

    def __call__(self,x):
        return self._c0 + self._c1 * x

    def table(self,start,end,npoints):
        x = start

        if end < start:
            return 'Error in printing table'
        if npoints < 1:
            return 'Error in printing table'
        if start == end:
            df = 1
        else:
            df = (float(end)-float(start))/(npoints-1)
        outp = ''
        count = 0
        while x <= end:
            y=self(x)
            nl="\n"
            outp+="%10.2f%10.2f" % (x, y)
            outp+=nl
            count += 1
            x= start + count*df
        return outp


class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    
    def __call__(self, x):
        return float(self.c0 + self.c1*x)
    
    def make_table_line(self, x):
        return "{:10.2f}{:10.2f}\n".format(x, self(x))
    
    def table(self, L, R, n):
        if L==R:
            return self.make_table_line(L)
        if L>R:
            return "Error in printing table"
        if n==1:
            return self.make_table_line(L)
        if n==0:
            return "Error in printing table"
        
        table = []
        step = float(R-L)/(n-1)
        for i in range(n):
            x = L + step*i
            table.append(self.make_table_line(x))
        
        return "".join(table)
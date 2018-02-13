# Generally, problems can be broken down to simpler or more direct problems.
# Always take note of intent of code rather than just the code itself.
class Polynomial(object):
    def __init__(self,coeff): # Can you see any issues with this __init__?
        self.coeff=coeff
    
    # The problem to solve in this method is how to
    # take care of polynomials with different length.
    # In this case, we add based whether the element exists in either polynomial.
    def __add__(self,p2):
        newcoeff=[]
        lennewp=max(len(self.coeff),len(p2.coeff))
        for i in range(lennewp):
            if i < len(self.coeff) and i < len(p2.coeff):    # element exists in both
                newcoeff.append(self.coeff[i]+p2.coeff[i])
            elif i < len(self.coeff):                        # element exists only in self
                newcoeff.append(self.coeff[i])
            else:                                            # element exists only in other
                newcoeff.append(p2.coeff[i])
        return Polynomial(newcoeff)
    
    # Just like in __add__, the problem to solve in this method is how to
    # take care of polynomials with different length.
    def __sub__(self,p2):
        newcoeff=[]
        lennewp=max(len(self.coeff),len(p2.coeff))
        for i in range(lennewp):
            if i < len(self.coeff) and i < len(p2.coeff):    # element exists in both
                newcoeff.append(self.coeff[i]-p2.coeff[i])
            elif i < len(self.coeff):                        # element exists only in self
                newcoeff.append(self.coeff[i])
            else:                                            # element exists only in other
                newcoeff.append(-p2.coeff[i])
        return Polynomial(newcoeff)
    
    # The problem to solve in this method is
    # how to accumulate the results for each term. (This should be simple!)
    def __call__(self,x):
        retval=0
        for i in range(len(self.coeff)):
            retval+=self.coeff[i]*x**i
        return retval
    
    # The problems to solve in this method are
    # 1. Accumulating the results of each term
    # 2. Ensuring that the resulting polynomial is the correct length (no extra 0 terms)
    def __mul__(self,p2):
        lenfp=len(self.coeff)*len(p2.coeff) # Result polynomial must be smaller than this size.
        d={}                                # use a dict to accumulate results for each term.
        for i in range(lenfp):
            d[i]=0
        for i in range(len(self.coeff)):
            for j in range(len(p2.coeff)):
                coeff=self.coeff[i]*p2.coeff[j]
                d[i+j]+=coeff
        maxid=0
        for i in range(lenfp):              # Get the largest term in the result polynomial
            if d[i]!=0:
                maxid=i
        fl = []

        for i in range(maxid+1):            # Make the coeff list the correct size.
            fl.append(d[i])

        return Polynomial(fl)
    
    # The problem to solve in this method is
    # how to make sure you get a new polynomial (this is actually really simple!)
    def derivative(self):
        newPoly=Polynomial(self.coeff)
        newPoly.differentiate()
        return newPoly
    
    # The problem to solve in this method is
    # how to make sure that derivatives are put in the correct term.
    def differentiate(self):
        newcoeff = []
        for i in range(1,len(self.coeff)):
            newcoeff.append(i*self.coeff[i])
        self.coeff = newcoeff


# Here's a improved version of the first answer. With different ways of solving things.
class Polynomial(object):
    
     # Should make a copy so that when coeff changes outside the polynomial,
     # the polynomial itself doesn't change.
     # (Tutor doesn't test for this, but it's usually good practice to do so.)
    def __init__(self, coeff):
        self.coeff=coeff[:]
    
    # The problem to solve in this method is how to
    # take care of polynomials with different length.
    # In this case, we always add the shorter polynomial to the longer one,
    # so we will never see an IndexError.
    def __add__(self,p2):
        if len(self.coeff) > len(p2.coeff):
            longcoeff = self.coeff
            shortcoeff = p2.coeff
        else:
            longcoeff = p2.coeff
            shortcoeff = self.coeff
        sum_coeff = longcoeff[:]    # Make sure you copy the coefficients so
                                    # you don't modify the original polynomial!
        for i in range(len(shortcoeff)):
            sum_coeff[i] += shortcoeff[i] # Calculation done here
        return Polynomial(sum_coeff)
    
    # Just like in __add__, the problem to solve in this method is how to
    # take care of polynomials with different length.
    # There's multiple ways to solve this problem. Another way is to extend the
    # lists to the same length by filling in extra 0s.
    # Note that either way works. Choose the most readable and understandable to you.
    def __sub__(self,p2):
        maxlen = max(len(self.coeff), len(p2.coeff))
        extendself = self.coeff + [0]*(maxlen - len(self.coeff))
        extendother = p2.coeff + [0]*(maxlen - len(p2.coeff))
        sum_coeff = []
        for i in range(maxlen):
            sum_coeff.append(extendself[i] - extendother[i]) # Calculation done here
        return Polynomial(sum_coeff)
    
    # Using the index and the value itself is a very common pattern
    # e.g. self.coeff[i] and i.
    # The enumerate() function can do this for you (Check python docs.)
    def __call__(self,x):
        retval=0
        for i, c in enumerate(self.coeff):
            retval += c*(x**i)
        return retval
    
    # The problems to solve in this method are
    # 1. Accumulating the results of each term
    # 2. Ensuring that the resulting polynomial is the correct length (no extra 0 terms)
    def __mul__(self,p2):
        # Problem 2 can be easily solved with some maths!
        # Notice that the polynomial size should be
        # largest power of self * largest power of p2 + 1
        # (len(self.coeff)-1) + (len(p2.coeff)-1) + 1
        # which is simply
        # len(self.coeff) + len(p2.coeff) - 1
        result_size = len(self.coeff)+len(p2.coeff)-1
        # Create a coeff list with 0s for the result.
        result_coeff = []
        for i in range(result_size):
            result_coeff.append(0)
        
        # Now you can just do += to add the results for each term.
        # We use enumerate again for clarity.
        for i, c1 in enumerate(self.coeff):
            for j, c2 in enumerate(p2.coeff):
                result_coeff[i+j] += c1*c2
        
        return Polynomial(result_coeff)
    
    # Nothing changed here.
    def derivative(self):
        newPoly=Polynomial(self.coeff)
        newPoly.differentiate()
        return newPoly
    
    # The problem to solve in this method is
    # how to make sure that derivatives are put in the correct term.
    # Notice that originally we're simply doing a loop just to make a list.
    # Python gives us a convenient way to do that, called list comprehension
    def differentiate(self):
        self.coeff = [i*self.coeff[i] for i in range(1, len(self.coeff))]


##My anw
class Polynomial(object):
    def __init__(self,coeff):
        self.coeff=coeff
        
    def __call__(self,x):
        value=0
        for i in range(len(self.coeff)):          
            value += self.coeff[i]*x**i
        return value
    
    def __add__(self,other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self,other):
        if len(self.coeff) >= len(other.coeff):
            result_coeff = self.coeff[:]  
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
            ls=[]
            for i in range(0,len(other.coeff)-len(self.coeff)):
                ls.append(0)
                
            result_coeff = self.coeff[:]+ls
            for i in range(len(result_coeff)):
                result_coeff[i] -= other.coeff[i]
        return Polynomial(result_coeff)
        
    def __mul__(self,other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        ls=[]
        for i in range(0,M+N+1):
            ls.append(0)
                
        result_coeff = ls
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)
                
    def differentiate(self):
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]

      
    def derivative(self):
        dpdx = Polynomial(self.coeff[:])
        dpdx.differentiate()
        return dpdx
        
        
p1 = Polynomial ([1 , -1])
p2 = Polynomial ([0 , 1, 0, 0, -6, -1])
p3 = p1 + p2
print p3.coeff
[1, 0, 0, 0, -6, -1]
p4 = p1*p2
print p4.coeff
[0, 1, -1, 0, -6, 5, 1]
p5 = p2. derivative ()
print p5.coeff
[1, 0, 0, -24, -5]
p = Polynomial ([1 , 2, 3])
q = Polynomial ([2 , 3])
r=p-q
print r.coeff
[-1, -1, 3]
r=q-p
print r.coeff
[1, 1, -3]
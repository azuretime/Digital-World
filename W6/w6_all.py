# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 01:08:38 2017

@author: Jiang Jinjing
"""
## P1
def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst
##  
def reverse(s):
    rers = []
    for i in range(len(s)):
        rers.append(s[len(s)-i-1])
    rers = ''.join(rers)
    return rers
print reverse('how are you?')
##
def reverse(s):
    rev = ""
    for i in range(len(s)-1, -1, -1):
        rev = rev + s[i]
    return rev

# Repeatedly adding of strings is inefficient.
# Use list instead, then join.
def reverse(s):
    rev = []
    for i in range(len(s)-1, -1, -1):
        rev.append(s[i])
    rev = "".join(rev) # Convert from list of strings to string.
    return rev
    
    
## P2
def check_password(password):
    if len(password) < 8:
        return False
    countD = 0
    while len(password) >= 8:
        for i in password:
            if i.isdigit():
                countD += 1   
        #return countD
        if countD < 2:
            return False
        else:
            return True
##
def check_password(password):
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    countDigit=0
    for c in password:
        if c.isdigit():
            countDigit+=1
    if countDigit < 2:
        return False
    return True
    
    
    
    
## P3
def longest_common_prefix(s1,s2):
    common=''
    lens1=len(s1)
    lens2=len(s2)
    if lens1 < lens2:
        shortstr=s1
        longstr=s2
    else:
        shortstr=s2
        longstr=s1
    for i in range(len(shortstr)):
        if shortstr[i]==longstr[i]:
            common+=shortstr[i]
        else:
            return common

# Whenever you need string concatenation, you can use lists and str.join too. (Check python docs)
def longest_common_prefix(s1,s2):
    prefix = [] 
    for i,j in zip(s1,s2): # You can use zip too.
        if i==j:
            prefix.append(i)
        else:
            break
    return "".join(prefix)
    
    
    
    
    
## P4
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

# Instead of directly manipulating the Coordinate's attributes, you can make better use of the Coordinate class.
# You will learn more about this in week 8.
class Coordinate:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        # Alternatively, you can calculate mag here instead of defining mag().
        # This way, you calculate mag only once.
        # self.mag = (x**2 + y**2)**0.5
    
    def mag(self):
        return (self.x**2 + self.y**2)**0.5

def get_maxmin_mag(f):
    pmin = None
    pmax = None
    for line in f:
        coords = line.split()
        p = Coordinate(coords[0], coords[1])
        if (pmin is None) or (p.mag() < pmin.mag()):
            pmin = p
        if (pmax is None) or (p.mag() > pmax.mag()):
            pmax = p
    
    return pmax,pmin




    
## H1
def binary_to_decimal(binaryStr):
    d=0
    count=0
    for c in binaryStr[::-1]:
        if c=='1':
            n =2**count
            d = n+d
        count+=1
    return d
##
def binary_to_decimal(binaryStr):
    dec=0
    count=0
    for c in binaryStr[::-1]:
        if c=='1':
            dec+=2**count
        count+=1
    return dec
    
    

    
## H2
def uncompressed(s):
   i = 0
   new_s = ''
   number = 1
   while i < len(s):
       if s[i].isdigit():
           number = int(s[i])
       else:
           character = s[i]
           new_s += character * number
           number = 1
       i += 1
   return new_s

##
def uncompressed(s):
    retstr = ""
    for i in range(0,len(s),2):
        retstr += (int(s[i])*s[i+1]) # string*integer repeats the string, eg. "a"*3 = "aaa"
    return retstr

def uncompressed(s):
    i=0
    retstr=''
    while i < len(s):
        try:               # Try/except checks if any errors happen in the try block
            freq=int(s[i]) # If s[i] is not a integer, it will cause an error (aka Exception).
        except ValueError: # except will catch the error and handle it.
            freq=1         # In this case, s[i] is not a number,
            i-=1           # so we need to make the code treat it as a letter by
                           # simulating that we read a 1 in front of it.
                           # Note that in this question, it's not necessary to check for bad input,
                           # but it is always good to check for it.
        i+=1
        letter=s[i]        # There's a possibility for bad input here, can you see it?
        for j in range(freq):
            retstr+=letter
        i+=1
        
    return retstr

def uncompressed(s):
    i=0
    retstr=''
    while i < len(s):
        if s[i] not in "1234567890": # This is a "guard clause" that checks if s[i] is a valid integer before decompressing.
            i += 1                   # Otherwise, just skip the letter.
            continue                 # continue advances to the next iteration of the loop.
        freq = int(s[i])
        letter = s[i+1]              # There's a possibility for bad input here, can you see it?
        retstr += letter*freq
        i+=2
    return retstr

# This answer makes use of recursion
def uncompressed(s):
    if len(s)<2:
        return s
    if s[0] not in "1234567890":
        return s[0]+uncompressed(s[1:])
    else:
        return (int(s[0])*s[1])+uncompressed(s[2:])

        
        
        
        
        
## H3
import string
UpperCase = string.ascii_uppercase

def get_base_counts2(dna):
    for letter in dna:
        if not (letter in UpperCase):
            return 'The input DNA string is invalid'            

    dict={'A':0,'C':0,'G':0,'T':0}
    for letter in UpperCase:
        if (dna.count(letter) != 0) and (letter in ['A','C','G','T']):
            dict[letter] += dna.count(letter)
    return(dict)
    
##
import string
UpperCase = string.ascii_uppercase

def get_base_counts2(dna):
    for letter in dna:
        if not (letter in UpperCase):
            return 'The input DNA string is invalid'            

    counts = {'A':0,'C':0,'G':0,'T':0}
    for letter in UpperCase:
        if (dna.count(letter) != 0) and (letter in ['A','C','G','T']):
            counts[letter] += dna.count(letter)
    return counts

import string
UpperCase = string.ascii_uppercase

def get_base_counts2(dna):
    for letter in dna:
        if letter not in UpperCase:
            return 'The input DNA string is invalid'            

    counts = {'A':0,'C':0,'G':0,'T':0}
    for letter in counts: # You can just count the letters you want, which are: A,C,G,T.
        counts[letter] = dna.count(letter)
    return counts
    

    
    
## H4
def get_fundamental_constants(f):
    constants={}
    alist = f.readlines()
    length = len(alist)
    i = 2
    while i < length:
        (key, val, dim) = alist[i].split() # This is tuple unpacking.
        constants[key] = float(val)
        i += 1
    return constants

def get_fundamental_constants(f):
    constants={}
    f.next() # use file.next() to skip the first 2 lines.
    f.next()
    for line in f: # iterate through the rest of the file
        (key, val, dim) = line.split()
        constants[key] = float(val)
    return constants
    
    
    
    
    
## H5
def process_scores(f):
    total=0
    count=0
    data=f.read()
    scores=data.split()
    for s in scores:
        total+=float(s.strip())
        count+=1
    average=total/count
    return total,average
    

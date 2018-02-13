# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 15:24:36 2017

@author: Jiang Jinjing
"""

## P2
def compound_value_months(monthlyAmt, annualRate, months):
    mr = annualRate/12.0
    i = 1
    m = 0
    while i <= months:
        m = (monthlyAmt + m)*(1+mr)
        i += 1
    return round(m,2)
##
def compound_value_months(monthlyAmt, annualRate, months):
    monthRate=annualRate/12.0
    multiplier=(1+monthRate)
    val=0
    for i in range(months):
        val=(monthlyAmt+val)*multiplier
    return val
    
    
    
    
## P3
####### Your function should return a tuple containing a list of average #####
####### and the overall average, e.g., ([3.5,6.0,1.4], 3.625) ################  

def find_average(listOfLists):
    averages = []
    totalV = 0.0
    numE = 0.0
    for group in listOfLists:
        group_sum = 0.0
        for value in group:
            group_sum += value
        if len(group)>0:
            v = group_sum / len(group)
            v = round(v,3)
        elif len(group)==0:
            v=0.0
        totalV = totalV + group_sum
        numE += len(group)
        averages.append(v)
        aver = totalV/numE
        
    return (averages,aver)
print find_average([[1,2,5,3],[3,-2,6,7,6,8],[],[3,-1,-4]])    
##
def find_average(listOfLists):
    aveList = []
    totalVal = 0.0
    numElements = 0

    i = 0
    while (i < len(listOfLists)):
         sumVal = 0.0
         alist = listOfLists[i]
         j=0
         while (j < len(alist)):
             sumVal += alist[j]
             j = j + 1
         if (len(alist) > 0):
             aveVal = sumVal / len(alist)
         else:
             aveVal = sumVal
         aveList += [aveVal]
         totalVal += sumVal
         numElements += len(alist)
         i = i + 1

    aveValue = totalVal/numElements

    return (aveList, aveValue)

    
    
    
    
## P4
def transpose_matrix(a):
    b = []
    colb = len(a);
    rowb = len(a[0]);
    for i in range(rowb):
        rowList = []
        for j in range(colb):
            rowList.append(a[j][i])
        b.append(rowList)
    return b
##
def transpose_matrix(a):
    b = []
    colb = len(a);
    rowb = len(a[0]);
    for i in range(rowb):
        rowList = []
        for j in range(colb):
            rowList.append(a[j][i])
        b.append(rowList)
    return b


    
    
    
## P5
def get_details(name, key, phonebook):
    length_list = len(phonebook)
    for i in range(length_list):
        my_dd = phonebook[i]
        if ( my_dd['name'] == name and key in my_dd):
            return my_dd[key]
    return None
##
def get_details(name, key, phonebook):
	for entry in phonebook:
		if name == entry['name']:
			return entry[key]




## P6
   
def get_base_counts(dna):
    dict={}
    for letter in dna:
        if letter!='A' and letter!='C' and letter!='T' and letter!='G' :
            return 'The input DNA string is invalid'
        elif letter =='A' or letter =='C' or letter == 'T' or letter == 'G': 
            if not letter in dict.keys():
                dict[letter] = 1
            elif letter in dict.keys():
                dict[letter] += 1
            
    return dict
##
def get_base_counts(dna):
    counts={}
    for base in dna:
        if base!='A' and base!='T' and base!='G' and base!='C':
            return 'The input DNA string is invalid'            
        elif base=='A' or base=='C' or base=='T' or base=='G':
             if not base in counts.keys():
                 counts[base]=1
             else:
                 counts[base] += 1
    return counts
    
print get_base_counts('ATTCCGG')    
    
    
## H1 
# submit only part (b)
def get_conversion_table():
    ######Enter your code below ########
    t1=[]
    t2=[]
    t=[]
    table1={}
    for i in range(0,11):
        t.append(i*10)
        t1.append(round((i*10-32.0)*5.0/9.0 ,1))
        t2.append(round((i*10 - 30.0)/2.0,1))
    

    conversion= [t,t1,t2]    #this is the table mentioned in the questions
    return conversion  
    
##
def get_conversion_table():
    F=[0,10,20,30,40,50,60,70,80,90,100]
    C =[]
    CApprox = []

    for i in range(len(F)):
        actualC=round(((F[i]-32)*5/9.0),1)
        approxC = round((F[i]-30)/2,1)
        C.append(actualC)
        CApprox.append(approxC)

    conversion = [F,C,CApprox]
    return conversion
    
    
    
    
    
## H2
def max_list(inp):
    max_list = []
    for i in inp:
        max = i[0]
        for j in i:
            if j > max:
                max = j
        max_list.append(max)
    return max_list
##
def max_list(inp):
    outp=[]
    i = 0
    while (i < len(inp)):
           maxNum = -sys.maxint-1
           j = 0
           while(j < len(inp[i])):
               if (inp[i][j]>maxNum):
                   maxNum = inp[i][j]
               j=j+1
           outp.append(maxNum)
           i=i+1
    return outp
    
    
    
    
    
## H3
def multiplication_table(N):
    if N <= 0 or N%1 != 0 :
        return 'None'
    else:
        list = []
        for i in range(N):
            sub = []
            for j in range(N):
                sub.append((i+1)*(j+1))
            list.append(sub)
        return list
##
def multiplication_table(N):
    if (N < 1):
        return None

    table = []
    i = 1
    i_pos = i-1
    while i < N+1:
        n = 1
        n_pos=n-1
        table.append([])
        while n <= N:
            num = i*n
            table[i_pos].append(num)
            n += 1
            n_pos += 1
        i += 1
        i_pos += 1

    return table

def multiplication_table(N):
    if (N < 1):
        return None
    table = []
    for i in range(1,N+1):
        # This can actually be table.append(range(i,i*N+1,i))
        row = []
        for j in range(i,i*N+1,i):
            row.append(j)
        table.append(row)
    return table
    
    
    
    
    
## H4
def most_frequent(numList):
    dic = {}
    list = []
    max = 0
    for i in numList:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic.keys():
        if dic[i] > max:
            max = dic[i]
    for i in dic.keys():
        if dic[i] == max:
            list.append(i)
    return list

##
def most_frequent(numList):
    d={}
    for i in numList:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    
    maxNumList=[]
    maxFreqList=[]
    
    finished=False
    while not finished:
        maxFreq=0
        maxNum=0

        for k,v in d.items():
            if v>maxFreq:
                maxNum=k
                maxFreq=v
        if d!={}:
            del d[maxNum]
        if maxNumList==[] or maxFreq in maxFreqList:
            maxNumList.append(maxNum)
            maxFreqList.append(maxFreq)
        elif maxNumList!=[]:
            finished=True
    return maxNumList

    
    
    
    
    
## H5
def diff(p):
    q = {}
    if 0 in p:
        del p[0]
    for i in p.keys():
        q[i-1] = p[i]*i
    return q
##
def diff(p):
    dp={}

    keys = p.keys()

    for j in keys:
        if j!=0:
            dp[j-1]=(j)*p[j]
    return dp
    
    
    
    
## E2
def interlock(word1,word2,word3):
    result = False
    word = ''
    if len(word1)!= len(word2) or len(word1)*len(word2) == 0:
        return result
    for i in range(len(word1)):
        word += word1[i] + word2[i]
    if word == word3:
        result = True
    return result
##
def interlock(word1, word2, word3):

    if (len(word1)==0 and len(word2)==0 and len(word3)==0):
        return False
    if (len(word1) != len(word2) or len(word3) != len(word1) + len(word2)):
        return False
    index = 0
    for i in range(len(word1)):
        if (word3[index] != word1[i] or word3[index+1] != word2[i]):
            return False
        index = index + 2
    return True


    
    
## E3
import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throw_dice(n,nExp):
    count = 0.
    for i in range(nExp):
        success = 0
        for m in range(n):
            a = random.randint(1,6)
            if a == 6:
                success =1
        if success ==1:
            count += 1
    p = count/nExp
    return round(p,2)
##
import random
import time
random.seed(round(time.time()/3,-1))   #update the seed every 30 seconds

def n6(n):
    nSix = 0  # no of 6
    for i in range(n):
        eyes = random.randint(1, 6)
        if eyes == 6:
            nSix += 1
    return nSix

def throw_dice(n, nExp):
    M = 0
    for i in range(nExp):
        if n6(n) >= 1:
            M += 1
    probability = float(M)/nExp
    return round(probability,2)
    
    
    
    
    
## E4
import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def pi_approx_by_monte_carlo(numThrows):
    hits = 0
    for i in range (0,numThrows):
        x = random.random()
        y = random.random()
        dist = math.sqrt(math.pow(x,2) + math.pow(y,2))
        if dist <= 1.0:
            hits = hits + 1.0
    pi = 4.0 * (float(hits) / numThrows)
    return round(pi,2)

## E5
#### name your function game
import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code


def game(r, N):
    balance = 0
    for i in range(N):
        balance -= 1
        sum = 0
        for m in range(4):
            sum += random.randint(1,6)
        if sum < 0:
            balance += r
    if balance < 0:
        return False
    else:
        return True
        
##
import math
import random
import time
random.seed(round(time.time()/3,-1))   #update the seed every 30 seconds

def game(r, N):
    M = 0  # counter for no of wins
    gain = 0
    for experiment in range(N):
        eyes = [random.randint(1,6) for i in range(4)]
        if sum(eyes) < 9:
            M += 1
            gain += r-1
        else:
            gain -= 1
    if gain >=0:
        return True
    else:
        return False
        
        
        
        
## E6
import math
def approx_ode(h,t0,y0,tn):
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places
    t = t0
    y = y0
    for i in range(1, int((tn-t0)/h)+1,1):
        y += h*(0.5*f(t,y)+ 0.5*f(t+h,y)+ h*f(t,y))
        t += h
    return round(y,3)

######### Ignore code below this line ######################################

def f(t, y):
    return 4.0-t+2.0*y


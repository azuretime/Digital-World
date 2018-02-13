print'-------------------------------------------------------'
dic = {'orange':3 , 'apple':2}
print dic
print'-------------------------------------------------------'
print 'apple' in dic  #Ture. check whether this key exists
print 2 in dic        #False. cannot check reversely
print'-------------------------------------------------------'
print dic.keys()     #['orange', 'apple']
print dic.keys()[1]  #apple
print dic.values()   #[3, 2]
print dic.values()[1] #2
print'-------------------------------------------------------'
dic['banana'] = 4                          #addition of pair
print dic
print'-------------------------------------------------------'
print dic['orange']                        #3, find value of the key
print dic.keys()[dic.values().index(3)]    #orange, find key of the value (only works if the value is distinct, only got one of that value)
print dic.keys()[0]                        #orange, same as above
print'-------------------------------------------------------'
print dic.values().index(3)                #find index of the values
print dic.keys().index('orange')           #find index of key
print'-------------------------------------------------------'
dic ['orange'] = 5                         #re-assignment
print dic
print'-------------------------------------------------------'
del dic['banana']
print dic
print'-------------------------------------------------------'
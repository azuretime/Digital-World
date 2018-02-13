print'-------------------------------------------------------'
lists = [1,2,3,4,5,6,7,8]
print lists[-2:]    
print'-------------------------------------------------------'
lists[1] = 0
print lists[1]      #list is mutable
print'-------------------------------------------------------'
lists.append(9)
print lists
print'-------------------------------------------------------'
print lists.index(3) #2, index of element 3
print'-------------------------------------------------------'
lists.insert(0,3) #insert 3  at 0 position
print lists
print'-------------------------------------------------------'
lists.remove(3)     #(there are two 3 in the lists, have to remove one by one)
print lists
lists.remove(3)
print lists
print'-------------------------------------------------------'
lists.sort()       #arrange from low to high:[0, 1, 4, 5, 6, 7, 8, 9]
print lists
print'-------------------------------------------------------'
lists2 = [10,11,12,13,14]
print lists + lists2 #[0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print'-------------------------------------------------------'
for a,b in zip(lists,lists2):
    print a * b    
#0
#11
#48
#65
#84

print'-------------------------------------------------------'
lists3 = ['pizza' , 'fries' , 'coke']
for index,item in enumerate(lists3):
    print index+1 , item
#1 pizza
#2 fries
#3 coke
print'-------------------------------------------------------'
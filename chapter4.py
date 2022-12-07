#  chapter 4     
'''                         Lists and Strings                 '''

# create a list 
a=[1,2,3,456,7]
print(a)

#print value of 3 index 
print(a[2])

#change value of l index in list
a[0]=98
print(a)

# crate  items of different data items
a=["sun","moon","star",2,5,6]
print(a)

#list slicing
friends= ["divya","suraj","vivek","ram",44]
print(friends[0:3])

#list methods

l1=[1,8,7,2,21,15]
l1.sort()   
'''incresing ordear'''
print(l1)

l1.reverse()
'''reverse ordear'''
print(l1)

l1.append(45)
'''add any values'''
print(l1)

l1.insert(1,66)
'''add in given position'''
print(l1)

l1.pop(1)
print(l1)
'''remove at particular index'''

l1.remove(21)
print(l1)
'''remove particular word'''

'''                                                        Tuples                      '''


t=(1,2,3,4)
print(t[0])    #not update
              #() writes in this way
#t[3]=5
#print(t)

print(t.count(1))
print(t.index(2))




'''          question problem solving  '''
# write a program to store seven fruits in a list entered by user
'''
f1=input("enter name of fruits ")

f2=input("enter name of fruits ")

f3=input("enter name of fruits ")

f4=input("enter name of fruits ")

f5=input("enter name of fruits ")

f6=input("enter name of fruits ")

f7=input("enter name of fruits ")

fruits=[f1 , f2 , f3 ,f4 ,f5 ,f6,f7 ]
print(fruits)

# write a program to accept marks of six student and displays in sort manner
a=[53,56,46,75,34,87,]
a.sort()
print(a)'''

# chect that tupples cannot be changed
''''a=(2,5,7,6)
a[2]=7
print(a)'''

# write a program to sum a list with 4 numbers
a=[6,7,3,7]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))

# write a program to count the number of zero in the following tuples

a=(7,5,6,0,7,0,80,0)
print(a.count(0))
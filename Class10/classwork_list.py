list_1 = [10, 20]

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

a_nested_list = ['spam', 2.0, 5, [10, 20]] 

print(AFC_east)

AFC_east[3] = 'New York Giants'
print(AFC_east)


print(AFC_east[0:2])
# 0 =< i <2 (no include 0)
print(AFC_east[-2:])
print(AFC_east[2:4])

#---

#Excersice 1

L = [
    ['Apple', 'Google', 'Microsoft'], #list 1
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'], #list 2
    ['Adam', 'Bart', 'Lisa'] #list 3
    
]

print(L[0][0])
#find apple
print(L[2][2])
#find lisa
print(L[1][2][1])
#find on rial

#---
#Traversin a list

for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

#----
#Lenght of list?

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

#---
#List Operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) #prints two lists combine 

#---
m = []
m.append(a)
m.append(b)
print(m)

print([0] * 4)
print(['Tom Brady', 'Bill Belichick']*3)

#---
#list slices

t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t[1:3])
##['b', 'c'] 
print(t[:4])
# a b c d 
print(t[3:])
#d e f

t[1:3] = ['x', 'y']
print(t)
#a x y d e f

#---
#

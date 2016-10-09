
#Dictionaries.py Classwork

#find index of jerry - forget this as we have a better way 
names = ['Rose', 'Jerry', 'Alex']
scores = [95, 75, 85]
print(scores[names.index('Jerry')])

#Output
#75 



#Using Key (name) & value (grade)
grades = {'Jerry': 75, 'Rose': 95}
print(grades['Jerry'])

#Output 
# 75

grades['Brian'] = 90
print(grades)

#Output
#different output order of names & grades every Time. Don't have order in dic but in list we do. 

print(len(grades)) 
#3
print('Jerry' in grades)
#True
print(90 in grades.values())
#True 

#----
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('Bookkeeper')
print(h)
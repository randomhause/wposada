listOne = [1, 2, 3, 3, 1, 4]
 
def has_dups(listOne):
   dictionary = {}
   for item in listOne:
       dictionary[item] = 1 + dictionary.get(item, 0)
       if dictionary[item] > 1:
           return True
   return listOne
 
print(has_dups(listOne))
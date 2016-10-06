
#my file
#Problem 1 
"""Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
  
def nested_sum(t): 
   total = 0 
   for i in t:
       total += sum(i)
   return total 

t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))

#Problem 2
Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
   

#Problem 3

#Problem 4
def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    new_list = t[:]
    new_list.sort()
    return new_list == t
  

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))


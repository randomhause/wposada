
#Problem 1 
"""Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
def nested_sum(t): 
   total = 0 
   for i in t:
       total += sum(i)
   return total 

t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))


    

    
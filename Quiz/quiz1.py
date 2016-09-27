#Question1
"""a, b: two integers
Returns True if either one is 9, or if their sum or difference is 9. 
"""
def crazy_about_9(a, b): 
    if a == 9 or b == 9 or a+b==9:
       return True
    else:
        return False

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))
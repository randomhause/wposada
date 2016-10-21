# Upload quiz_2.py file to Blackboard - Session 12
 
 
def replace_even(data):
    '''
    Replace all elements at an even index in the list with 0.
    No return is required.
    data: the list of values to process'''

   
    for i in range(len(ONE_TEN)):
        if i % 2 != 0:
            ONE_TEN[i]=0 


ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)
 

def remove_middle(data):
     '''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.
 
    data: the list of values to process
     '''
    if len(data) % 2 == 0: #if lenght can be divided by 2 then it is even
        #to remove is use .pop
        #or del data [i]
        data.pop(len(data)/ 2 - 1) #pop the first one. Lenght will be 5 now.
        data.pop(len(data)// 2)
    else: 
        data.pop(len(data)// 2)
 
 # Uncomment the following lines to test
 ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 remove_middle(ONE_TEN)
 print(ONE_TEN)
 

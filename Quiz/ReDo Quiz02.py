
def replace_even(data): 
    for i in range(len(ONE_TEN)):
        if i % 2!= 0: 
            ONE_TEN[i]=0
 

ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)


def remove_middle(data): 
    if len(data) % 2 == 0: 
        data.pop(len(data)//2 - 1)
        data.pop(len(data)//2)
    else:
        data.pop(len(data)//2)
 

ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)
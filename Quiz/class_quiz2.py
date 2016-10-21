#Quiz 2
#dic & list mutiblae 
#int & string inmutable

def replace_even(data):
    for i in range(len(ONE_TEN)):
        if i % 2 != 0: 
            ONE_TEN[i]=0

ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)

def remove_middle(data):
    if len(data) % 2 == 0:
        data.pop(len(data)/2 - 1)
        data.pop(len(data)//2)
    else:
        data.pop(len(data)//2)

ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)

def insert_integer(data, number):
    for i in range(len(data)):
        if data[i] > number: 
            data.insert(i, number)
            break
    return data
    

data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(new_data)

def print_hist(data): 
    key_list = data.keys()
    key_list.sort()
    for key in key_list:
        num_ast = data.get(key)
        print('%: ' %(key) + num_ast * '*')

letter_counts = {'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts)


#Exercise01.1
def ex1_1(result):
result = 0 
for i in range(10):
    result += i #result = result +i

print ex1_1('Sum of range 10 is: ', result)



#Exrecise02
iteration = 4
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#Excercise03

#Only Possivite Intergers 
'''
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans)) '''

#Possivite & Negative Intergers (HW)

x = int(input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans ** 3 == abs(x):
        break
if ans ** 3 != abs(x): 
    print(str(x), 'is not a perfect cube!')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


#cubeRootBisection
cube = 54
epsilon = 0.01
num_guesses = 0 
high = cube 
guess = (high + low) / 2.0

while abs(guess**2 - x) >= epsilon and guess <= x:
    num_guesses += 1
    if guess**2 < x:
        high = guess



print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
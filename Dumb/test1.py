'''
#-------------------------------------#

def happyBirthdayEmily():
    print("Happy Birthday, dear Emily.")


def happyBirthdayAndre():
    print("Happy Birthday, dear Andre.")
  

def main():
    happyBirthdayEmily()
    happyBirthdayAndre()

main()
#-------------------------------------#


def happyBirthday(person):
    print("Happy Birthday, dear " + person + ".")


happyBirthday('Emily')
happyBirthday('Andre')
#-------------------------------------#
'''
def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

main() 
#-------------------------------------#

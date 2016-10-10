"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.

Among them, three were telling the truth while one was lying.
Could you find out who is the thief?

explaining: 
if we suppose JOHN is the thief: 
    1 -> 'john' != thief    FALSE   T
    2 -> 'George' == thief  FALSE   T
    3 -> 'Ringo' == thief   False   F
    4 -> 'RINGO' != thief   TRUE    T
=                             1     3
    #!= (not equal)
"""

for theif in ['John', 'Paul', 'George', 'Ringo']:
    sum = (theif != 'John') + (thief == 'George') + (theif == 'Ringo') + (theif != 'Ringo') = 3
    print(theif)

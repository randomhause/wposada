from PyLyrics import *

#print(PyLyrics.getLyrics('Run-D.M.C.','Sucker M.C.\n\'s (Krush Groove 1)')) #Print the lyrics directly

hip_pop = 
    [PyLyrics.getLyrics('Grandmaster Flash and the Furious Five ','The Message')]
    hip_pop.append(PyLyrics.getLyrics('Sugarhill Gang','Rappers Delight'))
    hip_pop.append(PyLyrics.getLyrics('Afrika Bambaataa','Planet Rock'))
#hip_pop.append(PyLyrics.getLyrics('Run-D.M.C.','Sucker M.C.s')) #Not found
    hip_pop.append(PyLyrics.getLyrics('Geto Boys','Mind Playing Tricks on Me'))
    hip_pop.append(PyLyrics.getLyrics('Snoop Dogg','Nuthin But a G Thang'))
    hip_pop.append(PyLyrics.getLyrics('Public Enemy','Fight the Power'))
    hip_pop.append(PyLyrics.getLyrics('Notorious B.I.G.','Juicy'))
    hip_pop.append(PyLyrics.getLyrics('Eric B.','Paid in Full'))

country =
    [PyLyrics.getLyrics('Johnny Cash', 'I Walk the Line')]
    country.append(PyLyrics.getLyrics('Patsy Cline', 'Crazy'))
    country.append(PyLyrics.getLyrics('Hank Williams','Im So Lonesome I could Cry'))
    country.append(PyLyrics.getLyrics('George Jones', 'He Stopped Loving Her Today'))
    country.append(PyLyrics.getLyrics('Jimmie Rodgers', 'Standing on the Corner'))
    country.append(PyLyrics.getLyrics('Tammy Wynette', 'Stand By Your Man'))
    country.append(PyLyrics.getLyrics('Ray Charles', 'You Dont Know Me'))
    country.append(PyLyrics.getLyrics('Merle Haggard', 'Mama Tried'))
    country.append(PyLyrics.getLyrics('Dolly Parton', 'Jolene'))
    country.append(PyLyrics.getLyrics('Waylon Jennings and Willie Nelson', 'Mammas, Dont Let Your Babies Grow Up to Be Cowboys'))

motown =
    [PyLyrics.getLyrics('The Temptations', 'My Girl')]
    motown.append(PyLyrics.getLyrics('Marvin Gaye', 'Whats Going On'))
    motown.append(PyLyrics.getLyrics('Marvin Gaye', 'I Heard it Through the Grapevine'))
    motown.append(PyLyrics.getLyrics('The Temptations', 'Papa was a Rolling Stone'))
    motown.append(PyLyrics.getLyrics('Smokey Robinson and the Miracles', 'Tracks of My Tears'))
    motown.append(PyLyrics.getLyrics('Marvin Gaye', 'Whats Going On'))


#pop = 


f = open("hip_pop.py", "w")
g_hp = [hip_pop]
f.write("\n".join(map(lambda x: str(x), g_hp)))
f.close()

f2 = open("")


#Test the following print(genre) list 
'''
print(hip_pop[0])
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print(hip_pop[1])
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print(hip_pop[2])
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')
print('-------------------------------------------------------------------------')

#pickup 

'''
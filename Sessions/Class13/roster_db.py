import dbm
import random
ROSTER = ("Beshansky",
          "Collins",
          "Fischer",
          "Giovanucci",
          "Jain",
          "Kim",
          "Lauture",
          "Lee",
          "Maddox",
          "Martinez",
          "Mendez",
          "Oh",
          "Petrone",
          "Posada",
          "Rule",
          "Schilb",
          "Tariq",
          "Wang",
          "Wolf")

visits = ['0']
db = dbm.opn('db_student', 'c')
for student in ROSTER:
    db[student] = random.choice(visits)
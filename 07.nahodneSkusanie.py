from random import *

students = []
newQuestions = []
numStudents = int(input('Uvedzte pocet studentov: '))
numQuestions = int(input('Uvedzte pocet otazok: '))

for i in range(1, numStudents+1):
    students.append(i)
shuffle(students)

if numStudents <= numQuestions:
    question = randint(1,numQuestions)
    newQuestions.append(question)
    for i in range(len(students)-1):
        question = randint(1,numQuestions)

        while question in newQuestions or newQuestions[-1]%2 == question%2: #ked chcete aby sa menila parnost
            question = randint(1,numQuestions)
        
        #while question in newQuestions or newQuestions[-1]%2 == question%2: # <- odkomentujte, ked to nepotrebujete
        #    question = randint(1,numQuestions)
        
        newQuestions.append(question)
    for i in range(len(students)):
        print(i+1,'. student:',students[i],' otazka',newQuestions[i])
else:
    print('Prilis vela studentov')

""" from random import *

students = []
questions = []
even = []
odd = []
numStudents = int(input('Uvedzte pocet studentov: '))
numQuestions = int(input('Uvedzte pocet otazok: '))


if numStudents <= numQuestions:
    for i in range(1, numStudents+1):
        students.append(i)
    shuffle(students)
    for i in range(1, numQuestions+1):
        questions.append(i)

    parity = 1
    for i in questions:
        if parity == 1:
            odd.append(i)
        else:
            even.append(i)
        parity = -parity
    shuffle(odd)
    shuffle(even)

    
else:
    print('Prilis vela studentov')

print(even)
print(odd)"""

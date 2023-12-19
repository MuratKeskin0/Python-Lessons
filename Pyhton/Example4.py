def calculate_average(row):
    row= row[:-1]
    liste= row.split(':')
    studentName= liste[0]
    notes=liste[1].split(',')

    note1=int(notes[0])
    note2=int(notes[1])
    note3=int(notes[2])

    average=(note1+note2+note3)/3

    if average>=90 and average<=100:
        point="AA"
    elif average<90 and average>=80:
        point="BB"
    elif average<80 and average>=70:
        point="CC"
    else:
        point="DD"

    return studentName +": " + point + "\n"


def read_notes():
    with open("exam_notes4.txt","r") as file:
        for row in file:
            print(calculate_average(row))

def input_note():
    name = input('Student name: ')
    surname = input('Student surname: ')
    note1 = input('Student note1: ')
    note2 = input('Student note2: ')
    note3 = input('Student note3: ')

    with open("exam_notes4.txt","a") as file:
        file.write(name+ ' ' + surname + ':' + note1+','+note2+','+note3+'\n')
        

def save_note():
    with open("exam_notes4.txt", "r") as file:
        liste = []
        for i in file:
            liste.append(calculate_average(i))

    with open("results4.txt", "w") as file2:
        for item in liste:
            file2.write(item)
  

while True:
    choice = input('1- read notes\n2- input note\n3- save note\n4- exit\n')

    if choice == "1":
        read_notes()
    elif choice == '2':
       input_note()
    elif choice == '3':
        save_note()
    elif choice == '4':
       break
    else:
        print('invalid choice')
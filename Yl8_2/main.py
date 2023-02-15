import turtle
turtle.pensize(4)
turtle.hideturtle()
turtle.speed(5)

with open ("kilpkonn.txt" , "r") as text:
    temp = text.readlines()
list_text = temp [0].split ()

Antall = 1
List_length = len(list_text)
#while List_length > Antall:
for i in range(0, len(list_text), 2):
    try:
        verdi = int(list_text[Antall])
    except IndexError:
        print("Index out of range")
    if verdi > 0:
        turtle.right(verdi)
        Antall = Antall+1
    try:
        verdi = int(list_text[Antall])
    except IndexError:
        print("Index out of range")
        print (verdi)
    if verdi > 0:
        turtle.forward(verdi)
    Antall = Antall+2

turtle.bgcolor(0, 0, 254)

turtle.done ()
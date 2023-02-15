import turtle

def instructions(turtle): #defineerib instructionsid
    instr = []
    with open(turtle, 'r') as f: #avab turtle teksti faili
        for rida in f:
            command = rida.strip().split(' ')
            instr.append(command)
    return instr

def draw_shape(kolmnurk, turtle): #joonistab kujundi
    for command in kolmnurk:
        if command[0] == 'edasi':
            turtle.forward(int(command[1]))
        elif command[0] == 'tagasi':
            turtle.backward(int(command[1]))
        elif command[0] == 'paremale':
            turtle.right(int(command[1]))
        elif command[0] == 'vasakule':
            turtle.left(int(command[1]))

how_many = int(input("Mitu korda kujund joonistada? ")) #kysitakse mitu korda kujundit soovitakse joonistada

instr = instructions('kilpkonn.txt')

a = input("Sisestage programmi pealkiri: ")
turtle.title(a)


turtil = turtle.Turtle()
turtil.hideturtle()
turtil.speed(0)


for i in range(how_many):
    draw_shape(instr, turtle)

turtle.exitonclick()
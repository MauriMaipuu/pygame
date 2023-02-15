import turtle

def instructions(turtel): #defineerib instructionsid
    instr = []
    with open(turtel, 'r') as f: #avab turtle teksti faili
        for rida in f:
            command = rida.strip().split(' ')
            instr.append(command)
    return instr

def draw_shape(kolmnurk, turtel): #joonistab kujundi
    for command in kolmnurk:
        if command[0] == 'edasi':
            turtel.forward(int(command[1]))
        elif command[0] == 'tagasi':
            turtel.backward(int(command[1]))
        elif command[0] == 'paremale':
            turtel.right(int(command[1]))
        elif command[0] == 'vasakule':
            turtel.left(int(command[1]))

kordade_arv = int(input("Mitu korda kujund joonistada? ")) #kysitakse mitu korda kujundit soovitakse joonistada

instr = instructions('kilpkonn.txt')

a = input("Sisestage programmi pealkiri ")
turtle.title(a)


turtil = turtle.Turtle()
turtil.speed(0)

for i in range(kordade_arv):
    draw_shape(instr)

turtle.exitonclick()
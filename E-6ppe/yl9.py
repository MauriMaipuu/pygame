#Mauri Maipuu
#arvasin et luuakse ristkülik ja kolnurk tekstiga Tere!
#tegelikult luuakse Tere! siis sinine kast ja punane kolmnurk

from tkinter import *  # imporditakse
raam = Tk()  #luuakse tkinteri raam
raam.title("Tühi tahvel")  #raamile antakse pealkiri
tahvel = Canvas(raam, width=600)  #luuakse lõuend mille suurus on 600px

tahvel.create_rectangle(50, 70, 100, 100, width=2, outline="blue")  #tehakse ristkülik ja selle joon värvitakse siniseks
tahvel.create_text(50, 50, text="Tere!")  #luuakse text "Tere!"

tahvel.create_polygon(100, 100, 150, 150, 200, 100, fill="red", outline="black")  #tehakse punane kolmnurk ja sellel on mustad ümbrisjooned

tahvel.pack()
raam.mainloop()  #event loop tkinteri käivitamiseks

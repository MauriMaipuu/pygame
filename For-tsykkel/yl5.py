arvud = [10, 61, 2, 14, 42, 24, 7, 5]


def arvude_jarjend(arv): #teeb sum k2su ilma sum-ita
    summa = 0
    for n in arv:
        summa += n
        print(summa)


if arvud == []:
    print(0)
print(arvude_jarjend(arvud))
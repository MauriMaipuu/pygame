arvud = [13, 24, 16, 48, 27, 19, 84] #arvude loetelu

paaris = 0
paaritu = 0

for arv in arvud: #vaatab millised arvud paaris ja paaritud
    if arv % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

print("Paaris arvusid on: ", paaris)
print("Paarituid arve on: ", paaritu)
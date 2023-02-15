#Mauri Maipuu
#///!!! SAMMUDE YLESSANNE !!!\\\#
sammude_list=[]

f = open('sammud.txt')#avab sammud.txt faili

for rida in f:
    sammude_list.append(rida.strip())#loob iga failis olevale reale indeksi koha listi jaoks
f.close()#paneb kinni faili
print("N2dala sammud:", sammude_list)

#teeb listi integeriks
with open('sammud.txt') as f:
    sammude_list = [ int(i) for i in f ]
sammud_kokku = sum(sammude_list)
print("Samme on kokku:", sammud_kokku)

#keskmise arvutamine
keskmine = round(sum(sammude_list)/len(sammude_list))
print("Keskmine on:", keskmine)

#miinimum sammude arv
minimum = min(sammude_list)
päev = sammude_list.index(minimum)
print("V2iksem sammude arv:",minimum,"oli p2eval ",päev,".")

#suurim sammude arv
maximum = max(sammude_list)
päev2 = sammude_list.index(maximum)
print("Suurim sammude arv:", maximum, "oli p2eval", päev2)
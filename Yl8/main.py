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
print("Keskmine on:", sum(sammude_list)/len(sammude_list))

#miinimum sammude arv
print("V2iksem sammude arv:", min(sammude_list))

#suurim sammude arv
print("Suurim sammude arv:", max(sammude_list))
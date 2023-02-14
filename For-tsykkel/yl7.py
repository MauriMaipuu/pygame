#!!! EI TOOTA HETKEL !!!

months = ['Jaanuar', 'Veebruar', 'M2rts', 'Aprill', 'Mai', 'Juuni', 'Juuli', 'August', 'September', 'Oktoober', 'November', 'Detsember']

x = (input("Sisesta kuup2ev (dd.mm.yyyy): "))
mon, date, year = x.split('.')
month_str = months[int(mon) - 1]
print(f"Formatiseeritud kuup2ev(dd.kuu.yyyyS): {month_str} {date}, {year}")
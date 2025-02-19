import os # impportuojame (itraukiame os)
# # os.chdir("Testinis") # pakeicia aplanka
# # os.mkdir("Testinis_vidinis") # musu esamame aplanke sukuria nauja aplanka
# # os.chdir("C:\AMD\AMD-Software-Installer")
# # os.mkdir(r"C:\UserBenchmark\Testinis_vidinio_vidinis") # \ simboliukas reiskia, kad po jo eina specialus simbolis
# # du būdai nurodyti kelią arba naudoti dviguba bruksneli - \\ arba parasyti pries stringa r raide
# # print("labas \n sveiki")
# os.chdir("Testinis")
# for failas in os.listdir():
#     os.rename(failas,f"{failas}{1}")
# print(os.stat("klaidos.py"))
# import datetime
# print(datetime.datetime.fromtimestamp(1739432495)) # is sekundziu nuo 1970-01-01 grazina normalia data ir laika
# import datetime
# print(datetime.datetime.now().timestamp()) # grazina laika sekundemis nuo 1970-01-01

# with open("naujas.txt","w") as failas: # failas = open("naujas.txt","w") # w - sukuria faila jeigu jo nera, jeigu yra istrina tai kas yra ir uzraso ant virsaus
#     failas.write("As esu naujas tekstas tame paciame faile, taciau atidarytas su w")

# with open("naujas.txt","r") as failas: # r - atidaro nuskaitymo rezime
#     print(failas.read()) # read - nuskaito teksta is failo
# a - skiriasi nuo w tuo, akd vietoje to, kad irasytu ant virsaus jis papildo
# with open("naujas.txt","r+") as failas: # r+ - atidaro nuskaitymo rezime ir leidzia dar prideti teksta kaip su a raide
#     print(failas.read())
#     failas.write("\nTai yra jau pakeistas tekstas dar karta")

# with open("naujas.txt","w", encoding="utf-8") as failas: # encoding butinas dirbant su lt ar kitom specialiom raidem
#     failas.write("Aš klausiu jūsų kaip jums sekasi kiškis, ąsla, ąsotis, ąžuolas, čiburėkas")

# with open("naujas.txt","w", encoding="utf-8") as failas: # r+ (w) - usraso ant virsaus
#     failas.write("ilgas mano tekstas")
#     failas.seek(0) # keiciame kursoriaus pozicija i nurodyta vieta
#     # print(failas.read())
#     failas.write("Testinis")

# with open("naujas.txt","r", encoding="utf-8") as failas: # encoding butinas dirbant su lt ar kitom specialiom raidem
#     # print(failas.readlines())
#     for line in failas.readlines(): # failas = readlines - nuskaito eilutes kaip saraso elementus | readline skaito po eilute
#         print(line, end="")


# failus nuskaityti, failus sukurti, failus istrinti, i failus irasyti, i failus prideti


# failo sukurimas

# with open("tekstinis.txt","w"): # w - sukuria faila ir leidzia irasyti
#     pass 

# failo irasymas - kaip irasyti i faila
# failas turi dvi pagrindines komandas failas.write(tekstinis_turinys) ir failas.read()
tekstas = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# with open("tekstinis.txt","w") as failenis: # failas = open("tekstinis.txt")
#      failenis.write(tekstas)

# failo papildymas tekstu
# with open("tekstinis.txt","a") as failenis: # a - append
#      failenis.write("\nCia yra pridetinis tekstas visi ji matote")


# with open("tekstinis.txt","r") as failenis: # r - read - leidzia nuskaityti
#     nuskaitytas = failenis.read()

# print(nuskaitytas)



# with open("tekstinis.txt","r") as failenis: # r - read - leidzia nuskaityti
#      nuskaitytas_sarasas = failenis.readlines()

# kuri_eilute = 0
# modifikuotas_sarasas = []

# for eilute in nuskaitytas_sarasas: # enumerate - galima panaudoti
#     kuri_eilute += 1
#     modifikuotas_sarasas.append(f"{kuri_eilute}. {eilute}") # idedu visa tekstine eilute i sarasa

# with open("tekstinis.txt","w") as failenis: 
#      for me in modifikuotas_sarasas:
#           failenis.write(me)


# kuri_eilute = 0
# with open("tekstinis.txt","r+") as failenis: # r+ - read + write
#      nuskaitytas_sarasas = failenis.readlines() # nuskaito ir kursorsiu pasilieka gale
#      failenis.seek(0) # padeda kursorsiu i pradzia ir rasom ant virsaus

#      for eilute in nuskaitytas_sarasas: # enumerate - galima panaudoti
#         kuri_eilute += 1
#         failenis.write(f"{kuri_eilute}. {eilute}") # idedu visa tekstine eilute i sarasa

# kuri_eilute = 0
# with open("tekstinis.txt","r+") as failenis: # r+ - read + write
#      nuskaitytas_sarasas = failenis.readlines() # nuskaito ir kursorsiu pasilieka gale
#      failenis.seek(0) # padeda kursorsiu i pradzia ir rasom ant virsaus
#     #  failenis.truncate() # istrina faila
#      failenis.write(f"Modifikacija") # idedu visa tekstine eilute i sarasa

# import this # isivaizduokit kad kazkur yra failas pavadinimu this
# # jo viduje yra taip
# # print(eilerastis)


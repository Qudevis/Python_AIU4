# funkcija yra kodo blokas, kuri galima iskviesti su tam tikrai parametrais (argumentais) ir gauti rezultata (galima kviesti neribota kieki kartu)

# def pasisveikinti(): #visos funkcijos prasideda def (define) + funkcijos_pavadinimas + ():
#     print("Sveiki")
#     print("Funkcija veikia")
# print("Funkcija nebevyksta")

# pasisveikinti() # funkcijos iskvietimas / function call
# print("programa baigta")

# def pasisveikinti(vardas): # vardas - argumentas, privaloma pateikti | vardas = "Jonas"
#     vardas = "Simas"
#     print(f"Sveiki {vardas}")

# name = "Jonas" # sukuriamas kintamasis name
# pasisveikinti(name) # kvietimo metu privalome pateikti visus argumentus
# pasisveikinti(name)
# pasisveikinti(name)
# pasisveikinti(name)
# print(name)

# def suma(sk1, sk2): # funkcija su 2 argumentais - sk1 ir sk2 | sk1 = 4 | sk2 = 9
#     print(f"suma yra: {sk1+sk2}")

# suma(4,9) # eiliskumas svarbus
# suma(5,7) # eiliskumas svarbus

# def suma(sk1, sk2): 
#     # print(f"suma yra: {sk1+sk2}") # O jeigu as noriu dar prie sitos sumos kazka prideti/padaryti ? 
#     return sk1 + sk2 # return zodelis - programai vykstant istato vietoje funkcijos jos grazinama reiksme

# print(suma(4,9)) # grazinta_reiksme = 13
# # print(f"Suma yra: {grazinta_reiksme*2}")

# def saraso_spausdinimas(sarasas):
#     print(sarasas)
#     return 9 # po return funkcija nera vykdoma, sekancios eilutes yra praleidziamios
#     print(sarasas)

# saraso_spausdinimas([4,2,5,8,2,20])

# def pasisveikink(vardas):
#     if vardas == "Justas":
#         return f"Sveiki destytojau {vardas}"
#     else:
#         print("Dar nebaigiau, nes ne destytojas")
#     print("Funkcijos pabaiga")
    
# print(pasisveikink("Justa"))


# def nebutini(sk,sk2,sk3=1): # numatytoji reiksme tai reiksme kuri bus naudojama, jeigu nieko nepaduodame
#     return (sk+sk2)*sk3

# print(nebutini(sk2=5, sk3=7))


# def nebutini(sk,sk2,sk3=1,vardas="Jonas",ar_sudeti=True, sarasas=[1,2,3]): # negali po nebutinu argumentu eiti butini
#     return (sk+sk2)*sk3


# while True:
#     pasirinkimas = input("1. Prideti knyga \n2. Atvaizduoti knygas\njeigu norite isjungti paspauskite q")
#     if pasirinkimas == 1:
#         # kvieciame funkcija prideti knyga
#     elif pasirinkimas == 2:
#         # kvieciame funkcija parodyti visas knygas
#     elif pasirinkimas == 'q':
#         break # bet jeigu visa programa yra while cikle, po break irgi programa nutruks
#         exit() # po exit programa nutraukiama

# zodynas = [{"pavadinimas":"Haris poteris","metai":1999,"Zanras":"Fantastika"}, {"pavadinimas":"Robinas Hudas","metai":1969,"Zanras":"Romanas"}]

# print(zodynas)
# print(zodynas[0]['Zanras'])

# 0. Haris poteris 1999 fantastika
# 1. Robinuas hydas 1969 Romanas






# Pythone egzistuoja du ciklai for ir While

# Ciklo paskirtis yra kartoti ta pati veiksma daug kartu

# if 4 > 3:
#     print("Labas")

# kiekis = 0
# sarasas = []
# while 4 > kiekis: # 4 > 0 | -> 1 -> 2 -> 3 -> 4
#     print("Labas")
#     kiekis = kiekis + 1 # kiekis = 0 + 1 | kiekis = 1 + 1 | kiekis = 2 + 1 | kiekis = 3 + 1
#     sarasas.append(kiekis)

# print(sarasas)
# salyga neteisinga ciklas baigesi darom kas yra toliau programoje




# sarasas = [4,5,7,4,1,6]

# for skaicius in sarasas: # ar dar yra skaiciu sarase kol yra skaiciu sarase tol ciklas tesis | 1 - iteracija | skaicius = 4
#     # 1 iteracija skaicius = 4 | 2 iteracija skaicius = 5 | skaicius = 7 | skaicius = 4
#     if skaicius == 7:
#         break
#     print(skaicius)

# range paskirtis yra sukurti sarasa su nurodytais skaiciais pavyzdiui
# range(5) sukuria sarasa [0,1,2,3,4] # range(5,10) -> [5,6,7,8,9]

# for skaicius in range(5):
#     print(skaicius)

# 4 strukturos - lentynos | list(sarasas) - jis laiko reiksmes pagal indeksa (nuo 0 iki tiek kiek yra skaiciu)
# zodynas - laiko reiksmes pagal rakta pavyzdziui {"Vardas":"Mantas"}
# tuple - tuple is esmes yra identiskas sarasui, tik jau ji sukurus nebegalima ideti ar pakeisti reiksmiu bet greitesnis nei sarasas
# greitesnis tai reiskia, kad tiesiog maziau laiko (milisekundemis) trunka paimti elementus is jo
# setas - tai pagrindinis skirtumas nuo saraso, kad sete gali buti tik unikalios reiksmes pvz negali buti {1,1} turi buti tik tokios pvz {1,2,3,4}
# list - [values], set - {values} dictionary - {key:value}, tuple - (values)
# suskaiciuoti kiek yra teisingu atsakymu [True,True,True,False] sum(sarasas) --- 3

# tekstas = "9"
# print(tekstas+tekstas)
# skaicius = list(tekstas)
# print(skaicius+skaicius)

# sarasas = ["9","5","2"] # "9 5 2".split()

# suma = 0
# for skaicius in sarasas:
#     suma = suma + int(skaicius)
# print(suma)


# sarasas = ["9","5","2"] # "9 5 2".split()
# skaiciu_sarasas = []

# for skaicius in sarasas:
#     skaiciu_sarasas.append(int(skaicius))

# print(skaiciu_sarasas) # ["9","5","2"] -> [9,5,2]




# def galutine_kaina(kaina,kiekis = 1,nuolaida = 1,ar_taikoma_nuolaida=False): # nuolaida - 0.9
#     gal_kaina = kaina * kiekis

#     if ar_taikoma_nuolaida:
#         gal_kaina = gal_kaina * nuolaida
#     return gal_kaina

# rezultatas = galutine_kaina(10,nuolaida=0.8,ar_taikoma_nuolaida=True)

# print(f"Jusu galutine kaina yra: {rezultatas}")


# def skaiciu_suma(*args): # -> abc (a,b,c)
#     suma = 0
#     for skaicius in args:
#         suma += skaicius
#     return suma

# a,b,c = 7,9,5
# print(f"Jusu suma yra: {skaiciu_suma(a,b,c)}")


# def skaiciu_suma(sarasas): # -> abc [a,b,c]
#     suma = 0
#     for skaicius in sarasas:
#         suma += skaicius
#     return suma


# print(f"Jusu suma yra: {skaiciu_suma([a,b,c])}")

# print(7,9,8,5)


# def spausdinimas(**kwargs): # -> {'Vardas': 'Justas', 'Pavarde': 'Kvederis', 'Amzius': 25}
#     for kvp in kwargs.items(): # kvp - key value pairs (rakto reiksmes poros)
#         print(kvp)

# spausdinimas(Vardas="Justas",Pavarde="Kvederis",Amzius=25)



# def skaiciu_suma(daugiklis,*args): # -> abc (a,b,c)
#     suma = 0
#     for skaicius in args:
#         suma += skaicius
#     return suma * daugiklis

# a,b,c = 7,9,5
# print(f"Jusu suma yra: {skaiciu_suma(a,b,c)}") # b ir c saraso dalis a - daugiklis

# def suma(a,b):
#     return a  + b # 9

# def spausdinimas(a,b,antraste):
#     print(f"{antraste} {suma(a,b)}")

# spausdinimas(4,6,"Jusu suma yra:")

# jus turite funkcija kuri patikrina ar skaicius yra int ir neleidzia nieko daryti kol nera int
# kvieciame ja is funkcijos kurioje reikia skaiciu 
# visa tai kvieciame is pagrindines funkcijos kurioje yra inputai ir printinimas
# visai tai kviestumeme is pagrindines programos

# suma(4,5) # Kai funkcija vykdoma cia atsiranda tiesiog 9 

# def grazina_tris(skaicius):
#     return 9, 5+skaicius,2*3
# # a,b,c = (9, 10, 6)
# print(grazina_tris(5)) # (9, 10, 6)

# globalus = 10

# def funkcija():
#     lokalus = 12
#     suma = globalus + lokalus # lokalus islieka funkcijos viduje
#     print(suma)

# kita_suma = globalus + lokalus

# print(kita_suma)
# funkcija()


# globalus = 10

# def funkcija():
#     lokalus = 12
#     globalus = 19 # is esmes yra kopija globalaus padaryta lokaliu
#     suma = globalus + lokalus # lokalus islieka funkcijos viduje
#     print(suma)

# # kita_suma = globalus + lokalus

# # print(kita_suma)
# funkcija()
# print(globalus)


# def kazkas(skaicius):
#     skaicius = 15
#     return skaicius
# sk = 9
# print(kazkas(sk))
# print(sk)

# def kazkas(skaiciai):
#     skaiciai.append(19)
#     return skaiciai
# sk = [4,5,8]
# print(kazkas(sk))
# print(sk)

# globalus = 10

# def funkcija():
#     global globalus # global zodelis funkcijoje pasako, kad jos viduje naudosime ne kopija o originala(t.y. globalu kintamaji)
#     lokalus = 12
#     globalus = 19 
#     suma = globalus + lokalus # lokalus islieka funkcijos viduje
#     print(suma)

# # kita_suma = globalus + lokalus

# # print(kita_suma)
# funkcija()
# print(globalus)


# def funkcija():
#     lokalus = 9
#     def funkcija2():
#         lokalus = 7
#         print(lokalus)
#     funkcija2()
#     print(lokalus)

# funkcija()


# print = 5

# print(19) # 5(19)

# cia yra komentaras
# vis dar komentaras... o gal ne ?

#veikia kaip komenatras - tik netikras
# """ 
# Cia yra komentaras
# vis dar komentaras
# ir cia vis dar tikrai komentaras
# """

# # veikia kaip keliu eiluciu stringas
# zodziai = '''
# Labas
# kaip sekasi
# kaip viskas
# Ar girdi mane ?
# '''
# print(zodziai)


# def funkcija(argumentas):
#     '''
#     Labas as esu funkcija \n
#     :param argumentas: Nieko nedaro \n
#     :return: Grazina visados nuli
#     '''
#     return 0

# funkcija()

# def funkcija(sarasas : list):
#     sarasas.append(15)
#     for i in sarasas:
#         print(i)
#     return 0

# funkcija([1,2,3])

# print(5,9,8, sep=",")

# def kubu(sk):
#     return sk ** 3

# funkcija = lambda sk: sk ** 3

# print(funkcija(5)) 

# sar = []
# for sk in range(11):
#     if sk > 3:
#         sar.append(sk*5)

# sarasas = [sk*5 for sk in range(11) if sk > 3] # ka ideti i sarasa | ciklas | dejimo salyga

# print(sarasas)

# sarasas = [(x+1+5*3-1+3) if x >= 45 else x+5 for x in range(50)] # ka ideti i sarasa | dejimo salyga | ciklas 
# print(sarasas)

# def kubu(sk):
#     return sk ** 3

# skaiciai = "4 8 5 9 5 21 5 8 4 536".split()
# # print(skaiciai)

# # ns = []
# skaiciai = [int(sk) for sk in skaiciai] # padarom visus skaicius integeriais

# sarasas = list(map(kubu, skaiciai)) # map pritaiko funkcija kiekvienam saraso elementui atitinka toki dalyka:

# # for sk in skaiciai:
# #     ns.append(kubu(sk))

# print(sarasas)

# List comprehension rezultatas yra tiesiog sarasas [sk2 for sk2 in skaiciai] -> [4,8,5,4,56,1,3,14,564]
skaiciai = [4,8,5,4,56,1,3,14,564]

sarasas = list(map(lambda sk: sk**3, skaiciai)) # 

print(sarasas)


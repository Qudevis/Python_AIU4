# skaiciai = [8,4,2,1,5]

# suma = 0

# for skaicius in skaiciai: # 1 iteracija -> skaicius = skaiciai[0] | 2 iteracija -> skaicius = skaiciai[1] | ir t.t. su visomis iteracijomis
#     suma = suma + skaicius
#     print(f"Tarpine suma {suma}, o pridetas skaicius yra {skaicius}")


# print(suma)


# zodziai = ["Labas", "kaip","sekasi"]

# for zodis in zodziai:
#     print(zodis)

# kiekis = 5
# kartas = 0

# while kartas < kiekis: # Kai kartas pasiekia 5 salyga nebeteisinga
#     print(f"{kartas} yra - Labas")
#     if 1 >5:
#         pass
#     else:
#         pass
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# kartas = 0
# sarasas = []

# while kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# print(sarasas)



# kartas = 0
# sarasas = []

# while kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# print(sarasas)


# kartas = 0
# sarasas = []

# if kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 
# if kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 
# if kartas < 2: # Kai kartas pasiekia 5 salyga nebeteisinga
#     ivestis = input("Iveskite skaiciu: ")
#     sarasas.append(ivestis)
#     kartas = kartas + 1 # kartas = 0... +1... Kartas = 1 ..... +1 ... Kartas = 2. 

# print(sarasas)


dictionary = {"Jonas":20,"Antanas":25,"Justas":15}


# for raktas in dictionary.keys(): # dictionary.keys() arba dictionary -> eina per raktus
#     print(raktas)

# for reiksme in dictionary.values(): # dictionary.values()  -> eina per reiksmes
#     print(reiksme)

# print(dictionary.items())

# tuplu_sarasas = [('Jonas', 20), ('Antanas', 25), ('Justas', 15)]

# tuplas = (4,9)
# kint1, kint2, kint = tuplas
# print(kint2)

# sarasas = (kintamasis,8,2,4) # [] - sarasas | () - tuple | {} - setas | {raktas:reiksme} - zodynas

# for key, value in dictionary.items(): # key, value = ('Jonas', 20) | kvp = ('Antanas', 25)
#     print(f"Raktas yra: {key} o reiksme {value}")



# sarasas = range(10,100) # range(nuo,iki) generuoja skaicius (antras skaicius ne imtinai)

# print(list(sarasas))

# for skaicius in range(20): # range(20) = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#     print(skaicius)

# for skaicius in range(5,20,3): # range(nuo,iki,zingsnis) | taip pat kaip ir stringe stringas[nuo:iki:zingsnis]
#     print(skaicius)

# tuplas = (4,2,8,5)

# for skaicius in tuplas:
#     if skaicius > 6:
#         print(skaicius)
#     else:
#         print(f"netinkamas skaicius {skaicius}")


# ar_neteisingas = True
# # 2> 3 -> False
# # 3> 1 -> True
# while ar_neteisingas:
#     ivestis = input("Iveskite tik skaiciu 5")
#     if ivestis == "5": 
#         ar_neteisingas = False

# print("Programa Baigta")


# ar_neteisingas = True
# # 2> 3 -> False
# # 3> 1 -> True
# while ar_neteisingas:
#     ivestis = input("Iveskite tik skaiciu 5")
#     if ivestis.isdigit():
#         if int(ivestis) == 5: 
#             ar_neteisingas = False

# print("Programa Baigta")

# a = 0
# while True:
#     a = a +1
#     print(a)

# sarasas = [8,5,2,6,9,3, 6] # surasti ar sarase yra 4 (reiksme) | -> in yra tiesiog pasleptas ciklas

# for elementas in sarasas:
#     if elementas == 6:
#         print("Egzistuoja")
#         break # nutraukia cikla, siuo atveju 4 iteracijos metu, ir 9 3 ir 6 net nebetikrina

# print("Programa baigta")

# sarasas = [8,5,2,6,9,3, 6] # suradus skaiciu didesni nei 7 ji atspaudinti

# for skaicius in sarasas:
#     if skaicius > 7:
#         print(skaicius)
#     else:
#         continue # praleisti likusia iteracijos dali
#     #cia vykdoma tik jeigu nesuveike continue
#     print("Dar kazka darau")


# sarasu_sarasas = [14,[4,7,5],8,9]

# for elementas in sarasu_sarasas:
#     if type(elementas) == list:
#         for el in elementas: # elementas = [4,7,5]
#             print(el)


# for sk in range(10):
#     for sk2 in range(10):
#         print(f"sk: {sk} ir sk2: {sk2}")

# for sk in range(10):
#     pass

# print("labas")


# import random

# print(random.randint(0,10)) # random.randint(nuo,iki) generuoja atsitiktinius skaicius tame rezyje nuo 0 iki 10


# # Sukurti programą, kuri:
# # Leistų vartotojui įvesti 5 žodžius
# # Pridėtų įvestus žodžius į sąrašą
# # Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# # Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
# # Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index
 
# user_input = input("Įveskite norimą tekstą: ").replace(",", "").split() # labas,kaip,sekasi | Labas Kaip sekasi -> ["Labas","kaip","sekasi"]
 
# for zodis in user_input: 
#     print(f"Žodis: {zodis}, jo ilgis: {len(zodis)} simboliai, vieta sąraše: {user_input.index(zodis)+1}")
 

# import random
 
# lupokartas=0
 
# while lupokartas<3: # 3<3 -> Netiesa
#     randomskaicius=random.randint(1,6) # 5
#     lupokartas+=1 # lupokartas = 2
#     if randomskaicius==5:
#         print("pralaimejai")
#         break
# else: # Else suveikia, nes 3<3 yra Netiesa
#     print("Laimejai")

# for i in range(8):
#     break
#     pass
# else:
#     print("Ciklas baigtas")
#     pass
 


# # Žodžio apsukimas
# # Paprašykite naudotojo įvesti žodį ar trumpą frazę.
# # Sukurkite programą, kuri, naudodama for ciklą, atspausdintų šį žodį (pvz., "Kava" → "avaK"). Nenaudokite [::-1] ar reverse
# # Išveskite gautą apsuktą tekstą.
 
# user_input = input("Įveskite žodį ar trumpą frazę: ")
# output = []
 
# for indeksas in range(len(user_input)-1, -1, -1):
#     print(indeksas) # Simbolis cia yra indeksas
#     output.append(user_input[indeksas]) # 1 iteracijoje - pridedame s | 
 
# output = " ".join(output) # skiriklis.Join(sarsas) -> jis sujungs saraso elementus i stringa pagal nurodyta skirikli
 
# print(user_input)
# print(output)


# for i in range(10, 0, -1): # Jeigu norime spausdinti skaicius atvirkstine tvarka
#     print(i)


# fraze = input("Iveskite zodi arba trumpa fraze: ")
# atg_fraze = ""
 
# for simbolis in fraze:
#     atg_fraze = simbolis + atg_fraze # 1 iteracija atg_fraze = l | a + l = al | b + al -> bal  
 
# print(atg_fraze)


# sarasas = [4,5,1,2,4,8,9]


# for i in sarasas:
#     print(i)


# sarasas = [4,5,1,2,4,8,9]


# suma = 0
# for i in sarasas:
#     suma = suma + i # suma neegzistuoja...
#     print(i)



# sarasas = [4,5,1,2,4,8,9]


# suma = 0
# for i in sarasas:
#     if i > 0:
#         suma = suma + i # suma neegzistuoja...  

# for i in range(3): # [0,1,2]
#    ivestis =  input(f"Iveskite {i} skaiciu")
#    print(f"Ivedete {ivestis}")

# print(4>1)

# kintamasis = 0

# while True: # 4>0 | 4 > 1 | 4>2 | 4>3 | 4 >4 - False
#     print("VEIKIU KOL SALYGA TEISINGA")
#     kintamasis = kintamasis + 1
#     if kintamasis == 6:
#         break
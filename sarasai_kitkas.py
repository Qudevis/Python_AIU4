# setas = {3,2,3,4,5,4,5,2,3,5,2,5,2,5,2,1,6,7,8,9}
# print(setas)

# setas = {"Benas","Cicinas","Antanas","Egle","Denis"}
# print(setas)

# products = ["Morkos","Bulves","Morkos","Obuoliai","Morkos","Bananai","Obuoliai"]

# setas = set(products) # set() konvertuoja i seta pavyzdiui list -> set

# print(setas)

# products = [{"Morkos":5},{"Obuoliai":15}] # Taip negalima

# setas = set(products) # set() konvertuoja i seta pavyzdiui list -> set

# print(setas)

# products = ["Morkos","Bulves","Morkos","Obuoliai","Morkos","Bananai","Obuoliai"]

# setas = set(products) # set() konvertuoja i seta pavyzdiui list -> set

# # setas.add(4)
# # setas[0] = "Testas" # Negalima keisti reiksmiu
# print(setas)

# zodynas = {"Petras": 19, "kristupas": 17, "Mantas": 18} 

# if "Petras" in zodynas:
#     print("Petras yra zodyne")
# else:
#     print("Petro nera zodyne")

# listas = [[1,2,3],[3,4,5],[6,7,8]]

# if 3  in listas:
#     print("YRa sarase")
# else:
#     print("Tiesa, kad nerastas")


# zodynas = {"Petras": 19, "kristupas": 17, "Mantas": 18} 

# if 19 in zodynas.values(): # nes values grazina sarasa reiksmiu
#     print("Petras yra zodyne")
# else:
#     print("Petro nera zodyne")

# if not 5 > 4: # == != (not tai kaip !)
#     print("Pirmas skaicius didesnis")
# else:
#     print("Antras skaicius didesnis")

# listas = [1,2,3]

# listas1 = [1,2,3]

# if listas is listas1: # is klausia ar tai yra tas pats dalykas patikrindamas ar jie rodo i ta pacia vieta atmintyje,
#     # == - tikrina ar tos pacios reiksmes is tikrina ar rodo i ta pacia vieta (naudojame tik su refference tipo)
#     print("Taip tai tas pats")

# print(type(5)) # atiduoda kokio tipo tai elementas

# if type("10") == int: # netiesa, nes yra stringas
#     print("TAIP TAI Integeris")

# tuplas = (4,5,8,9)
# tuplas = (4,5,8,9,5,[1,2,3], "Labas")
# # tuplas[1] = 3 # NEgalima keisti
# tuplas[5][1] = 9
# print(tuplas) # Greitesnis atvaizdavime

# tuplas = (3,2,5,4,1)

# a,b,c = tuplas # unpacking (ispakavimas) -> a = 3 | b = 2 | c = 5
# print(c)



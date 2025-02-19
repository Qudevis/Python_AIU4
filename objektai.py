# Klases ir Objektai - dvi pagrindines dalys
# klase - yra kaip objekto sablonas, kas tai daug maz bus - kaip namo abstraktus brezinys 
# objektas, jau konkretus pastatytas namas



# class House: # klase
#     def __init__(self): # metodas - (jeigu metodas turi aplink save __ __ vadinasi jis vadinamas (dunder/magic metodu))
#         pass

# class House: 
#     def __init__(self,spalva, heigth, width, window_amount): # metodas yra tiesiog funkcija priklausanti klasei
#         # varguolio_namas.color = spalva
#         # pasiturincio_namas.color = spalva
#         self.color = spalva # savybe - property
#         self.heigth = heigth # self tarsi kalba apie save tai reiskia, kad kiekviena karta kvieciant reiskia as kalbu apie save
#         self.width = width
#         self.window_amount = window_amount

# varguolio_namas = House("Red",400,800,6) # mes sukuriame (inicializuojame ) objekta
# pasiturincio_namas = House("Green",600,20000,20) # mes sukuriame (inicializuojame )

# print(varguolio_namas.color) # gauname viena is objekto reiksmiu
# print(pasiturincio_namas.color)

# varguolio_namas.window_amount = 8 # pakeiciame viena is objekto reiksmiu 
# print(varguolio_namas.window_amount) # atspausdiname pakeista objekto reiksme

# class Dog:
#     def __init__(self, spalva, vardas):
#         self.color = spalva
#         self.name = vardas
#     def loti(self): # visi metodai privalo tureti argumenta self
#         print("AU AU") # klases gali tureti kiek nori ivairiu metodu 

# Reksas = Dog("Brown", "Reksas")

# Sargis = Dog("Black", "Sargis")

# Reksas.loti()

# sar = list() # sukuriau objekta sar is klases list
# sar.append() # kvieciu sar objekto metoda append


# class Dog:
#     def __init__(self, spalva, vardas):
#         self.color = spalva
#         self.name = vardas
#     def loti(self): # visi metodai privalo tureti argumenta self
#         print(f"{self.name} loja - AU AU")
#         # print("AU AU") # klases gali tureti kiek nori ivairiu metodu 

# Reksas = Dog("Brown", "Reksas")

# Sargis = Dog("Black", "Sargis")

# Reksas.loti()
# Sargis.loti()


# class Dog:
#     def __init__(self, spalva, vardas,kojos = 4): # numatytoji reiksme jeigu nieko nenurodome
#         self.color = spalva
#         self.name = vardas
#         self.legs = kojos
#     def loti(self): # visi metodai privalo tureti argumenta self
#         print(f"{self.name} loja - AU AU")
#         # print("AU AU") # klases gali tureti kiek nori ivairiu metodu 

# Reksas = Dog("Brown", "Reksas")

# Sargis = Dog("Black", "Sargis")

# Reksas.loti()
# Sargis.loti()
# # lakis - lucky
# ulakis = Dog("Brown","Ulakis",3)
# print(ulakis.legs)
# print(Reksas.legs)


# class Dog:
#     def __init__(self, spalva, vardas): # numatytoji reiksme jeigu nieko nenurodome
#         self.color = spalva
#         self.name = vardas
#         self.legs = 4
#     def loti(self): # visi metodai privalo tureti argumenta self
#         print(f"{self.name} loja - AU AU")
#         # print("AU AU") # klases gali tureti kiek nori ivairiu metodu 

# Reksas = Dog("Brown", "Reksas")

# Sargis = Dog("Black", "Sargis")

# Reksas.loti()
# Sargis.loti()
# # lakis - lucky
# ulakis = Dog("Brown","Ulakis")
# print(ulakis.legs)
# print(Reksas.legs)
# ulakis.legs = 3
# print(ulakis.legs)


# class Dog:
#     def __init__(self, spalva, vardas): # numatytoji reiksme jeigu nieko nenurodome
#         self.color = spalva
#         self.name = vardas
#         self.legs = 4
#     def loti(self): 
#         print(f"{self.name} loja - AU AU")

#     def __str__(self): # str - specialus metodas, kuris iskvieciamas print metu - skirtas atvaizduoti objekta
#         return f"Šuniukas {self.name} yra {self.color} spalvos"
#     def __repr__(self): # specialus metodas veikia, kai printinama lentyna (list,dict,tuple,set) skirtas reprezentuoti, vietoje to, kad atvaizduoti daug informacijos
#         return f"{self.name}"

# Reksas = Dog("Brown", "Reksas")

# Sargis = Dog("Black", "Sargis")

# # sarasas = [Reksas,Sargis]

# dogs = []
# dogs.append(Reksas)
# dogs.append(Sargis)

# print(dogs)

# for dog in dogs:
#     print(dog)
#     # dog.loti()


# sarasas = [7,1,4,5,8,96]

# with open("test.txt","r") as failas:
#     gautas = failas.read()

# gautas_sar = gautas.replace("[","").replace("]","").split(", ")

# print(gautas_sar)

# import pickle # biblioteka kuri skirta irasyti ir nuskaityti i faila sudetingus objektus

# sarasas = [  
#     {"Pavadinimas":"Haris Poteris ir išminties akmuo","Autorius":"J.K.Rowling","Išleidimo metai":1997,"Žanras":"Fantastinė"},
#     {"Pavadinimas":"Žiedų valdovas: žiedo brolija","Autorius":"J.R.R.Tolkien","Išleidimo metai":1954,"Žanras":"Fantastinė"},
#     {"Pavadinimas":"1984","Autorius":"G. Orwell","Išleidimo metai":1949,"Žanras":"Distopija"},
#     {"Pavadinimas":"Pietinia kronikas","Autorius":"R. Kmita","Išleidimo metai":2017,"Žanras":"Romanas"},
#     {"Pavadinimas":"Mažas gyvenimas","Autorius":"H. Yanagihara","Išleidimo metai":2015,"Žanras":"Romanas"},
#     {"Pavadinimas":"Haris Poteris ir paslapčių kambarys","Autorius":"J.K.Rowling","Išleidimo metai":1998,"Žanras":"Fantastinė"},
#     {"Pavadinimas":"Puikus naujas pasaulis","Autorius":"A. Huxley","Išleidimo metai":1932,"Žanras":"Distopija"},
#     {"Pavadinimas":"Kopa","Autorius":"F. Herbert","Išleidimo metai":1965,"Žanras":"Mokslinė fantastika"}
#     ]

# with open("failas.pickle","wb") as failas: # wb - write bytes
#     pickle.dump(sarasas,failas) # beveik tas pats kas write | pickle.dump(turinys,failas)

# with open("failas.pickle","rb") as failas: # rb - read bytes
#     grazintas = pickle.load(failas) # ka idejom ta ir pasiemame
# # grazintas.append(19)
# grazintas.append({"Pavadinimas":"Pridetinis","Autorius":"F. Herbert","Išleidimo metai":1965,"Žanras":"Mokslinė fantastika"})
# print(grazintas)

# import patarimai # mes galime importuoti savo kitus kodo failus
# patarimai.number_list = [8,1,9,11,15,8]
# print(patarimai.max_number())
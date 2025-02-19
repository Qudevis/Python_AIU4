# # Tai čia yra mano failas kuriame bus pirma paskaita
# # Sios paskaitos tikslas yra susipazinti su kintamaisiais


# # Sita kodo dalis atsakinga uz atvaizdavima

# # print - tikslas isvesti informacija i terminala (konsole)

# # print(30)
# # print(30)
# # print(30)
# # print(30)

# # kintamasis yra kaip dezute kuri saugo kazkokia reiksme


# # kintamasis = 40 + 17

# # kintamasis2 = 30

# # print(kintamasis2)
# # print(40)

# # print(kintamasis)
# # print(kintamasis)
# # print(kintamasis)
# # print(kintamasis)


# # skaicius1 = 5 # dezute su viduje esanciu 9 ir ant jos uzrasu skaicius1
# # skaicius2 = 7

# # suma = skaicius1 + skaicius2 # 9 + 7 | suma = 9 + 7 | suma = 16

# # print(suma)

# # skirtumas = skaicius1 - skaicius2
# # print(skirtumas)

# # print(skaicius1 * skaicius2) # daugyba

# # print(skaicius1 / skaicius2) # dalyba

# # skaicius1 = 10
# # skaicius2 = 10
# # skaicius3 = 10
# # skaicius4 = 10

# # suma = skaicius1 + skaicius2 + skaicius3 + skaicius4
# # print(suma)

# # trumpnenis = 8.57 * 9.85


# # print(trumpnenis)

# # print(7 % 4) # atsakymas, jeigu 4 zmonem norime duoti 7 obuolius, kad visi gautu pilna obuoli visi gauna po 1 ir trys lieka nepadalinti
# # print(7 // 4)

# # print( 4 ** 3)

# # kintamasis = 8.5

# # print(kintamasis)

# # kintamasis = 9

# # print(kintamasis)

# # jono_amzius = 25

# # skaicius1 = 10
# # skaicius2 = 11
# # skaicius3 = 12
# # skaicius4 = 13

# # suma = skaicius1 + skaicius2 # 21
# # print(suma) # 21

# # # suma = suma + skaicius3 # 21 + 12
# # suma += skaicius3 # suma = suma + skaicius3
# # print(suma) # 33

# # suma = suma + skaicius4 # 33 + 13 | suma = 46
# # print(suma) # 46

# # pavarde = "Kvederis" # String (tekstas)

# # print("Justas's last name is...\n" + pavarde + " And he is")

# # amzius = 20

# # print(f"Antanui yra: {amzius} metu") # f raidele leidzia tekste rasyti reistinius sklaustelius {} ir tarp ju ideti kintamuju reiksmes

# # vardas = "justas"
# # pavarde = "kvederis"

# # print(f"Mano vardas yra: {vardas} O mano pavarde yra: {pavarde} Ir man patinka programuoti")
# # print("-"*40)
# # print("Vardas|Pavarde|amzius")
# # print("-"*40)

# # kintamasis = 15

# # print(kintamasis) # ===== print(15)

# # input - tarp skliausteliu parasome teksta naudotojui ir rezultate gauname ka naudotojas ivede

# # vardas = input("Iveskite savo varda: ") # vardas = "Justas"

# # print(f"Sveiki, {vardas}")

# # skaicius1 = input("Iveskite pirma skaiciu: ") # "9"
# # skaicius2 = input("Iveskite pirma skaiciu: ") # "5"



# # print(skaicius1 + skaicius2)

# # tekstas = 15
# # konvertuotas = str(tekstas) # konvertavimas atrodo taip tipas(konvertuojamas_dalykas)
# # print(konvertuotas + "9")

# # skaicius1 = float(input("Iveskite pirma skaiciu: ")) # "9" -> int("9") -> skaicius1 = 9
# # skaicius2 = float(input("Iveskite pirma skaiciu: ")) # "5"


# # print(skaicius1 + skaicius2)

# # print(str(10) + str(15))

# # kint = None

# # print(kint)
# # kazkam = input() # inputo rezultatas yra stringas (tekstas) ir vadinasi jam ivykus visad bus stringas tai pvz kazkam = ""
# # kint = 15
# # po_printo = print(20)
# # print(po_printo)

# # vardas = input("Iveskite varda: ") # vardas = "Justas"
# # input("Iveskite varda: ") # "Justas"

# # "Justas"

# # print(f"atsakymas yra: {"15+9"}")

# # pavarde = input("Iveskite pavarde: ")

# # ilgis = 20

# # print("-"*40)
# # print(f"{"Vardas":^{ilgis}}|{"Pavarde":<20}|{"Amzius":<6}|") # {"Vardas":>{20}} | {turinys:>ilgis}

# # print(f"{"Justas":>{20}}|{"Kvederis":>{20}}|{30:>{6}}|")

# # print(f"{"Aurelijus":>{20}}|{"Kvederis":>{20}}|{30:>{6}}|")

# # print(f"{"ula":>{20}}|{pavarde:>{20}}|{30:>{6}}|")
# # print("-"*40)


# tekstas = "Sveiki, kaip sekasi"

# # tekstas_did = tekstas.upper() # tekstas_did = "SVEIKI, KAIP SEKASI"
# # print(tekstas_did)

# pakeistas = tekstas.replace("a","ei") # Paimama kopija ir ji pakeiciama ORIGINALUS NESIKEICIA
# # tekstas.replace("a","ei") # "SVEIKI, KAIP SEKASI"
# print(tekstas.replace("a","ei"))
# # Jeigu turime kažkur reikšmę, tai galime įstatyti vietoje reikšmės kintamajį su ta reikšme ir atvirkščiai, jeigu turime kažkur kintamajį, galime įstatyti vietoje jo reikšmę
# print(tekstas)












# #Pirma užduotis
 
# pirmas_zodis = input("Įveskite pirmą žodį: ")
# antras_zodis = input("Įveskite antrą žodį: ")
# trecias_zodis = input("Įveskite trečią žodį: ")
 
# print(f"Ir gaunasi sakinys: {pirmas_zodis} {antras_zodis} {trecias_zodis}")
 
# #Antra užduotis
# pirmas_skaicius = int(input("Įveskite pirmą skaičių: "))
# antras_skaicius = int(input("Įveskite antrą skaičių: "))
# trecias_skaicius = int(input("Įveskite trečią skaičių: "))
 
# skaiciu_suma = pirmas_skaicius + antras_skaicius + trecias_skaicius
 
# print(f"Šių skaičių suma: {skaiciu_suma}")

# kint = 15
# test = f"asdas,{kint}"
# "sdas".center
# print(test)


# print(8**0.5)
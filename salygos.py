# True - tiesa | False - netiesa | True - 1 | False - 0
# Bool - turi reikšmes true arba false

# amzius = 18 

# ar_tiesa = (amzius==18) # ar_tiesa = True | ar 18 yra lygu 18

# print(f"Yra {ar_tiesa}, kad tau 18 metu")

# amzius = 18 

# ar_tiesa = (amzius!=18) # 

# print(f"Yra {ar_tiesa}")

# amzius = 19 

# ar_tiesa = (amzius>18) # 

# print(f"Yra {ar_tiesa}, kad tau daugiau nei 18")


# amzius = 18 

# ar_tiesa = (amzius>=18) # (amzius>=18) -> True|False -> ar_tiesa = True arba False

# print(f"Yra {ar_tiesa}, kad tau daugiau nei arba 18 metu")

# amzius = 19 
# vardas = "Jonas"
# ar_tiesa = (amzius>=18 and amzius < 65 and vardas == "Jonas") # and susiaurina tinkamu variantu kieki

# print(f"Yra {ar_tiesa}, kad tu esi pilnametis, bet ne senolis")

# and - siaurina salyga (maziau True) | or - platina salyga (Daugiau True)

# amzius = 500 
# # vardas = "Jonas"
# ar_tiesa = (amzius>=18 or amzius < 65) # and susiaurina tinkamu variantu kieki

# print(f"Yra {ar_tiesa}, kad tu esi pilnametis, bet ne senolis")


# amzius = 12
# vardas = "Jonas"
# ar_tiesa = ( (amzius>=18) or (amzius < 65 and vardas == "Antanas") ) # and susiaurina tinkamu variantu kieki

# print(f"Yra {ar_tiesa}, kad tu esi pilnametis, bet ne senolis")


# if 5>4: # Jeigu 5 yra daugiau nei 4 tada daryk tai, kas yra po dvitaskiu
#     print("Tiesa")

#
# amzius = 90

# if amzius>=18: 
#     print("Tu gali pirkti energetinius gėrimus")
# else:
#     print("Netiesa")
    

# if amzius>=65: 
#     print("Tu esi senolis")
# else:
#     print("Tu nesi senolis")

# print("Programa baigta")


# amzius = 19

# if amzius>=18: # 19 > 18 -> TIesa
#     print("Tu gali pirkti energetinius gėrimus")

#     if amzius>=65: # 19 > 65
#         print("Tu esi senolis")
#     else:
#         print("Tu nesi senolis")
# else:
#     print("Netiesa")
    



# amzius = 19
# if amzius>=18: # 19 > 18 -> TIesa
#     print("Tu gali pirkti energetinius gėrimus")

#     if amzius>=65: # 19 > 65
#         print("Tu esi senolis")
#     else:
#         print("Tu nesi senolis")
# else:
#     print("Netiesa")



# amzius = int(input("Iveskite amziu")) # amzius = "18"

# if amzius == 18: # 18.000000001 ar lygus 18.0 ?
#     print("Tiesa")
# else:
#     print("Netiesa")


# amzius = 4
# if amzius > 65: # Netiesa
#     print("Tu esi senolis")

# if amzius > 18: # Tiesa
#     print("Tu esi suauges")

# if amzius > 3: # Tiesa
#     print("Tu esi vaikas")
# else:
#     print("Priklausau treciam")


# if amzius > 65: # Netiesa
#     print("Tu esi senolis")
# elif amzius > 18: # Tiesa
#     print("Tu esi suauges")
# elif amzius > 3: # NEBETIKRINAM
#     print("Tu esi vaikas")
# else:
#     print("Netiesa")

# amzius = 25

# match amzius:
#     case 18: # if amzius == 18
#         print("Tu aštuoniolika")
#     case 25: # elif amzius == 25
#         print("Tau 25")
#     case 30: # elif amzius == 25
#         print("Tau 30")
#     case 35: # elif amzius == 25
#         print("Tau 35")    

# bilietas = "Netikras" # "Paprastas"/"Vip"/"Super Vip"

# match bilietas:
#     case "Paprastas": # if bilietas == "Paprastas"
#         print("Prašome eiti i stovimas vietas")
#     case "Vip": # elif bilietas == "Vip"
#         print("Prasome eiti į Vip ložę")
#     case "Super Vip": 
#         print("Prasome eiti i specialiai jums paruostas vietas")
#     case _: # else
#         print("Netinkamas bilietas")


# ivestis = input("IVeskite skaiciu") # "15" | "Labas"

# # if 5 ==5: # 5 ==5 -> True | False 

# if ivestis.isdigit():
#     print("Visi yra skaiciai")
#     konvertuotas = int(ivestis)
# else:
#     print("Ivedei ne skaiciu")

# Įdėkite patikrinimus ar viskas atliekama teisingai, pavyzdžiui, patys suprantate,
# kad dalinti iš nulio negalima, kaip pavyzdys.
# Kam pavyksta, taip pat padarykite, kad jeigu būtų įvestas ne skaičius, programa nenulūžtų,
# bet praneštų naudotojui, kad buvo įvesta neteisinga reikšmė)
 
# print("Programa skaičiuotuvas.")
 
# a = input("Įveskite pirmą skaičių: ") # "-7.5"

# if a.replace(".","").replace("-", "").isdigit() or a == 0: # "-7.5" -> "-75" -> "75" -> True
#     a = float(a) # float("-7.5")
# else:
#     print(f"{a} nėra skaičius")
 
# symbol = input("Įveskite metematinį veiksmą\n(Pvz.: +, -, *, /, n^2 arba root) ")
# if symbol == "n^2":
#     print("\tPirmas įvestas skaičius, bus keliamas antro skaičiaus laipsniu")
# elif symbol == "root":
#     print("\tIš pirmo įvesto skaičiaus, bus traukiama antro skaičiaus laipsnio šaknis")
 
# b = (input("Įveskite antrą skaičių: "))
# if b.replace(".","").replace("-", "").isdigit() or b == 0:
#     b = float(b)
# else:
#     print(f"{b} nėra skaičius")


 

# match symbol:
#     case "+":
#         print(f"Rezultatas: {a} + {b} = {a+b}")
#     case "-":
#         print(f"Rezultatas: {a} - {b} = {a-b}")
#     case "*":
#         print(f"Rezultatas: {a} * {b} = {a*b}")
#     case "/":
#         if b == 0:
#             print("Iš nulio dalinti negalima")
#         else:
#             print(f"Rezultatas: {a} / {b} = {a/b}")
#     case "n^2":
#         print(f"Rezultatas: {a} ^ {b} = {a**b}")
#     case "root":
#         print(f"Rezultatas: {b}root({a}) = {a**b}") # 
#     case _:
#         print("Tokios operacijos šiuo metu nėra")
#


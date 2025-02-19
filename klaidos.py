
# try: # Programa megins vykdyti koda kuris yra try bloke
#     print("Prasidejo try blokas")
#     7/0
#     print("Veikiu viskas tvarkoje")
# except: # Jeigu try bloke ivyks klaida, jis vykdys except bloko koda
#     print("Ivyko klaida")


# if 1> 0:
#     print("Dar kazkokie veiksmai")

# print("Programa baigta") # Po try except esantis kodas - toliau veikia
# print("Programa tikrai baigta")


# try: # Programa megins vykdyti koda kuris yra try bloke
#     print("Prasidejo try blokas")
#     "Labas" + 5
#     # sarasas = [1,2,3]
#     # print(sarasas[5])
#     # 7/0
#     # int("Labas")
#     print("Veikiu viskas tvarkoje")
# except ZeroDivisionError as exception: # Jeigu try bloke ivyks klaida, jis vykdys except bloko koda
#     print("Dalyba is nulio negalima")
#     # irasyk i faila, kad ivyko klaida
# except ValueError as ex: # ex = klaidos_tekstas
#     print(f"Negalima tokios reiksmes konvertuoti {ex}")
#     # irasymas i faila
#     # klaidos sutvarkymas
#     # dar kazkas
#     # dar vienas dalykas, su klaida mes isgausime funkcionaluma
# except IndexError as ex:
#     print("Per mazas/didelis indeksas")
# except Exception as e: # negalima except as e -> reikia except Exception as e
#     print("Ivyko nenumatyta klaida")


# if 1> 2:
#     print("Dar kazkokie veiksmai")

# print("Programa baigta") # Po try except esantis kodas - toliau veikia
# print("Programa tikrai baigta")


# try:
#     # 7/0
#     try:
#         int("Labas")
#     except:
#         print("Vidine klaida")

#     print("Tesiama pagrindine programa")
# except:
#     print("Isorine klaida")

# print("Programa baigta")


# raise ZeroDivisionError("Ivyko klaida")
# try:
#     # 7/0
#     try:
#         raise Exception("Ivyko klaida") # padarius raise try sokam i jo except
#         int("Labas")
#         print("Nevygdomas")
#     except:
#         raise Exception("Ivyko klaida") # padarius raise except sokiam i isorini except
        
#     print("Tesiama pagrindine programa")
# except Exception as ex:
#     print(f"Isorine klaida {ex}")

# print("Programa baigta")


# try:
#     print("Cia gali buti klaida")
#     7/0
#     print("Veikiu po klaidos")
#     # open file
#     # veiksmai .... IVYKO KLAIDA
#     # dar kazkas vyksta ir ivyko klaida
# except:
#     print("tikrai ivyko klaida")
# finally:
#     # close file
#     print("Man neidomu ar ivyko klaida ar ne")

# print("Programa baigta")

# while True:
#     try:
#         ivestis = int(input("Iveskite skaiciu: ")) # ivykus klaidai kitos eilutes nevykdo
#         break
#     except:
#         print("Ivedete ne skaiciu, meginte dar karta")


# print("Baigta")


# # Buggy Code: Count occurrences of a specific element.
# numbers = [3, 1, 3, 2, 3, 4, 5]
# target = 3
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         count =+ 1  
# print("The number " + target + " appears " + count + " times.")


# # Buggy Code: Merge two lists alternately.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged = []
# for i in range(len(list1)):
#     merged.append(list1[i])
#     merged.append(list2[i+1])
# print("The merged list is: " + str(merged))

import datetime
 
while True:
    try:
        user_input = input("Įveskite norimą datą ir laiką(formatu: year-month-day, hour:minutes): ")
        user_input = datetime.datetime.strptime(user_input, "%Y-%m-%d, %H:%M")  
 
        # Metai:
        print(f"Nuo šios datos praėjo: {int(datetime.datetime.strftime(datetime.datetime.now(), "%Y")) - int(datetime.datetime.strftime(user_input, "%Y"))}")   
 
        # # Menesiai:
        print(f"Nuo šios datos praėjo: {round(((datetime.datetime.now() - user_input).days/30), ndigits=1)} mėnesių")   
 
        # Dienos:
        print(f"Nuo šios datos praėjo: {(datetime.datetime.now() - user_input).days} dienos")   
 
        # Valandos:
        print(f"Nuo šios datos praėjo: {(datetime.datetime.now()-user_input).days*24} valandos")    
 
        # Minutes:
        print(f"Nuo šios datos praėjo: {(datetime.datetime.now()-user_input).days*24*60} minutės")  
 
        # Sekundes:
        print(f"Nuo šios datos praėjo: {(datetime.datetime.now()-user_input).total_seconds()} sekundės")
 
        break
 
    except ValueError as e:
        print(f"Įvestas neteisingas formatas! Klaida: {e}\n")
        print("Pakartokite įvestį.")
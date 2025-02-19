# print("Sveiki programa pradeta")

# vardas = input("Iveskite savo varda: ")


# print(f"Sveiki {vardas}")

# if vardas == "Justas":
#     print("Jus turite admin teises")
# else:
#     print("Jus esate paprastas naudotojas")

# input("Iveskite bet ka kad uzdarytumete programa")

# tekstas = "Labas, kaip sekasi, kaip laikaisi ?"

# sarasas = tekstas.split() #atskiria stringa per tarpeli (arba nurodyta simboli) ir is jo padaro sarasa

# print(sarasas[3][2])

# sarasas = [[1,2,3],[4,5,6]]

# print(sarasas[1][1])

# ar_pirmas_teisingas = False

# if True: # Ar teisingai tenai ivestas skaicius
#     print("Teisingai")
#     ar_pirmas_teisingas = True
# else:
#     print("Neteisingai")

# ar_antras_teisingas = False
# if True and ar_pirmas_teisingas: # Ar teisingai tenai ivestas antras skaicius
#     print("Teisingai")
#     ar_antras_teisingas = True
# else:
#     print("Neteisingai")


# # Pasirink veiksma
# if ar_pirmas_teisingas and ar_antras_teisingas:


# if 2> 3:
#     print("Tiesa")

#     print("Tikrai tiesa")
# else:
#     print("Netiesa"
#     exit()
#     print("Tikrai netiesa")

# dictionary = {"vard":1,"Pav":2}

# print(list(dictionary))


# kint = {1,2,3}

# sar = [1,2,3,4]
# sar.pop()


# sarasas = [3, 8, 1, 6, 4]
 
# indeksu_sarasas = input("Iveskite du indeksus, atskiriant " ": ").split()
 
# ind1 = int(indeksu_sarasas[0])
# ind2 = int(indeksu_sarasas[1])
 
# # sarasas[ind1], sarasas[ind2] = sarasas[ind2], sarasas[ind1] # sarasas[ind1] = sarasas[ind2] | sarasas[ind2] = sarasas[ind1] 

# tarp_kint = sarasas[ind1]

# sarasas[ind1] = sarasas[ind2]
# sarasas[ind2] = tarp_kint 
 
# print(sarasas)
 
# # Turi būti žodynas, kuriame saugomi valiutų kursai (EUR, USD, GBP).
# # Vartotojas įveda pradinę valiutą, tikslinę valiutą ir sumą.
# # Programa konvertuoja sumą pagal kursą. Jei valiuta neegzistuoja – išveda klaidos pranešimą.
 
exchange_rate = {
    "EUR": {"EUR": 1.0,
            "USD": 1.04,
            "GBP": 0.84},
    "USD": {"EUR": 0.96,
            "USD": 1.0,
            "GBP": 0.81},
    "GBP": {"EUR": 1.2,
            "USD": 1.24,
            "GBP": 1.0}
}
 
user_input = input("Įveskite pradinę valiutą(EUR, USD, GBP), tikslinę valiutą(EUR, USD, GBP) ir sumą: ").replace(",", "").split()
# EUR GBP 50 -> ["Eur", "GBP", 50] | user_input[0] = EUR | user_input[1] = GBP | user_input[2] = "50"
if user_input[0] in exchange_rate and user_input[1] in exchange_rate:
    rate = exchange_rate[user_input[0]][user_input[1]] # exchange_rate[user_input[0]] {"EUR": 1.0, "USD": 1.04,"GBP": 0.84}
    output = float(user_input[2]) * rate # 50 * 0.84

    print(f"{user_input[2]} {user_input[0]} yra {output} {user_input[1]}")
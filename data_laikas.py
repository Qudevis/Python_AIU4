# datetime
import datetime # bibliotekos ikelimas i musu programa

# print(datetime.datetime.today()) # Grazina dabartine data ir laika
# print(datetime.date.today()) # grazina tik data 
# print(datetime.datetime.today().time()) # grazina tik laika

# dob = datetime.datetime(1992,5,19,19,10,15) # sukuria data ir laika (datetime.date sukurtu tik data)
# print(dob)

# suformatuota = dob.strftime("%Y,%m,%d ") # strftime - string from time | suformatuoja data i stringa, pagal nurodymus skliausteliuose
# print(suformatuota)


# ivestis = input("Iveskite savo gimimo data (yyyy-mm-dd)")
# # 2025-09-05 
# dob = datetime.datetime.strptime(ivestis,"%Y-%m-%d") # strptime - parse time from string
# print(dob)

# dob = datetime.datetime(1992,5,19,minute=5) 
# print(dob)
# dob = datetime.datetime(1992,5,19,15,5) 
# print(dob)
# print(dob - datetime.timedelta(0,0,0,0,0,4)) # Nepatogu
# print(dob + datetime.timedelta(hours=6,minutes=2)) # jeigu aprasyme matote ligybe galima taip nurodyti

# siandien = datetime.datetime.today()
# skirtumas = siandien - dob
# print(skirtumas)

# print(datetime.timedelta(weeks=9)) # TimeDelta yra dar vienas tipas kuris fiksuoja laiko poslinki

# import datetime

# # Create date objects directly
# date1 = datetime.date(2024, 1, 1)
# date2 = datetime.date(2025, 2, 5)

# # 2025 - 2024 - 1 * 12 (12) + 1 -> 12 + 1 = 13
# months = (date2.year - date1.year) * 12 + (date2.month - date1.month) 
# print("Total months passed:", months)



 
# # Parašyti programą, kuri:
# # Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# # Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# # Metų
# # Mėnesių
# # Dienų
# # Valandų
# # Minučių
# # Sekundžių
# # Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# # Patarimas: naudoti datetime, .days, .total_seconds()
# # Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje): round(skaicius)
 
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# ivestis = input("Iveskite norima data ir laika formatu yyyy-mm-dd hh:mm:ss : ")
# paverstas = datetime.strptime(ivestis, "%Y-%m-%d %H:%M:%S")

# dabar = datetime.today()


# skirtumas = dabar - paverstas  
# rel_skirtumas = relativedelta(dabar, paverstas)  

# total_seconds = skirtumas.total_seconds()
# total_minutes = total_seconds / 60
# total_hours = total_seconds / 3600
# total_days = skirtumas.days  
# total_months = (rel_skirtumas.years * 12) + rel_skirtumas.months  
# total_years = rel_skirtumas.years  

# print("Jusu ivesta data:", paverstas)
# print("Dabar yra:", dabar)
# print(f"Nuo ivestos datos praejo: {round(total_seconds)} sekundziu")
# print(f"Nuo ivestos datos praejo: {round(total_minutes)} minuciu")
# print(f"Nuo ivestos datos praejo: {round(total_hours)} valandu")
# print(f"Nuo ivestos datos praejo: {total_days} dienu")
# print(f"Nuo ivestos datos praejo: {total_months} menesiu")
# print(f"Nuo ivestos datos praejo: {total_years} metu")

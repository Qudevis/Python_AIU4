# dictionary = {} # tuscias zodynas

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# print(dictionary) # atspausdiname zodyna

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# print(dictionary["Mantas"]) # reiksmes gaunamos pagal rakta

# dictionary["Jonas"] = 8 # Pakeisti zodyno reiksme
# print(dictionary)

# ismesta = dictionary.pop("Mantas") # ismeta elementa ir grazina reiksme (ismeta pagal rakta)
# print(ismesta)

# del dictionary["Mantas"] # Ismeta elementa negrazindamas reiksmes

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} # Netuscias zodynas

# dictionary["Petras"] = 20 # Naujo elemento idejimas | Jeigu tokio rakto nera ides, jeigu yra pakeis reiksme
# print(dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14, 7 : 15} # Netuscias zodynas

# dictionary[7] = "dvidesimt" # Naujo elemento idejimas | Jeigu tokio rakto nera - ides, jeigu yra - pakeis reiksme
# print(dictionary)

# dictionary = {1:7, 2:8, 3:9} 
# print(dictionary[2])

# dictionary = {"Jonas":[8,9,4,10], "Mantas":[2,5,8,10], "Karolis":[10,10,9,10]} 
# karolis_grades = dictionary["Karolis"] # karolis_grades = [10,10,9,10]
# last_grade = karolis_grades[-1]
# print(last_grade)

# dictionary = {"Jonas":[8,9,4,10], "Mantas":[2,5,8,10], "Karolis":[10,10,9,10]} 
# last_grade = dictionary["Karolis"][-1] # dictionary["Karolis"] -> [10,10,9,10] -> [10,10,9,10] [-1]
# print(last_grade)

# dictionary = {"Jonas":{"Mantas":15, "Rimas": 23}, "Mantas":[2,5,8,10], "Karolis":[10,10,9,10]} #sarasai gali tureti sarasus
# print(dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14, "Jonas":12} # Zodyno raktai yra unikalus
# print(dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} 

# new_dictionary = dictionary.copy() # zodynai yra refference tipo (nuorodos)
# dictionary.clear()
# print(new_dictionary)

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} 
# print(dictionary.keys()) # atiduos sarasa raktu
# print(dictionary.values()) # atiduos sarasa reiksmiu

# print(dictionary.get("Petras")) # grazina reiksme jeigu yra, jeigu nera grazina None
# print(dictionary["Petras"]) # Grazina reiksme jeigu yra, jeigu nera klaida/nuluzta

# dictionary = {"Jonas": 9, "Antanas": 11, "Mantas": 14} 

# dictionary1 = {"Petras": 19, "kristupas": 17, "Mantas": 18} 
# dictionary.update(dictionary1) # update - apjungia zodynus, jeigu yra dublikuotu reiksmiu antro zodyno reiksmes prioritizuojamos
# print(dictionary)




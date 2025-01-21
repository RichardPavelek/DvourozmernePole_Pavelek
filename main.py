array = [
    [7, 9, 6],
    [14, 18, 12],
    [28, 26, 24]
]
#Výpis pole
print(array)

#Změna hodnoty v druhém řádku a druhém sloupci
array[1][1] = 105

#Výpis pole
print(array)

#Nový řádek 
new_row = [100, 96, 43, 57]  
array.append(new_row)

# Přidání sloupce
for i in range(len(array)):
    array[i].append(17)

# Výpis pole
print(array)

#Dictonaries

# Neuen Key-Value-Paar hinzufügen
dict_nd = {"a": 1, "b": 2}
dict_nd["c"] = 3
print(dict_nd)


# Mehrere Werte hinzufügen
dict_nd = {"a": 1, "b": 2}
dict_nd.update({"c": 3, "d": 4})
print(dict_nd)


# In einer Schleife befüllen
dict_nd = {}
for x in range(5):
    dict_nd[x] = x ** 2  # Fügt Key-Value-Paare hinzu
print(dict_nd)


#Eine Liste in einem Dictionary speichern (Falls du .append() verwenden willst)
dict_nd = {"zahlen": [1, 2, 3]}
dict_nd["zahlen"].append(4)  # Fügt zur Liste hinzu
print(dict_nd)

    
# Den größten Wert finden
mein_dict = {"a": 10, "b": 25, "c": 5, "d": 39, "e": 40, "f": 40}

max_wert = max(mein_dict.values())  # Größter Value
print(max_wert)  # Output: 40
# hier wird eine Liste mit Values nach dem größten durchsucht: max() gibt nur einen Value zurück


# Key und Value des größten Werts holen
max_key = max(mein_dict, key=mein_dict.get)
print(max_key, mein_dict[max_key])  # Output: d 40
# hier wird ein Dictionary nach dem größten Value durchsucht: max() gibt ein Key zurück


# Die n größten Werte holen
n = 3
top_n = sorted(mein_dict.items(), key=lambda x: x[1], reverse=True)[:n]
print(top_n)  
# es ein Dictonary kann nicht geslicet werden [:2], deswegen wird .items() genutzt


# Alternative: Mit heapq.nlargest() effizient n größte Werte holen (für große Dictionaries)

import heapq

n = 3
top_n = heapq.nlargest(n, mein_dict, key=mein_dict.get)
print(top_n)
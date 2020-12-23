# Datei verschieben
import os
import shutil

cleanOrdner = "C:/Users/mkarm/Downloads/"
ziel_beispiel = "C:/Users/mkarm/OneDrive/Michi/Versicherungen/"
dateien = os.listdir(cleanOrdner)
print(dateien)
print(dateien[0])

for i in dateien:
    print(f"i: {i}")
    if 'Beispiel' in i:
        print("Gefunden - Element Found in Tuple")
        pfad = cleanOrdner + i
        print(pfad)
        shutil.move(pfad, ziel_beispiel)
#    else:
# print("Element not Found in Tuple")

print("Aufräumen beendet")

print("Test pushen - Ergänzung von github")



#funktion schreiben mit Input: gesuchterDateiname, aufzuräumenderOrdner, Zielort
#wenn mehere zutreffende Datein im Verzeichnis, dann alle verschieben mit jeweils einer ausgabe
#Ausgabe dass erfolgreich verschoben wurde
#exe bauen und in autostart hinzufügen
#Buch S. 325

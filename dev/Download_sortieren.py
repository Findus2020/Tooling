# Datei verschieben
import os
import shutil

if __name__ == '__main__':
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

def clean_folder(subject,folder,target):
    folder_list = os.listdir(folder)
    k = 1
    for i in folder_list:
        #print(f"{k}. Datei: {i}") #Ausgabe aller Datein im Quellordner
        k += 1
        if subject in i:
            print(f"{i} gefunden")
            path = folder + i
            shutil.move(path, target)
            print(
            f"Datei: {i}, Quelle: {folder}, Ziel: {target}")

#Audi-Bank
clean_folder("Kontoauszug-1519125726", "C:/Users/mkarm/Downloads/", "C:/Users/mkarm/OneDrive/Michi/Konto/Audi Bank/Kontoauszug 2020")
#Renault-Bank
clean_folder("29131500", "C:/Users/mkarm/Downloads/", "C:/Users/mkarm/OneDrive/Michi/Konto/Renault Bank/Kontoauszug/2020")



#funktion schreiben mit Input: gesuchterDateiname, aufzuräumenderOrdner, Zielort
#wenn mehere zutreffende Datein im Verzeichnis, dann alle verschieben mit jeweils einer ausgabe
#Ausgabe dass erfolgreich verschoben wurde
#exe bauen und in autostart hinzufügen
#Buch S. 325

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
    print(f"Die Datei zum Thema {subject} aus dem Ordner {folder} wird in das Zielverzeichnis {target} verschoben")
    folder_list = os.listdir(folder)
    k = 1
    for i in folder_list:
        print(f"{k}. Datei: {i}")
        k += 1
        if subject in i:
            print(f"{i} gefunden")
            path = folder + i
            shutil.move(path, target)




clean_folder("Bank", "C:/Users/mkarm/Downloads/", "C:/Users/mkarm/OneDrive/Michi/Versicherungen")





#funktion schreiben mit Input: gesuchterDateiname, aufzuräumenderOrdner, Zielort
#wenn mehere zutreffende Datein im Verzeichnis, dann alle verschieben mit jeweils einer ausgabe
#Ausgabe dass erfolgreich verschoben wurde
#exe bauen und in autostart hinzufügen
#Buch S. 325

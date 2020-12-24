# Datei verschieben
import os
import shutil

def clean_folder(name, subject, folder, target):
    folder_list = os.listdir(folder)
    k = 1
    for i in folder_list:
        # print(f"{k}. Datei: {i}") #Ausgabe aller Datein im Quellordner
        k += 1
        if subject in i:
            print(f"{i} gefunden")
            path = folder + i
            shutil.move(path, target)
            print(
                f"Datei: {i}, Quelle: {folder}, Ziel: {target}")

    print(f"{name}: Aufräumen beendet")


#exe bauen und in autostart hinzufügen
#Buch S. 325

import os
import shutil
import PyPDF2

def clean_folder(name, subject, folder, target, pdf_inhalt=None):
    """Funktion die einen Ordner durchsucht und Dateien verschieben. \n
    name: Belieber Name der Suche \n
    subject: Bestandteil des Dateinamens \n
    folder: Durchsuchter Ordner \n
    target: Zielordner \n
    pdf_inhalt: Text-Bestandteil innerhalb des PDF"""

    if not os.path.isdir(target):
        print(f"FEHLER: Angegebener Zielpfad '{target}' existiert nicht!")
        return

    folder_list = os.listdir(folder)  # erstellt eine Liste mit dem Inhalt des aufzuräumenden Ordners
    k = 1
    found = []
    for i in folder_list:
        # print(f"{k}. Datei: {i}") #Ausgabe aller Datein im Quellordner
        k += 1
        if subject in i:
            print(f"{name}: {i} gefunden")
            path = folder + i
            if pdf_inhalt is None:
                shutil.move(path, target)
                print(f"Datei: {i}, Quelle: {folder}, Ziel: {target}")
                found.append(i)
            else:
                pdffileobj = open(path, 'rb')  # creating a pdf file object
                pdfreader = PyPDF2.PdfFileReader(pdffileobj)  # creating a pdf reader object
                pageobj = pdfreader.getPage(0)  # creating a page object
                if pdf_inhalt in pageobj.extractText():  # extracting text from page
                    pdffileobj.close()
                    shutil.move(path, target)
                    print(f"Datei: {i}, Quelle: {folder}, Ziel: {target}, PDF-Inhalt: {pdf_inhalt}")
                    found.append(i)
                else:
                    print(f"{name}: Dateiname passend, jedoch den entsprechenden PDF-Inhalt nicht gefunden")
                    pdffileobj.close()

    print(f"{name}: Aufräumen beendet")

    return found

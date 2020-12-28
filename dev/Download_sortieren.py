"""Ordner durchsuchen und Dateien verschieben"""
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

    folder_list = os.listdir(folder)
    k = 1
    for i in folder_list:
        # print(f"{k}. Datei: {i}") #Ausgabe aller Datein im Quellordner
        k += 1
        if subject in i:
            print(f"{i} gefunden")
            path = folder + i
            if pdf_inhalt == None:
                shutil.move(path, target)
                print(f"Datei: {i}, Quelle: {folder}, Ziel: {target}")
            else:
                pdfFileObj = open(path, 'rb')  # creating a pdf file object
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # creating a pdf reader object
                pageObj = pdfReader.getPage(0)  # creating a page object
                if pdf_inhalt in pageObj.extractText():  # extracting text from page
                    pdfFileObj.close()
                    shutil.move(path, target)
                    print(f"Datei: {i}, Quelle: {folder}, Ziel: {target}, PDF-Inhalt: {pdf_inhalt}")
                else:
                    print("Dateiname passend, jedoch den entsprechenden PDF-Inhalt nicht gefunden")
                    pdfFileObj.close()

    print(f"{name}: Aufräumen beendet")



#exe bauen und in autostart hinzufügen
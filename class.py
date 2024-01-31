import os
import patoolib


class MyClass:
    def __init__(self):
        self.name = ""
        self.hash = ""
        self.filepath_rar = ""
        self.filepath_zip = ""
        self.filepath_folder = ""
        self.filepath_save_csv = ""


def entpacke_archiv(archiv_pfad, ziel_ordner):
    try:
        patoolib.extract_archive(archiv_pfad, outdir=ziel_ordner)
        print(f"Entpackt: {archiv_pfad}")
    except Exception as e:
        print(f"Fehler beim Entpacken von {archiv_pfad}: {e}")


def finde_und_entpacke(dateiendungen, such_ordner, ziel_ordner):
    for root, dirs, files in os.walk(such_ordner):
        for datei in files:
            if datei.endswith(tuple(dateiendungen)):
                voller_pfad = os.path.join(root, datei)
                entpacke_archiv(voller_pfad, ziel_ordner)


# Einstellungen
dateiendungen = ['.zip', '.rar']
such_ordner = 'Pfad/zum/Suchordner'  # Pfad zum Ordner, in dem gesucht werden soll
ziel_ordner = 'Pfad/zum/Zielordner'  # Pfad zum Ordner, in den entpackt werden soll

finde_und_entpacke(dateiendungen, such_ordner, ziel_ordner)

# ------------------------------------
from email.parser import Parser

# Pfad zur E-Mail-Datei
email_datei = '/pfad/zur/email-datei.eml'

# E-Mail-Datei lesen und parsen
with open(email_datei, 'r') as f:
    email_message = Parser().parse(f)

# Betreff ausgeben
print("Betreff:", email_message['Subject'])

# ---------------------------------------

import os
def aendere_dateiendung_zu_eml(alter_pfad):
    if not alter_pfad.lower().endswith('.eml'):
        neuer_pfad = alter_pfad.rsplit('.', 1)[0] + '.eml'
        os.rename(alter_pfad, neuer_pfad)
        print(f"Datei umbenannt: {alter_pfad} -> {neuer_pfad}")
    else:
        print("Datei hat bereits die Endung .eml")

# Beispiel: Ändern Sie den Pfad zur Ihrer Datei
alter_pfad = '/pfad/zur/aktuellen_datei.xyz'
aendere_dateiendung_zu_eml(alter_pfad)

# Auslesen einer Zeile
import email
import email.policy

def extract_line_from_email(eml_file_path, line_number):
    try:
        with open(eml_file_path, 'r', encoding='utf-8') as file:
            msg = email.message_from_file(file, policy=email.policy.default)

            # Ermittle den Inhaltstyp der E-Mail
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        # Extrahiere den Text-Inhalt
                        text = part.get_payload(decode=True).decode()
                        break
            else:
                # Für einfache Nachrichten ohne Teile
                text = msg.get_payload(decode=True).decode()

            # Zeilenweise aufteilen und die spezifische Zeile extrahieren
            lines = text.splitlines()
            if line_number < len(lines):
                specific_line = lines[line_number]
                print("Gesuchte Zeile:", specific_line)
            else:
                print("Zeilennummer ist außerhalb des Bereichs der E-Mail.")

    except Exception as e:
        print(f"Fehler beim Lesen der E-Mail: {e}")

eml_path = 'pfad/zu/deiner/email.eml'
line_number = 10  # Die Zeilennummer, die du extrahieren möchtest (beginnend mit 0)

extract_line_from_email(eml_path, line_number)

import random
import string

# Mindestlänge für ein Passwort
MIN_LAENGE = 16


def generate_password(laenge):
    """Erstellt ein zufälliges Passwort aus Buchstaben, Zahlen und Sonderzeichen."""

    # Alle möglichen Zeichen für das Passwort
    zeichen = string.ascii_letters + string.digits + string.punctuation

    # Passwort wird durch zufällige Auswahl von Zeichen erzeugt
    passwort = "".join(random.choice(zeichen) for _ in range(laenge))

    return passwort


def main():
    print("=== Passwort Generator ===\n")

    try:
        # Eingabe der gewünschten Passwortlänge
        eingabe = input("Gib die gewünschte Länge ein (mindestens 16): ").strip()

        # Umwandlung in eine Zahl
        laenge = int(eingabe)

        # Prüfung der Mindestlänge
        if laenge < MIN_LAENGE:
            print(f"Fehler: Das Passwort muss mindestens {MIN_LAENGE} Zeichen lang sein.")
        else:
            # Passwort erzeugen
            passwort = generate_password(laenge)

            # Ausgabe
            print("\nDein generiertes Passwort lautet:")
            print(passwort)

    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein!")

    except KeyboardInterrupt:
        print("\nProgramm wurde beendet.")


if __name__ == "__main__":
    main()

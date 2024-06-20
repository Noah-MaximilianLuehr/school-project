# Quiz Game

# Fragen und Antworten
Fragen = [
    {"Frage": "Was ist die Hauptstadt von Frankreich?", "Antwort": "Paris", "Zur Auswahl stehen": ["Paris", "London", "Berlin"]},
    {"Frage": "Was is der Größte Planet in unserem Sonnensystem?", "Antwort": "Jupiter", "Zur Auswahl stehen": ["Erde", "Saturn", "Jupiter"]},
    {"Frage": "Was ist das größte Säugetier?", "Antwort": "Wal", "Zur Auswahl stehen": ["Elefant", "Wal", "Löwe"]},
    {"Frage": "Welcher is der höchste Berg?", "Antwort": "Mount Everest", "Zur Auswahl stehen": ["Mount Everest", "Mount Kilimanjaro", "Mount Fuji"]},
    {"Frage": "Welche is die größte noch lebende spezies von Eidechsen?", "Antwort": "Komodowarane", "Zur Auswahl stehen": ["Komodowarane", "Salzwasserkrokodil", "Black Mamba"]},
    
]

# initialisieren der Score
Score = 0

# Willkommensnachricht
print("Wilkommen zum Quiz!")
print("Du wirst fünf Fragen gestellt bekommen, viel Glück!")

# Fragen
for Frage in Fragen:
    print(Frage["Frage"])
    for i, option in enumerate(Frage["Zur Auswahl stehen"], start=1):
        print(f"{i}) {option}")
    while True:
        try:
            choice = int(input("Wähle eine Nummer: "))
            if 1 <= choice <= len(Frage["Zur Auswahl stehen"]):
                if Frage["Zur Auswahl stehen"][choice - 1] == Frage["Antwort"]:
                    print("Richtig!")
                    Score += 1
                else:
                    print(f"Daneben, die Richtige Antwort ist {Frage['Antwort']}")
                break
            else:
                print("Ungültige Eingabe, bitte versuche es erneut.")
        except ValueError:
            print("Ungültige Eingabe, bitte gib eine Nummer ein.")

# Anzeigen der Finalen Punkteanzahl
print(f"\nDein ergebnis ist {Score} von {len(Fragen)}")
if Score == len(Fragen):
    print("Glückwunsch, du hast einen Perfekten Score! :D")
elif Score >= len(Fragen) / 2:
    print("Gut gemacht, du hast bestanden! :)")
else:
    print("Schade, vielleicht schafft du es ja nächstes mal! :(")
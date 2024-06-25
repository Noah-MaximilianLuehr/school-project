# Quiz Game

# Fragen und Antworten
Fragen = [
    {"Frage": " A, »B« or C ", "Antwort": "B", "Zur Auswahl stehen": ["A", "B", "C"]},
]

# initialisieren des Score
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
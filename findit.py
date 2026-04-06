import sys
from os.path import exists
import json


def create_game():
 if not exists("user.json"):
  print("Willkommen bei Find It. Bei diesem Spiel geht es darum, dass du die Wörter anhand von drei Eigenschaften errätst.")
  username = input("Bitte wähle einen Nutzernamen und drücke RETURN, um mit dem Spiel zu beginnen: ")
  if username == "exit":
   print("Ciao!")
   sys.exit(0)
  else:
   # Initialize data dict to collect user's data
   data = {
    "username": username,
    "level": 1,
   }
   with open("user.json", "w") as opened_file:
    json.dump(data, opened_file)
   resume_game()

def resume_game():
 try:
  with open("levels.json", "r") as levels, open("user.json", "r+") as user:
   user_data = json.load(user)
   levels_data = json.load(levels)
   print(f"Willkommen, {user_data['username']}")
   is_running = True
   while(is_running):
    if user_data.get('level') <= len(levels_data.get('levels')):
     print(f"Level {user_data['level']}")
     level = levels_data.get('levels')[user_data.get('level') - 1]
     print("Das Wort zeichnet sich durch folgende Eigenschaften aus:")
     print(f"{level.get('p1')}")
     print(f"{level.get('p2')}")
     print(f"{level.get('p3')}")
     print(f"Das Wort beginnt mit {level.get('word')[0]} und endet mit {level.get('word')[ - 1]}.")
     solution = input("Errate das Wort: ")
     if solution == level.get('word'):
      print("Richtig!")
      user_data['level'] += 1
      user.seek(0)
      user.truncate()
      json.dump(user_data, user)
     elif solution == "exit":
       print("Ciao!")
       sys.exit(0)
     else:
      print("Leider falsch. Neuer Versuch:")
    else:
     print("Du hast alle bisher verfügbaren Level gemeistert.")
     break
     sys.exit(0)
 except FileNotFoundError:
  print("Die benötigten Dateien für das Spiel sind nicht vorhanden.")
 except json.decoder.JSONDecodeError:
  print("Die Dateien sind fehlerhaft.")

if not exists("user.json"):
 create_game()
else:
 resume_game()
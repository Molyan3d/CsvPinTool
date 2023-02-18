import csv
import os

# Search for the "emotes.csv" file in the same directory as this script
emotes_file = "emotes.csv"

# credits
PACKAGE_VERSION = "\033[32m1.0\033[0m"
AUTHOR = "\033[32m@molyan & @daviwow\033[0m"
GITHUB_LINK = "\033[32mgithub.com/Molyan3d/CsvPinTool\033[0m"
COPYRIGHT_DESC = "\033[32m(c) Molyan Stars Team, 2023\033[0m"
def info(msg: str):
    print(f"\033[32m-> {msg}\033[0m")


def print_credits() -> None:
    print(f'\033[32mUltimate CSV Emote Tool - {PACKAGE_VERSION}\033[0m')
    info(f'\033[32mImplemented by {AUTHOR}\033[0m')
    info(GITHUB_LINK)
    info(COPYRIGHT_DESC)

#print credits
print_credits()

# Define the list of pin types
pin_types = ["None", "angry", "gg", "happy", "phew", "sad", "thanks", "special"]

# Display the list of pin types
print("Enter pin type (0-7):")
for i, pin_type in enumerate(pin_types):
    print(f"{i}: {pin_type}")

# Ask for user input for pin type
while True:
    try:
        pin_type = int(input("Enter pin type (0-7): "))
        if 0 <= pin_type <= 7:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 7.")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 7.")

# Ask for user input for brawler name
brawler_name = input("Enter brawler name: ")

# Add prefix "emoji_" to brawler name
brawler_name = "emoji_" + brawler_name

# Filter out duplicate character names from the "emotes.csv" file
characters = []
with open(emotes_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        character_name = row[4]
        if character_name not in characters:
            characters.append(character_name)

# Display the list of characters
print("Characters:")
for i, character_name in enumerate(characters):
    print(f"{i}: {character_name}")

# Ask for user input for character name
while True:
    try:
        character_index = int(input("Enter character relative number: "))
        if 0 <= character_index < len(characters):
            break
        else:
            print("Invalid input. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Use the selected character name as the default code name
code_name = characters[character_index]

# Define column values based on pin type
if pin_type == 1:
    suffix = "angry"
    col_8 = "0"
    col_9 = "3"
    col_10 = "0"
elif pin_type == 2:
    suffix = "gg"
    col_8 = "1"
    col_9 = "0"
    col_10 = "5"
elif pin_type == 3:
    suffix = "happy"
    col_8 = "0"
    col_9 = "1"
    col_10 = "0"
elif pin_type == 4:
    suffix = "phew"
    col_8 = "2"
    col_9 = "6"
    col_10 = "0"
elif pin_type == 5:
    suffix = "sad"
    col_8 = "0"
    col_9 = "0"
    col_10 = "0"
elif pin_type == 6:
    suffix = "thanks"
    col_8 = "0"
    col_9 = "0"
    col_10 = "0"
elif pin_type == 7:
    suffix = "special"
    col_8 = "0"
    col_9 = "0"
    col_10 = "0"
elif pin_type == 0:
    suffix = ""
    col_8 = ""
    col_9 = ""
    col_10 = ""

# Ask for user input for SC file name, code name, and export name
sc_file_name = input("Enter the SC file name (Example: ui.sc): ")
code_name = input("Enter code name (Example: Undertaker): ")
export_name = input("Enter export name (The one used in the .sc): ")

# Add prefix "sc/" to SC file name
sc_file_name = "sc/" + sc_file_name

# Create new row with column values and append to the "emotes.csv" file
new_row = [brawler_name + "_" + suffix, "", sc_file_name, export_name, code_name, "", "", col_8, col_9, col_10]
with open(emotes_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print(f"\033[1;32mThe file has been saved successfully in {os.getcwd()}.\033[0m")


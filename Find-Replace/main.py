# Transferred the catalog to a separate file
from Catalog import CATALOG

# Need to remove puncutation from the word list
import string

# Turning the name into the capital-first version
def normalize_name(name):
    return name.capitalize()

# Finding and returning all possible capitalizations
# of the name -- here I stopped at only "sentence" and
# fully upper case
def possible_names(name):
    names = []
    letters = []
    # TODO: Accommodate all versions of all names
    return [name, name.upper()]

def remove_punct(word):
    return ''.join(
        [ch for ch in word if ch not in string.punctuation]
    )

# Create global container for later variables
CHOICE = None
CHARACTERS = []

# Begin user display/interaction
print("Choose a text by number below to modify:")

# Loop through the various entries in the catalog
# with some input validation to control what can
# be selected
while True:
    ERROR_MSG = "Errors:"
    for item in CATALOG:
        print(f"{item}. {CATALOG[item]['title']}")
    choice = input("Choose a text by number: ")
    try:
        choice = int(choice)
    except ValueError:
        ERROR_MSG = f"{ERROR_MSG}\nPlease enter a number!"
    try:
        CHOICE = CATALOG[choice]
        break
    except KeyError:
        ERROR_MSG = f"{ERROR_MSG}\nThat file doesn't exist!"
    print(f"\n{ERROR_MSG}\n")

# Open the chosen file
file = open(CHOICE['filename'],"r")

# Read the file into:
# 1. A single-string version
# 2. A list of all words lower-cased
text = file.read()
words = [remove_punct(word.lower()) for word in text.split()]
# Iterate to accept user input until nothing entered;
# should implement some basic validation to be sure
# that a given character actually exists in the text
# and then (and only then) proceed to input of desired
# replacement.
while True:
    character = input("Input character name to replace: ")
    if character == "":
        break
    if not character.lower() in words:
        print("That's not a character.")
        continue
    else:
        # To handle first and last names separately
        # character = character.split()
        replace = input("Name to replace with: ")
        CHARACTERS.append(
            {
                "name": normalize_name(character),
                "replace": replace,
            }
        )

# For every replacement value entered above, iterate --
# get the versions of the name that exist; here, we're
# using Shakespeare folio editions, so it's just the two:
# 1. the standard capital-first ("sentence" case)
# 2. all-upper all the time
for replacement in CHARACTERS:
    search_names = possible_names(replacement["name"])
    replace_names = possible_names(replacement["replace"])
    for i in range(len(search_names)):
        text = text.replace(search_names[i], replace_names[i])

# Write the file
with open(f"new_{CHOICE['filename']}.txt","w") as output:
    output.write(text)

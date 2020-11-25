import random
import re

file = open("frog_and_toad.txt","r")

lines = file.readlines()

# Remove new line characters
lines = [line.replace("\n","") for line in lines]

# Replace Frog and Toad with Ulysses and G. Wiz
for line in lines:
    new_line = line.replace("Frog","Ulysses")
    new_line = new_line.replace("Toad","G. Wiz")
    print(new_line)

# Scramble text, capitalization
for line in lines:
    new_line = ""
    # Split into words by space
    words = line.split()
    # Iterate over words
    for word in words:
        new_word = word
        # This is a "regular expression": it allows us
        # to look for patterns. Here, the pattern is
        # any A-Z or a-z letter, 0-9 numbers and anything
        # which contains a single '.
        match = re.findall("[A-Za-z0-9\']+", word)
        # If we find something
        if match:
            # It will come to us in a list
            new_word = match[0]
            # Test if the first letter is uppercase
            is_capital = new_word[0].isupper()
            # Scramble the letters, join 'em back into a word
            new_word = ''.join(
                random.sample(
                    new_word.lower(), 
                    len(new_word)
                )
            )
            # If the first letter was capital, capitalize
            # the first letter of this one
            if is_capital:
                new_word = new_word.capitalize()
            line = line.replace(word, new_word)
    print(line)

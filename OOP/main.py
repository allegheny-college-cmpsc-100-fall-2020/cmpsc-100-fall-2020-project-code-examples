import Comments
from Character import PC as player_char

HAIR_COLORS = ["red","brown","black","white","gray"]
HAIR_LENGTH = ["long", "medium", "short"]

def test_input(question, options):
    value = ""
    while value not in options:
        value = input(f"{question} ")
    return value

name = input("What is your name: ")
hair_color = test_input("What is your hair color?", HAIR_COLORS)
hair_length = test_input("What length is your hair?", HAIR_LENGTH)
eye_color = input("What color are your eyes? ")
height = input("How tall are you (meters please): ")

char = player_char(
    name = name,
    hair_color = hair_color,
    hair_length = hair_length,
    eye = eye_color,
    height = height
)

print(Comments.hair_length_comment(char))
print(Comments.eye_color_comment(char))
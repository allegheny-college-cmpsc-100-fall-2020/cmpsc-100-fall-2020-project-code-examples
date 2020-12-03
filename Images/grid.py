import os

from PIL import Image, ImageDraw

files = os.listdir("squares")

files.sort()

files = [file for file in files if file.endswith(".png")]

composite = Image.new("RGBA",(300,300)) # <-- this represents the final image

files = files[0:9]

x = 0
y = 0

for square in files:
    if x % 3 == 0 and x != 0: # <-- change the 3 to however many imgs per row
        x = 0
        y += 1
    sq = Image.open(f"squares/{square}")
    print(f"Opening {square}.")
    composite.paste(sq,(x*100,y*100)) # <-- change the 100s depending on your img size
    x += 1

composite.save("composite.png")

import os

from PIL import Image, ImageDraw

files = os.listdir("squares")

files.sort()

files = [file for file in files if not file.startswith(".ipynb")]

composite = Image.new("RGB",(900,900))

#files = files[0:9]

x = 0
y = 0

for square in files:
    if x % 3 == 0 and x != 0:
        x = 0
        y += 1
    sq = Image.open(f"squares/{square}")
    print(f"Opening {square}.")
    composite.paste(sq,(x*100,y*100))
    x += 1

composite.save("composite.png")
    
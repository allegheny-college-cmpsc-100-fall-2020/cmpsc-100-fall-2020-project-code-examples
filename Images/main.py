import random

from PIL import Image, ImageDraw

def make_random_color():
    val = lambda: random.randint(0, 255)
    return (val(), val(), val())

def make_random_point(x,y):
    new_x = random.randint(0, x)
    new_y = random.randint(0, y)
    return (new_x, new_y)

# Make 10 squares of a defined size with random colors

for i in range(1,11):
    square = Image.new(
        mode = "RGB", 
        size = (100,100), 
        color = make_random_color()
    )
    square.save(f"squares/square-{i}.png")

# Create canvas

picture = Image.new(
    mode = "RGB",
    size = (1000,1000),
    color = make_random_color()
)

# Get the size of final canvas
x,y = picture.size

# Paste each of the 10 pictures in random spots

for i in range(1,11):
    to_paste = Image.open(f"squares/square-{i}.png")
    picture.paste(
        to_paste, 
        make_random_point(x, y)
    )

picture.save("final_picture.png")

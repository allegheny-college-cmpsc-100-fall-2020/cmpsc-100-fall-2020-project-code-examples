from PIL import Image, ImageDraw, ImageFont

def write_text(img, text):
    # Starting sizes
    size = 1
    x, y = img.size

    # Load type and resources
    face = "type/permanent-marker.ttf"
    font = ImageFont.truetype(face, size)

    # Get the width of text and test it against
    # 75% of the image's width (for a nice border)
    while font.getsize(text)[0] < x * .75:
        # Increment size by 1 px until it gets to
        # 75% of the image's full size
        size += 1
        font = ImageFont.truetype(face,size)

    # Get final size of type object
    type_x, type_y = font.getsize(text)

    # Center the type in the x dimension
    final_x = (x - type_x) / 2

    # Honestly, trial and error
    final_y = y - (5.5 * type_y)

    # Draw the text
    draw.text(
        (final_x, final_y),
        caption,
        fill = "black",
        font = font
    )

    picture.save("typed.png")

picture = Image.open("spring-break.png")
draw = ImageDraw.Draw(picture)

# True, tho
caption = "G. Wiz, Prof. Luman, Frogger: Spring Break 2019"

write_text(picture, caption)

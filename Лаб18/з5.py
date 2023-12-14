from PIL import Image, ImageDraw, ImageFont
import sys

try:
    image=Image.open("image1_NN.png")
except:
    print("Unable to load image")
    sys.exit(1)
image1 = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(image)
idraw.rectangle((190,350,500, 500), fill='blue')
idraw = ImageDraw.Draw(image)
text = "Маникало Полина Александровна "
font = ImageFont.truetype("arial.ttf", size=18)
idraw.text((200, 400), text, font=font)
image1.save('image5_NN.png')
image.show()
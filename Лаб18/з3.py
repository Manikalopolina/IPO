from PIL import Image
image = Image.open('jelly (1).jpg')
image1=image.crop((0,0,700,700))
image1.save('image3_NN.jpg')
image1.show()
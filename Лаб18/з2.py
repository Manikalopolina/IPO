from PIL import Image
image = Image.open('jelly (1).jpg')
image1=image.rotate(-30)
image1.save('image2_NN.jpg')
image1.show()
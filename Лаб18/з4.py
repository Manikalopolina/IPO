from PIL import Image
from PIL import ImageFilter
image = Image.open('image3_NN.jpg')
image1 = image.filter(ImageFilter.SMOOTH)
image1.save('jelly4.jpg')
image1.show()

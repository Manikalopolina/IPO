from PIL import Image
image = Image.open('jelly (1).jpg')
print('Формат изображения: ', image.format)
print('Размер изображения: ', image.size)
print('Цветовой режим изображения: ', image.mode)
image.save('image1_NN.png')
image.show()
from __future__ import print_function
from PIL import Image

img = Image.open("initial.jpeg")
img = img.rotate(-90,Image.NEAREST,expand = 1)
img = img.transpose(Image.FLIP_LEFT_RIGHT)

pixels = img.load()
width, height = img.size

image_pixels = []
for x in range(width):
    for y in range(height):
        unit = pixels[x,y]
        image_pixels.append(unit)
        ##print(*unit,sep='',end='')

luminosity = []
for x in image_pixels:
    R = x[0]
    G = x[1]
    B = x[2]
    luminosity.append(int((R + G + B)//3) )

string = "`^,:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


ascii_list = []
for x in luminosity:
    resul = int((x/255)*(len(string)-1))
    ascii_list.append(string[resul])

##print(len(ascii_list))


ascii_matrix = []
i = 0
for x in range(width):
    lista = []
    for y in range(height):
        lista.append(ascii_list[i])
        i = i+1
    ascii_matrix.append(lista)


for x in range(width):
    for y in range(height):
        print(ascii_matrix[x][y]*2,end='')

    print('')




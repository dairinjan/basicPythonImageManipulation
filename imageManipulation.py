from PIL import Image

original_image = Image.open("image.jpg")
image  = original_image.copy()


print("Format:", image.format)
print("size:", image.size)
print("mode:", image.mode)
print("width:", image.width)
print("height:", image.height)

for column in range(image.width):
  for row in range(image.height):
    coordinates = (column,row,)
    pixel = image.getpixel(coordinates)
    inverted_color = ()
    for color in pixel:
      inverted_color += (255 - color,)
    
    image.putpixel(coordinates, inverted_color)

image.save("inverted_image.jpg")

for column in range(image.width):
  for row in range(image.height): 
    coordinates = (column,row,)
    flip_coordinates = (image.width - column - 1 , row) 
    pixel            = original_image.getpixel(flip_coordinates)    
    
    image.putpixel(coordinates, pixel)

image.save("flip_image.jpg")









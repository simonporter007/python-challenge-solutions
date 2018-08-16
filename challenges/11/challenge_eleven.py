from PIL import Image
import numpy as np

# Downloaded image from challenge 9 page
img = Image.open('cave.jpg')
pm = []
for y in range(1, img.height-2, 2):
    for x in range(1, img.width-2, 2):
        pm.append(img.getpixel((x, y)))

array = np.array(pm, dtype=np.uint8)
new_img = Image.fromarray(array)
new_img.save('cave.odd.jpg', "JPEG")

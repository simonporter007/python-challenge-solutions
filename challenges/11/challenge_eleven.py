from PIL import Image
import numpy as np

# View source for hints in title
# Downloaded image from challenge 10 page
img = Image.open('cave.jpg')
pm = []
for y in range(0, img.height-2, 2):
    pm.append([img.getpixel((x,y)) for x in range(0, img.width-2, 2)])

array = np.array(pm, dtype=np.uint8)
new_img = Image.fromarray(array)
new_img.save('cave.edited.jpg', "JPEG")

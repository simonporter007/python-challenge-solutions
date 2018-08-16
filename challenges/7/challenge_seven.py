from PIL import Image

# Downloaded image from challenge 7 page
# After loading the image, we print out the pixels half way down the image (for the grey band)
# Removing the replicated pixels for each block, which is 7 pixels wide
img = Image.open('oxygen.png')
gs = [img.getpixel((x, img.height/2)) for x in range(0, img.width, 7)]
for pix in gs:
    print(chr(pix[0]), end='')

# This gives us the following array, which can be converted to letters
res = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for letter in res:
    print(chr(letter), end='')

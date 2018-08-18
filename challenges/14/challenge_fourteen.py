from PIL import Image
import numpy as np

# View source for some hints, walking around and download the "100x100" image
img = Image.open('wire.png')
data = np.asarray(img)
# Image is not 100x100 so lets create one with the data
new_img = Image.new(img.mode, (100, 100), 1)

# We start by initiating two counters
j, cnt = 0, 0
# Looping over the width of the new image (!00px), working from the end down to 0
for i in range(new_img.width, -1, -1):
    # For each counter we want to create a whole row, followed by a whole row down
    # Followed by a whole row back across, followed by a whole row up to the start
    # i.e. 100+99+99+98...
    for x in range(j, i):
        # Each time we pull pixel data from the image and add it to the new one
        # Adjusting the ranges to account for the already "filled in" rows on the spiral
        new_img.putpixel((x, j), img.getpixel((cnt, 0)))
        cnt += 1
    for y in range(j+1, i):
        new_img.putpixel(((new_img.width-1)-j, y), img.getpixel((cnt, 0)))
        cnt += 1
    for x in range(i-2, j-1, -1):
        new_img.putpixel((x, (new_img.width-1)-j), img.getpixel((cnt, 0)))
        cnt += 1
    for y in range(i-2, j, -1):
        new_img.putpixel((j, y), img.getpixel((cnt, 0)))
        cnt += 1
    # Increase the overall counter to adjust row size for the four directions
    j += 1

# Finally lets save the finished file, which gives us the final clue for the answer
new_img.save('wire.edited.png', 'PNG')

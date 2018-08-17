from imghdr import what
from os import rename
# View source for hints and follow pages to see images
# Download hidden gfx file
data = open("evil2.gfx", 'rb').read()
# The dealer is dealing into 5 piles, do the same with the data
for i in range(5):
    with open('%d' % i, 'wb') as f:
        f.write(data[i::5])
    # Find the type of file we have and rename it
    ext = what('%d' % i)
    rename('%d' % i, '%d.%s' % (i, ext))

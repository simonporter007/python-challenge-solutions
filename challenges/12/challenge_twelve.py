from magic import from_file
from base64 import b64decode
from imghdr import what
from os import rename
# View source for hints and follow pages to see images
# Last image does not display correctly, download for analysis
if not what("evil4.jpg"):
    # If not an image, what is it?
    print(from_file("evil4.jpg"))

# Reading the file looks familiar, lets get our clue
# Clue doesn't help us! Note it for later and move on.
coded_string = open("evil4.jpg", "rb").read()
print(b64decode(coded_string))

# Download hidden gfx file
data = open("evil2.gfx", 'rb').read()
# The dealer is dealing into 5 piles, do the same with the data
for i in range(5):
    with open('%d' % i, 'wb') as f:
        f.write(data[i::5])
    # Find the type of file we have and rename it
    ext = what('%d' % i)
    rename('%d' % i, '%d.%s' % (i, ext))

import re
from urllib.request import urlopen
# The source gives us the clues to click the image and tells us 400 times should be enough
# Clicking the image gives us the first number
id = 12345
for i in range(400):
    # Looping over the responses and adjusting id each time
    response = urlopen(
        'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % id)
    html = response.read()
    match = re.findall(r'the next nothing is ([0-9]+)', str(html))
    if not match:
        # until we get to a new clue, which eventually gives us the final answer
        print("nothing=%s: %s" % (id, html))
        break
    else:
        id = match[0]
    response.close()

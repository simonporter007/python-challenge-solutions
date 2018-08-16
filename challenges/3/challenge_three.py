import re

# View source and extract the text to file. We need one small surrounded by EXACTLY three large
with open('challenge_three.txt') as f:
    content = f.read()
    # Using regular expressions will be easiest here (hint in title)
    matches = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', content)
    print(''.join(matches))

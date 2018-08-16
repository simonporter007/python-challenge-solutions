import re

# View source code gives us the hint to search for rare characters and text chunk
with open('challenge_two.txt') as f:
    content = f.read()
    # Rare characters in this case would be actual letters
    answer = re.sub(r'[^A-Za-z]', '', content)
    print(answer)

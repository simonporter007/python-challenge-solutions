import zipfile
import re

comments = list()
# Viewing the source code we can see a hint for zip, checking zip.html gives a further clue
# After we have the zip downloaded, there is a readme which gives hints and first id
with zipfile.ZipFile('channel.zip') as myzip:
    id = 90052
    # So lets loop over the files, starting from our id and find the next id until the end
    for i in range(0, len(myzip.namelist())):
        with myzip.open('%s.txt' % id) as f:
            contents = f.read()
            match = re.findall(r'Next nothing is ([0-9]+)', contents)
            if not match:
                # This gives us the final hint
                print(contents)
            else:
                id = match[0]
                # With the final hint we can add this code
                z = myzip.getinfo('%s.txt' % id)
                comments.append(z.comment)
            f.close()

print(''.join(comments))

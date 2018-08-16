import gfx

# View source for hints and follow pages to see images
# Download hidden gfx file
doc = gfx.open("pdf", "evil2.gfx")
for pagenr in range(1,doc.pages+1):
    page = doc.getPage(pagenr)
    print ("Page", pagenr, "has dimensions", page.width, "x", page.height )


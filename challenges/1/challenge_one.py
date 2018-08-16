import string
# Hints on the page specify "twice" and the image shows two letter differences on the image
# The cipher is on the page
cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = 'http://www.pythonchallenge.com/pc/def/map.html'
# create our tables for maketrans, with two letter difference
ins = string.ascii_lowercase
outs = 'cdefghijklmnopqrstuvwxyzab'
print(cipher.translate(cipher.maketrans(ins, outs)))
# From the clue we can run the second translation
print(url.translate(url.maketrans(ins, outs)))

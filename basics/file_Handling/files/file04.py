# x  Create File Give Error If File Exists

################## Binary file #################
#modes
# "rb" Open for reading
# "wb" Open for writing, truncating the file first
# "ab" Open for writing ,appending to the end of the first
# "rb+" Open for reading, writing without truncating the file
# "wb+" Open for writing and reading ,truncating the file first
# "ab+" Open for appending and reading

with open("image.png","rb") as image:
    content=image.read()

with open("logo.png","wb") as logo:
    logo.write(content)


numbers=[10,20,30,40]
with open("save.bin","wb") as s:
    s.write(bytes(numbers))


with open("save.bin","rb") as s:
    print(list(s.read()))
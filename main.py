
###<--------- Extract Hide EXE --------> ###
with open('photo2.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    
    with open('newfile.exe', 'wb') as e:
        e.write(f.read())


### <----------Hide exe in an image -----------> ###
# with open('photo2.jpg', 'ab') as f, open('procexp64.exe', 'rb') as e:
#     f.write(e.read())


### <------------Extract Hide Image---------> ###
# with open('photo2.jpg', 'rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex('FFD9'))

#     f.seek(offset + 2)

#     new_img = PIL.Image.open(io.BytesIO(f.read()))
#     new_img.save("new_image.png")


##### <-------- Hide image inside an image -------> ###
# img = PIL.Image.open('zelda.png')
# byte_arr = io.BytesIO()
# img.save(byte_arr, format='PNG')
# with open('photo2.jpg', 'ab') as f:
#     f.write(byte_arr.getvalue())


### <--------- Hide information inside image ------> ###
# with open('photo2.jpg','ab') as f:
#     f.write(b"Hello World")


### <----------Retrieve hide information------------> ###
# with open('photo2.jpg', 'rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex('FFD9'))

#     f.seek(offset + 2 )
#     print(f.read())

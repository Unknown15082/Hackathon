from PIL import Image
import os
for x in os.listdir("./test/"):
    for y in os.listdir("./test/" + x):
        img = Image.open("./test/" + x + "/" + y)
        img = img.resize((64, 64))
        img.save("./DataModified/Test/%s.png" % (x + "_" + y[:-4]))
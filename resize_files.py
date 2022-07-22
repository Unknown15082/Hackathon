from PIL import Image
import os
ff = open("./DataModified/modified_labels.csv", "w+")
ff.write("Frame,Label\n")
for x in os.listdir("./image/"):
    f = [x + "_" + z for z in open("./label/" + x + ".csv", "r").read().strip().split("\n")[1:]]
    ff.write("\n".join(f) + "\n")
    for y in os.listdir("./image/" + x):
        img = Image.open("./image/" + x + "/" + y)
        img = img.resize((64, 64))
        img.save("./DataModified/Train/%s.png" % (x + "_" + y[:-4]))
ff.close()
from TemplateMatch import *
import cv2
import os
import matplotlib.pyplot as plt
from waldo import color

dir = "images"
files = os.listdir(dir)
dir1 = "template"
files1 = os.listdir(dir1)

def main(f,f1):

    i=1

    print(files,files1)

    image = cv2.imread(dir + "/" + f[i])
    template = cv2.imread(dir1 + "/" + f1[i])

    seg = color(dir + "/" + f[i])
    box = templateMatching(image, template)
    
    fig = plt.figure()
fig.add_subplot(4, 1, 1)
imgplot = plt.imshow(seg)
fig.add_subplot(4, 1, 2)
imgplot = plt.imshow(image)
fig.add_subplot(4, 1, 3)
imgplot = plt.imshow(template)
fig.add_subplot(4, 1, 4)
imgplot = plt.imshow(box)

if __name__ == '__main__':
    main(files,files1)
        

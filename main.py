from TemplateMatch import *
import cv2
import os
import matplotlib.pyplot as plt
from skimage import feature, filters, io, color
from waldo import color

dir = "images"
files = os.listdir(dir)
dir1 = "template"
files1 = os.listdir(dir1)

def main(f,f1):

    for i in range(3):

        l = [50,1000,10000]
        h = [300,20000,20000]

        print(files,files1)

        image = io.imread(dir + "/" + f[i])
        template = io.imread(dir1 + "/" + f1[i])

        seg = color(dir + "/" + f[i], l[i], h[i])
        box = templateMatching(image, template)
          
       
        
       
         
        
          
        fig = plt.figure( figsize=[15, 11])
        plt.axis('off')
        plt.imshow(box)

        fig = plt.figure( figsize=[15, 10])
        plt.axis('off')
        plt.imshow(template)

        fig = plt.figure( figsize=[15, 10])
      
        plt.axis('off')
        plt.imshow(seg)

        fig = plt.figure( figsize=[15, 10])
        plt.axis('off') 
        plt.imshow(image)

        plt.show()

if __name__ == '__main__':
    main(files,files1)
        

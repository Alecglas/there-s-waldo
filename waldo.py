import os
import matplotlib.pyplot as plt
import numpy as np
import math

from skimage import feature, filters, io, color

import cv2

dir = "images"
files = os.listdir(dir)

def color(file, l, h):
    print("new")
    img = io.imread(file)
    new=img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #plt.figure(file, figsize=[9, 9])

    hsv_red = cv2.cvtColor(np.uint8([[[255,0,0]]]),cv2.COLOR_BGR2HSV)
    r = hsv_red[0][0][0]
    print(r)
    lower_red = np.array([r-15,100,100])
    upper_red = np.array([r+15,255,255])
    lower_white = np.array([0,0,200])
    upper_white = np.array([255,50,255])


    redmask = cv2.inRange(hsv, lower_red, upper_red)
    whitemask = cv2.inRange(hsv, lower_white, upper_white)

    mask = cv2.bitwise_or(redmask, whitemask)

    res = cv2.bitwise_and(img,img, mask= mask)


    ret, thresh = cv2.threshold(whitemask,0,255,cv2.THRESH_BINARY)
    ret, thresh1 = cv2.threshold(redmask,0,255,cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
    connectivity = 4



    output = cv2.connectedComponentsWithStats(thresh2, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]

    for i in range(1, num_labels):
        if i%100 == 0:
            print(i)
        
        if stats[i][4] > l and stats[i][4] < h:
            pts = np.where(labels == i)
            labels[pts] = -1

    res[labels != -1] = (0,0,0)
    
    return res

if __name__ == '__main__':
    for file in files:
        color(dir + "/" + file)
        plt.savefig("processed/" + file)




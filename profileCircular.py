import cv2 
import numpy as np

image = cv2.imread('imgs/profile.jpeg')

def rescale(frame,scale=0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = width,height

    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)

resize_image = rescale(image)

blank = np.zeros(resize_image.shape[:2],dtype='uint8')

circle = cv2.circle(blank,(resize_image.shape[1]//2,resize_image.shape[0]//2),100,255,-1)

masked = cv2.bitwise_and(resize_image,resize_image,mask=circle)

cv2.imshow("Resized",masked)
cv2.waitKey(0)
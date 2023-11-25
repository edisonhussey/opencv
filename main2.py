import cv2 
import numpy as np


import math

#image=cv2.imread("/Users/edisonhussey/Desktop/computingCoursework/map1.png")
image =np.zeros((500,500,3),dtype=np.uint8)


#image[100,100]=[140,140,0]
centre=[250,250]
distance=0
for i in range(500):
    for j in range(500):
        distance=((i-250)**2+(j-250)**2)**(1/2)
        print(distance)
        image[i,j]=[distance%255,distance%255,distance%255]

        #image[i,j]=[30-int(distance/200),140-int(distance/200),255-int(distance/200)]

    
        #image[i,j]=[125,125,(i+j)%250]
        #if i<100 :
         #   image[i,j]=[140,140,0]
        #else:
        #    image[i,j]=[0,255,0]

#for i in range(100):
#    image[100,i]=[140,140,0]
cv2.imshow('Modified Image',image)

cv2.waitKey(0)

cv2.destroyAllWindows()

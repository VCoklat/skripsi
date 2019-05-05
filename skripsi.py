import cv2
import numpy as np

  
image = cv2.imread('test.jpg')
#grayscaling
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#thresholding
retval, threshold = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

#closing
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

#connectedlabels
ret, labels = cv2.connectedComponents(closing)

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()

imshow_components(labels)  
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
#cv2.imshow('threshold',threshold)
#cv2.imshow('threshold',closing)  

#cv2.waitKey(0)
#cv2.destroyAllWindows()

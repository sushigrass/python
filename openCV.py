import cv2
import numpy as np
import matplotlib.pyplot at plt

img = cv2.imread('pic.jpg',cv2.IMREAD_GRAYSCALE)

'''cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

ptl.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

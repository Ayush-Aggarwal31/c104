import cv2

img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
texttoshow="I LIKE DOGGOS"
cv2.putText(img,texttoshow,(20,220),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,255))
cv2.imshow("c104",img)
cv2.waitKey(10000)
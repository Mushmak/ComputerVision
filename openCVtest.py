# import openCv library 
import cv2 

#read image/video feed
image =cv2.imread("D:\\k\\ViolaJones\\unnamed.jpg")
greyImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # set img to gray scale 


# create cascade classifier 
# i got the haarcascades from their github repo
face_cascade = cv2.CascadeClassifier("D:\\k\\ViolaJones\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml")


# face rectange co-ordinates 

face = face_cascade.detectMultiScale(greyImg,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in face:
    image = cv2.rectangle (image, (x,y), (x+w, y+h),(0,255,0),3)


# display face box 
resizeImg = cv2.resize(image,(450,500)) # resize image 
cv2.imshow("test",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

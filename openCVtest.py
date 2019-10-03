
# import openCv library 
import cv2 
'''
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
'''
# reading video 
cap = cv2.VideoCapture(0)
# create cascade classifier 
# i got the haarcascades from their github repo
face_cascade = cv2.CascadeClassifier("D:\\k\\ViolaJones\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml")

if (cap.isOpened()==False):
    print("error")

while True:
    ret, pic = cap.read()
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY) #convert to gray 
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
    # create rectangle 
    for x,y,w,h in face:
        cv2.rectangle (pic, (x,y), (x+w, y+h),(255,0,0),3)

    #display image 
    cv2.imshow("feed",pic) 
    
    key = cv2.waitKey(1)
    #breaks loop so we can close window 
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
    
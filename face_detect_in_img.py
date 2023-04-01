import cv2
image=cv2.imread('ff2.jfif')
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
haar_face_cascade = cv2.CascadeClassifier ("D:\python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
faces=haar_face_cascade.detectMultiScale (gray, scaleFactor=1.1, minNeighbors=5)
#print ("Faces Found", len(faces))
for x,y,w,h in faces:
    image = cv2.rectangle(image,(x,y),(x+w,y+h), (255, 0, 0), 2)
cv2.imshow("Gray", image)
cv2.waitKey(0)
cv2.destroyAllWindows ()

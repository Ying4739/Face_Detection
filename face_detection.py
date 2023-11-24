import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#  Capture camera
cap = cv2.VideoCapture(0)
while True:
    # Read the frame
    _, img = cap.read()
# Turn into gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect the face
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    i=1
# Draw the rectangle of the detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        crop_img=img[y:y+h, x:x+w]
        cv2.imwrite("people"+str(i)+".png", crop_img) 
        i = i + 1

    cv2.namedWindow('Human Face Found!', cv2.WINDOW_NORMAL) # Normal window size
    cv2.imshow('Human Face Found!', img )# Show the image
    
    if cv2.waitKey(30)== ord('s'):
        cv2.imwrite("saved.png",img)
    if cv2.waitKey(30)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

print(faces)
print('HumanFace{0} Detected !'.format(len(faces)))
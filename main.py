import cv2
from random import randrange

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_detector = cv2.CascadeClassifier('haarcascade_mouth.xml')

webcam = cv2.VideoCapture(0)

while True:
    
    successful_frame_read, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_detector.detectMultiScale(grayscaled_frame)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # using numpy to slice to array
        the_face = frame[y:y+h, x:x+w]
        
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)
        
        eyes = eye_detector.detectMultiScale(face_grayscale, scaleFactor=1.1, minNeighbors=10)
        
        mouth = mouth_detector.detectMultiScale(face_grayscale, scaleFactor=1.2, minNeighbors=15)
        
        # for (x_, y_, w_, h_) in smiles:
        #     cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 3)
        
        if len(smiles) > 0:
            cv2.putText(frame, 'Smiling', (x, y+h+40), fontScale=2, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))
    
        for (x_, y_, w_, h_) in eyes:
            cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (255, 255, 255), 2)
            
        for (x_, y_, w_, h_) in mouth:
            cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (255, 0, 0), 2)
        
    cv2.imshow('Clever Smile Detector', frame)

    
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

webcam.release()
cv2.destroyAllWindows()

print("Code Completed")

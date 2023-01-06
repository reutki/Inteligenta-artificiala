#Plates number detector:

import cv2
#taking the file to decode the numbers
carPlatesCascade = cv2.CascadeClassifier('plates.xml')
#starting the webcam
cap = cv2.VideoCapture(0)
#setting the window size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#if the webcam does not start, you get an error
if (cap.isOpened() == False):
    print('Error Reading Camera')
#if it starts, when you show the mubers, it opens a frame window and filters it by grayscaling it
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car_plates = carPlatesCascade.detectMultiScale(gray, scaleFactor=1.2,
                                                   minNeighbors=5, minSize=(25, 25))
#creates the rectangle and frame's color
    for (x, y, w, h) in car_plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
    if ret == True:
        cv2.imshow('Video', frame)
#if you press 'q' the script will stop.
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
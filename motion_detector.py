import cv2
import time
from datetime import datetime as dt

def fps_cal(now):
    #calculating fps
    then = now
    now = dt.now()
    now_s = now.second + now.microsecond/1000000
    then_s = then.second + then.microsecond/1000000
    diff = (now_s - then_s)
    try:
        fps = float(1/diff)
        print('fps is :',fps,"      now : {}      then : {}".format(now_s, then_s))
    except:
        pass
    return now

def motion_detection(img):
    #image detection
    #creating a casscade object
    face_casscade = cv2.CascadeClassifier(r"D:\Code\Python\Practice\170 Files\haarcascade_frontalface_default.xml") #cascade xml file is input

    #searching image to find coordinates to face
    face = face_casscade.detectMultiScale(img, scaleFactor=1.08, minNeighbors=10)

    return face

def image_conversion(first_frame, gray):
    delta_frame = cv2.absdiff(first_frame, gray)
    thres_hold = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thres_hold = cv2.dilate(thres_hold, None, iterations=2)
    (cnts,_) = cv2.findContours(thres_hold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("hreshold", thres_hold)

    faces = []
    for contour in cnts:
        if cv2.contourArea(contour) < 100:
            continue
        else:
            faces.append(cv2.boundingRect(contour))
            # cv2.imshow("capturing", contour)

    return faces

################################################################################
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fps = 0
now = dt.now()

first_frame = None
arr = []

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # faces = image_conversion(first_frame, gray)
    faces = motion_detection(gray)
    if faces is ():
        print("no")
    else:
        print("yes")

    #drawing rectangle on image
    for x,y,w,h in faces:
        img_1 = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("capturing", img_1)

    now = fps_cal(now)  #finding fps right after new frame

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# demo of camera filter program using OpenCV
# second commit
# third commit 
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

filter = "preview"
_,frame = cap.read()
feature_params = dict(
    maxCorners=1000,
    qualityLevel=0.3,
    minDistance=15,
    blockSize=15
)
while _:
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if(filter == 'preview'):
        res = frame
    elif(filter == 'blur'):
        res = cv2.GaussianBlur(frame,(17,17),0)
    elif(filter == 'canny'):
        res = cv2.Canny(gray,40,140)
    elif(filter == 'feature'):
        corner = cv2.goodFeaturesToTrack(gray,100,0.2,15,blockSize=9)
        if(corner is not None):
            res = frame
            for x,y in np.float32(corner).reshape(-1,2):
                cv2.circle(res,(int(x),int(y)),10,(0,255,0),3)
        print(corner)
    cv2.imshow("FEED",res)

    k = cv2.waitKey(1)
    if(k==27):
        break
    elif(k == ord('P')):
        filter = "preview"
    elif(k == ord('B')):
        filter = 'blur'
    elif(k == ord('C')):
        filter = "canny"
    elif (k == ord('F')):
        filter = "feature"
    _,frame = cap.read()

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np


def call(x):
    pass

cap = cv2.VideoCapture(0)
ret,frame = cap.read()
frame = cv2.flip(frame,1)
cv2.namedWindow('frame')
# cv2.createTrackbar('LH','frame',0,255,call)
# cv2.createTrackbar('UH','frame',255,255,call)
# cv2.createTrackbar('LS','frame',0,255,call)
# cv2.createTrackbar('US','frame',255,255,call)
# cv2.createTrackbar('LV','frame',0,255,call)
# cv2.createTrackbar('UV','frame',255,255,call)
while ret:

    cv2.imshow("feed",frame)

    ret,frame = cap.read()
    framehsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # frame = cv2.GaussianBlur(frame,(11,11),0)
    # lh = cv2.getTrackbarPos('LH','frame')
    # uh = cv2.getTrackbarPos('UH', 'frame')
    # ls = cv2.getTrackbarPos('LS', 'frame')
    # us = cv2.getTrackbarPos('US', 'frame')
    # lv = cv2.getTrackbarPos('LV', 'frame')
    # uv = cv2.getTrackbarPos('UV', 'frame')
    l_b = np.array([0,173,165])
    u_b = np.array([255,255,255])
    msk = cv2.inRange(framehsv,l_b,u_b)
    # msk = cv2.threshold(msk,200,255,cv2.THRESH_BINARY)
    msk = cv2.dilate(msk,(21,21),iterations=3)
    cnt,hier = cv2.findContours(msk,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for i in cnt:
        if(cv2.contourArea(i) < 300):
            continue
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,0),5)
        # cv2.drawContours(frame, i, -1, (255, 0, 0), 3)

    andop = cv2.bitwise_and(frame,frame,mask=msk)
    orr = cv2.bitwise_or(frame,frame,mask=msk)
    cv2.imshow("frame", andop)
    cv2.imshow("msk", msk)
    frame = cv2.flip(frame,1)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import mediapipe
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)

video = cv2.VideoCapture(0)

while True:
    fingerUp1=[0,0,0,0,0]
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)

    if hands:
        #hand1
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        #print(fingerUp)

        # hand2
        if len(hands)==2:
            lmList1=hands[1]
            fingerUp1=detector.fingersUp(lmList1)

            #print(fingerUp + fingerUp1)




        List3=0
        for i in range(0,5):
            List3 = List3+fingerUp[i] + fingerUp1[i]
        if fingerUp is not None or fingerup1 is not None:
            cv2.putText(frame,str(List3),(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

        #cnt.led(List3)

    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()

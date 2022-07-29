import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)
#cap3 = cv2.VideoCapture(2)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outDown.avi', fourcc, 20.0, (640, 480))

fourcc2 = cv2.VideoWriter_fourcc(*'XVID')
out2 = cv2.VideoWriter('outFR.avi', fourcc2, 20.0, (640, 480))

fourcc3 = cv2.VideoWriter_fourcc(*'XVID')
out3 = cv2.VideoWriter('outFL.avi', fourcc3, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    #ret2, frame2 = cap2.read()
    #ret3, frame3 = cap3.read()
    if ret==True:

        print('a')
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('b')
        break

    # if ret2==True:
    #
    #     print('c')
    #     out2.write(frame2)
    #
    #     cv2.imshow('frame2',frame2)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         print('d')
    #         break
    # else:
    #     print('e')
    #     break
    #
    # if ret3==True:
    #
    #     print('f')
    #     out3.write(frame3)
    #
    #     cv2.imshow('frame3',frame3)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         print('g')
    #         break
    # else:
    #     print('h')
    #     break

# Release everything if job is finished
cap.release()
#cap2.release()
#cap3.release()
out.release()
out2.release()
out3.release()
cv2.destroyAllWindows()
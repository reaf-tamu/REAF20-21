import cv2
import pyzed.sl as sl
import numpy as np
import serial.tools.list_ports

# def main():
#     print("Running...")
#     init = sl.InitParameters()
#     cam = sl.Camera()
#     if not cam.is_opened():
#         print("Opening ZED Camera...")
#     status = cam.open(init)
#     if status != sl.ERROR_CODE.SUCCESS:
#         print(repr(status))
#         exit()
#     runtime = sl.RuntimeParameters()
#     mat = sl.Mat()

#     key = ''
#     while key != 113:  # for 'q' key
#         err = cam.grab(runtime)
#         if err == sl.ERROR_CODE.SUCCESS:
#             cam.retrieve_image(mat, sl.VIEW.LEFT)
#             cap = mat.get_data()
#             cv2.imshow("ZED", cap)
#             key = cv2.waitKey(5)
#             #settings(key, cam, runtime, mat)
#         else:
#             key = cv2.waitKey(5)
#     cv2.destroyAllWindows()

#     cam.close()
#     print("\nFINISH")

# if __name__ == "__main__":
#     main()


cap = cv2.VideoCapture(1)
while(1):
    # Take each frame
    _, frame = cap.read()
    image = np.split(frame, 2, axis=1)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_orange = np.array([5,150,150])
    upper_orange = np.array([15,255,255])

    # Threshold the HSV image to get only orange colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)


    #Addition of Rectangle Detector
    font = cv2.FONT_HERSHEY_COMPLEX
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
    contours, hierarchy= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (255, 255, 255), 2)
            if len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (255, 255, 255))

#End  of Rectangle Detector

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',image[0])
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

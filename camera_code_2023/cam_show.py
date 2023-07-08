import cv2			#Import the cv2 library to gather camera images

cap = cv2.VideoCapture(0)	#Set the camera to record using the default camera


while True: 		#To show camera feed continuously, use an infinite while loop
    ret,img=cap.read()		#Capture the video frame by frame
    cv2.imshow('Video', img)	# Display the resulting frame
			#The frequency of images being captured is every 1ms using the waitKey()
    			#If an image is taken AND q is pressed, the while loop will break and end the program
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break


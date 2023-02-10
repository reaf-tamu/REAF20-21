from __future__ import print_function
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import cv2

vs = VideoStream(src=1).start()
fps = FPS().start()

while fps._numFrames < 15:
	pass

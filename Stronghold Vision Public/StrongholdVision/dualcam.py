import cv2
#import cv2.cv as cv
from time import sleep
from multiprocessing import Process as pProcess

#ALL IMPORTS STATEMENTS SHOULD BE ABOVE THIS LINE
#BEGIN CODE

global running
running = True


def cameraCall(windowName, cameraNumber, imageWidth, imageHeight):
	running = True
	cv2.namedWindow(windowName)
	camera = cv2.VideoCapture(cameraNumber)
	while running:
		if True:
			keyValue = cv2.waitKey(5) & 0xFF
			
			if keyValue == ord('q'):
				camera.release()
				print "quiting " + windowName
				running = False
				sleep(0.2)
				break
			elif keyValue == ord('r'):
				print "redoing camera " + windowName
				camera.release()
				sleep(0.3)
				camera = cv2.VideoCapture(cameraNumber)
			ret, frame = camera.read()
			display = cv2.resize(frame,(imageWidth,imageHeight))
			cv2.imshow(windowName, display)
	camera.release()
	running = False
	
	
if __name__ == '__main__':
  pass
  camera1 = pProcess(target=cameraCall, args=("CAM1", 1, 320, 240))
  camera1.start()
  camera0 = pProcess(target=cameraCall, args=("CAM0", 0, 320, 240))
  camera0.start()
  camera1.join(3)
  camera0.join(3)



import cv2
import numpy as np
import pyautogui
SCREEN_SIZE=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output.avi", fourcc,20.0,(SCREEN_SIZE))
while True:
	img= pyautogui.screenshot()
	frame=np.array(img)
	frame =cv2.cvtColor(frame,cv2.COLOR_BGR2EGB)
	out.write(frame)
	if cv2.waitkey(1)==ord("q"):
		break
cv2.distroyAllWindows()
out.release()


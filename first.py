'''this is a demo on video capture in python '''
import cv2 
'''this will open our video camera '''
cap = cv2.VideoCapture(0)

while True :
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 

cap.release()
cv2.destroyAllWindows()

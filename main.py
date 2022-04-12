import cv2

UserFP=input("Enter Filepath: ")
Flag=input("Enter Image Flag: ")
img=cv2.imread(UserFP, int(Flag))
cv2.imshow("My Activity", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#myactivity4
        

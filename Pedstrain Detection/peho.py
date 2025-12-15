import cv2


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


img = cv2.imread('i/p11.jpeg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


pedestrians, _ = hog.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.05)

# Draw a rectangle around each pedestrian
for (x, y, w, h) in pedestrians:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with the detected pedestrians
cv2.imshow('Pedestrians', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

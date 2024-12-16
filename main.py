import cv2

test_img = cv2.imread("test.jpg")
gray_img = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)

number_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_russian_plate_number.xml")

num_plates = number_cascade.detectMultiScale(gray_img,1.2,5)

for (x,y,w,h) in num_plates:
    cv2.rectangle(test_img,(x,y), (x+w, y+h) , (0,255,0), 2)

cv2.imshow("Test image",test_img)
cv2.waitKey(0)
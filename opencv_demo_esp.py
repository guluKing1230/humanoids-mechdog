import cv2
import urllib.request
import numpy as np

url = 'http://192.168.1.129:80/capture'  # ESP32-CAM IP

cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)  

while True:
    img_resp = urllib.request.urlopen(url) 
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8) 
    img = cv2.imdecode(imgnp, -1) 

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    canny = cv2.Canny(cv2.GaussianBlur(gray, (11, 11), 0), 30, 150, 3)  
    dilated = cv2.dilate(canny, (1, 1), iterations=2)
    (contours, _) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  
    k = img
    cv2.drawContours(k, contours, -1, (0, 255, 0), 2)

    cv2.imshow("mit contour", canny) 

    cv2.imshow("live transmission", img) 
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

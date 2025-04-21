import cv2
import urllib.request
import numpy as np

url = 'http://192.168.1.129:80/capture'  # Replace with your ESP32-CAM IP

cv2.namedWindow("Color Detection", cv2.WINDOW_AUTOSIZE)  

# Define HSV range for a specific color (e.g., red)
# You can change these values for different colors
lower = np.array([0, 120, 70])     # Lower bound for red
upper = np.array([10, 255, 255])   # Upper bound for red

while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a mask for the selected color
    mask = cv2.inRange(hsv, lower, upper)

    # Remove small blobs/noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = img.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # filter out small contours
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(output, "Color Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36,255,12), 2)

    cv2.imshow("Mask", mask)
    cv2.imshow("Color Detection", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

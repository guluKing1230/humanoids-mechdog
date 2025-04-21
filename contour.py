import cv2
import torch
import time
from yolov5 import YOLOv5
import urllib.request
import numpy as np

url = 'http://192.168.1.129:80/capture'  # ESP32-CAM IP addr

# Load the YOLOv5 model
model_path = "yolov5s.pt"  
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = YOLOv5(model_path, device=device)

while True:
    img_resp = urllib.request.urlopen(url)  
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8) 
    frame = cv2.imdecode(imgnp, -1)  

    start_time = time.time()

    results = model.predict(frame, size=640)  

    annotated_frame = results.render()  

    end_time = time.time()

    processing_time = end_time - start_time
    fps = 1 / processing_time

    cv2.putText(annotated_frame[0], f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("YOLOv5 Detection", annotated_frame[0])

    print(f"Processed frame in {processing_time:.4f} seconds, FPS: {fps:.2f}")


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

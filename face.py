import Hiwonder
import time
import Hiwonder_IIC
from HW_MechDog import MechDog


iic2 = Hiwonder_IIC.IIC(2)
cam = Hiwonder_IIC.ESP32S3Cam(iic2)
mechdog = MechDog()
time.sleep(1)

# face recognition
while True:
  ret = cam.face_recognition()
  if ret:
    mechdog.action_run("scrape_a_bow")
    time.sleep(5)
  time.sleep(0.1)


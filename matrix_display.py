import Hiwonder
import time
import Hiwonder_IIC
from HW_MechDog import MechDog

mechdog = MechDog()
tm = Hiwonder.Digitaltube()
i2c1 = Hiwonder_IIC.IIC(1)
i2csonar = Hiwonder_IIC.I2CSonar(i2c1)

mechdog.set_default_pose()
tm.setBrightness(4)
time.sleep(1)

distance = 0

def main():
  global distance

  while True:
    distance = i2csonar.getDistance()
    tm.showNum(distance)
    if (distance<15):
      i2csonar.setRGB(0,0xff,0x00,0x00)
    else:
      if (distance>40):
        i2csonar.setRGB(0,0x00,0x00,0x99)
      else:
        i2csonar.setRGB(0,0xfd,0xd0,0x00)
    time.sleep(0.1)


main()

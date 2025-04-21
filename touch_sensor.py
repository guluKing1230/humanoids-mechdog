import Hiwonder
import time
from HW_MechDog import MechDog

# Initialization
mechdog = MechDog()
enter_flag = 0
action_num = 0
button2 = Hiwonder.Button(2)


mechdog.set_default_pose()
time.sleep(1)

def main():
  global enter_flag
  global action_num

  while True:
    if (enter_flag==1):
      if (action_num==1):
        # if touched once: sit down
        mechdog.action_run("sit_dowm")
        time.sleep(1.5)
        action_num+=1
      elif (action_num==2):
        # second time: go prone
        mechdog.action_run("go_prone")
        time.sleep(1.5)
        action_num+=1
      else:
        # next: stand
        mechdog.action_run("stand_four_legs")
        time.sleep(1.5)
        action_num = 1
      # reset the flag
      enter_flag = 0
    else:
      time.sleep(0.2)

def on_extbutton_clicked():
  global enter_flag
  enter_flag = 1


button2.Clicked(on_extbutton_clicked)

main()

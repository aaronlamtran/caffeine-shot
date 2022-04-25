import pyautogui, time
while(True):
  pyautogui.moveRel(50, 0, 2)
  pyautogui.moveRel(0, 50, 2)
  pyautogui.moveRel(-50, 0, 2)
  pyautogui.moveRel(0, -50, 2)
  time.sleep(1)
  print('loop')
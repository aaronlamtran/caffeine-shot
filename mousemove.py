import pyautogui, time
while(True):
  pyautogui.moveRel(9, 50, duration=1)
  pyautogui.moveTo(100, 200, 2)
  pyautogui.moveTo(0, 500, 2 )
  pyautogui.moveTo(600, 0, 2)
  time.sleep(1)
  print('loop')
import pyautogui, time

currentTime = time.asctime()
print(f'Caffiene shot servered at {currentTime}! \nPress Ctrl-C to quit')
while(True):
  pyautogui.moveRel(50, 0, 2)
  pyautogui.moveRel(-50, 0, 2)
  time.sleep(5)
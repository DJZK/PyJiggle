import time

import pyautogui

# Endless Loop
while True:
    # First round
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 2, y + 2)
    time.sleep(1)

    # Second Round
    x, y = pyautogui.position()
    pyautogui.moveTo(x - 2, y - 2)
    time.sleep(1)

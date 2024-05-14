import numpy as np
import mss
import time
import webbrowser
import pyautogui
import cv2

def open_close():
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed")

# Load and resize the template image
facebook = cv2.imread('facebook.jpg')
facebook = cv2.resize(facebook, (150, 150))  # Resize to match the region size

sct = mss.mss()

dimensions = {
    'left': 340,
    'top': 500,
    'width': 150,
    'height': 150
}

while True:
    scr = np.array(sct.grab(dimensions))
    scr_remove = scr[:,:,:3]
    result = cv2.matchTemplate(scr_remove, facebook, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    open_close()

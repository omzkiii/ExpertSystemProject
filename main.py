import numpy, mss
import time,webbrowser, pyautogui, cv2

def open_close():
    time.sleep(20)
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed")
facebook = cv2.imread('facebook.jpg')
sct = mss.mss()

dimensions = {
        'left': 340,
        'top': 500,
        'width': 150,
        'height': 150
    }

while True:
    scr = numpy.array(sct.grab(dimensions))
    scr_remove = scr[:,:,:3]
    result = cv2.matchTemplate(scr_remove, facebook, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    open_close()
    # print(facebook)

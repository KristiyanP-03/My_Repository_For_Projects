import keyboard
import time
import pyautogui

autoclicker_active = False

def toggle_autoclicker():
    global autoclicker_active
    autoclicker_active = not autoclicker_active
    if autoclicker_active:
        print("Autoclicker activated!")
        autoclicker_loop()
    else:
        print("Autoclicker deactivated!")

def autoclicker_loop():
    while autoclicker_active:
        pyautogui.click()
        time.sleep(0.1)

keyboard.on_press_key('f', lambda _: toggle_autoclicker())

while True:
    pass
import pyautogui
import keyboard
#Left: 3286, Top: 305, Width: 92, Height: 7

LIFE_REGION = (3288, 304, 92, 4)
MANA_REGION = (3288, 315, 92, 4)
COR_LIFE = (218, 79, 79)
COR_MANA = (54, 51, 166)
WIDTH = 92

def calcular_life_mana(percent):
    return int(WIDTH * percent / 100)

def color_check(region, percent, color):
    result_percent = calcular_life_mana(percent)
    x = region[0] + result_percent
    y = region[1] + region[3]
    return pyautogui.pixelMatchesColor(int(x), int(y), color, 10)

def usar_suplies(event):
    while not event.is_set():
        if not color_check(LIFE_REGION, 40, COR_LIFE):
            pyautogui.press('F1')
        if event.is_set():
            return
        else:
            if not color_check(LIFE_REGION, 80, COR_LIFE):
                pyautogui.press('F3')
            if not color_check(MANA_REGION, 65, COR_MANA):
                pyautogui.press('Space')
            if event.is_set():
                return

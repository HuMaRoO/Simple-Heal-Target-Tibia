import pyautogui
import keyboard
import time
import threading

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
    return pyautogui.pixelMatchesColor(int(x), int(y), color, tolerance=10)

def usar_supplies(event):
    while not event.is_set():
        try:
            if not color_check(LIFE_REGION, 40, COR_LIFE):
                pyautogui.press('F1')
                time.sleep(0.5)
            
            elif not color_check(LIFE_REGION, 65, COR_LIFE):
                pyautogui.press('1')
                time.sleep(0.5)
            
            elif not color_check(LIFE_REGION, 85, COR_LIFE):
                pyautogui.press('2')
                time.sleep(0.5)
            
            if not color_check(MANA_REGION, 55, COR_MANA):
                pyautogui.press('Space')
                time.sleep(0.5)
            
            time.sleep(0.1)
        
        except Exception:
            time.sleep(1)
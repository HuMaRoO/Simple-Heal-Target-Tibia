import pynput
import pyautogui
pyautogui.useImageNotFoundException(False)
import threading
from loot import get_loot
from life_mana import usar_suplies

LIST_HOTKEY_ATK = [{"hotkey": "F5", "delay": 1.5}, {"hotkey": "F6", "delay": 1.5}, {"hotkey": "F7", "delay": 1.5}, {"hotkey": "F8", "delay": 1.5}]
BATTLE = (3091, 347, 166, 54)

def rotacao():
        while not event_rotacao.is_set():
            for attack in LIST_HOTKEY_ATK:
                if event_rotacao.is_set():
                    return
                if pyautogui.locateOnScreen('battle.png', confidence=0.9, region=BATTLE):
                    continue
                pyautogui.press(attack["hotkey"])
                pyautogui.sleep(attack["delay"])

def execute_hotkey(hotkey):
    pyautogui.press(hotkey)

run_bot = False
def key_press(key):
    global run_bot
    if key == pynput.keyboard.Key.delete:
        print("Kill bot") 
        return False
    
        
    if hasattr(key, 'char') and key.char == 'x':
        if run_bot == False:
            run_bot = True
            global th_rotacao, th_suplies, event_rotacao, event_suplies
            event_suplies = threading.Event()
            th_suplies = threading.Thread(target=usar_suplies, args=(event_suplies,))
            th_rotacao = threading.Thread(target=rotacao)
            event_rotacao = threading.Event()
            print("Start Rotacao")
            for hotkey in LIST_HOTKEY_ATK:
                execute_hotkey(hotkey)
            th_rotacao.start()
            th_suplies.start()
        else:
            run_bot = False
            event_rotacao.set()
            event_suplies.set()
            th_suplies.join()  
            th_rotacao.join()
            print("Stop Rotacao")
    
    if hasattr(key, 'char') and key.char == 'r':
        print('Looting') 
        get_loot()

with pynput.keyboard.Listener(on_press=key_press) as listener:
    listener.join()
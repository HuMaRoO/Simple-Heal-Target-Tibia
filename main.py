import pynput
import pyautogui
pyautogui.useImageNotFoundException(False)
import threading
from life_mana import usar_suplies

LIST_HOTKEY_ATK = [{"hotkey": "F5", "delay": 1.5}, {"hotkey": "F6", "delay": 1.5}, {"hotkey": "F7", "delay": 1.5}, {"hotkey": "F8", "delay": 1.5}]
BATTLE = (3091, 347, 166, 54)

def rotacao():
    global event_rotacao
    while not event_rotacao.is_set():
        for hotkey in LIST_HOTKEY_ATK:
            if event_rotacao.is_set():
                return
            else:
                execute_hotkey(hotkey["hotkey"])
                pyautogui.sleep(hotkey["delay"])


def execute_hotkey(hotkey):
    pyautogui.press(hotkey)


run_bot = False
def create_listener():
    def key_press(key):
        global run_bot
        if key == pynput.keyboard.Key.delete:
            print("Kill bot") 
            listener.stop()

    listener = pynput.keyboard.Listener(on_press=key_press)
    listener.start()

create_listener()
    
#ROTACOES
event_rotacao = threading.Event()
th_rotacao = None
def key_press(key):
    global run_bot, event_rotacao, th_rotacao
    if hasattr(key, 'char') and key.char == 'c':
        if run_bot == False:
            run_bot = True
            th_rotacao = threading.Thread(target=rotacao)
            th_rotacao.start()
            print("Start Rotacao")
        else:
            run_bot = False
            event_rotacao.set()
            if th_rotacao is not None:
                th_rotacao.join()
            print("Stop Rotacao")
    
    if hasattr(key, 'char') and key.char == 'x':
        if run_bot == False:
            run_bot = True
            global th_suplies, event_supplies
            event_supplies = threading.Event()
            th_suplies = threading.Thread(target=usar_suplies, args=(event_supplies,))
            th_suplies.start()
            print("Start Supplies")
        else:
            run_bot = False
            event_supplies.set()
            th_suplies.join()
            print("Stop Supplies")

#--------------------------------------MODELOS ANTIGOS--------------------------------------
"""def rotacao():
        while not event_rotacao.is_set():
            for attack in LIST_HOTKEY_ATK:
                if event_rotacao.is_set():
                    return
                if pyautogui.locateOnScreen('battle.png', confidence=0.9, region=BATTLE):
                    continue
                pyautogui.press(attack["hotkey"]) x
                pyautogui.sleep(attack["delay"])"""

"""    if hasattr(key, 'char') and key.char == 'x':
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
        get_loot()"""

with pynput.keyboard.Listener(on_press=key_press) as listener:
    listener.join()
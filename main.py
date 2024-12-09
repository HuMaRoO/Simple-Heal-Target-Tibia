import threading
import pyautogui
from pynput import keyboard
from life_mana import usar_supplies

# Constantes
LIST_HOTKEY_ATK = [
    {"hotkey": "F5", "delay": 2},
    {"hotkey": "F6", "delay": 2},
    {"hotkey": "F7", "delay": 2},
    {"hotkey": "F8", "delay": 2}
]

# Variáveis globais
rotacao_ativa = False
supplies_ativo = False
event_rotacao = threading.Event()
event_supplies = threading.Event()
th_rotacao = None
th_supplies = None


def execute_hotkey(hotkey):
    pyautogui.press(hotkey)

def rotacao():
    while not event_rotacao.is_set():
        for hotkey in LIST_HOTKEY_ATK:
            if event_rotacao.is_set():
                break
            execute_hotkey(hotkey["hotkey"])
            pyautogui.sleep(hotkey["delay"])

def on_press(key):
    global rotacao_ativa, supplies_ativo, th_rotacao, th_supplies, event_rotacao, event_supplies

    if key == keyboard.Key.delete:
        if rotacao_ativa:
            event_rotacao.set()
        if supplies_ativo:
            event_supplies.set()
        return False
    
    try:
        if key.char == '0':
            if not rotacao_ativa:
                event_rotacao.clear()
                th_rotacao = threading.Thread(target=rotacao)
                th_rotacao.start()
                rotacao_ativa = True
                print("Rotação iniciada")
            else:
                event_rotacao.set()
                rotacao_ativa = False
                print("Rotação parada")

        elif key.char == '-':
            if not supplies_ativo:
                event_supplies.clear()
                th_supplies = threading.Thread(target=usar_supplies, args=(event_supplies,))
                th_supplies.start()
                supplies_ativo = True
                print("Supplies iniciado")
            else:
                event_supplies.set()
                supplies_ativo = False
                print("Supplies parado")

    except AttributeError:
        pass

# Iniciar o listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Manter o programa rodando
listener.join()
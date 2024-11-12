import pyautogui
import random

LIST_POS = [(1451, 563), (1547, 526), (1617, 525), (1633, 633), (1633, 688), (1545, 698), (1455, 719), (1437, 625), (1518, 615)]
random.shuffle(LIST_POS)

def get_loot():
    for position in LIST_POS:
        pyautogui.moveTo(position)
        pyautogui.click(button="right")
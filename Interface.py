from tkinter import *
from tkinter.ttk import Label, Combobox, Checkbutton
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyautogui
from window import hidden_client
import subprocess

# Window Inicial #
root = tk.Tk()
root.title("Interface")
root.geometry("250x80")
root.resizable(False, False)

style = ttk.Style()
style.configure('TNotebook.Tab', padding=[10, 5]) #Adicao de padding entre as abas
style.configure('TNotebook.Tab', margin=[5, 2]) #Adicao da margem 
#style.configure('Custom.TButton', font=("Arial",15)) #Modelo Custom dos itens

menuBarra = ttk.Notebook(root)
menuBarra.grid(row=0, column=2, sticky="N")

aba1 = ttk.Frame(menuBarra)
menuBarra.add(aba1, text="Main")
aba2 = ttk.Frame(menuBarra)
menuBarra.add(aba2, text="Healing")

button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=3, sticky="NE", padx=5, pady=5)
btn_start_stop = ttk.Button(button_frame, text="Start")#style="Custom.TButton"
btn_start_stop.grid(row=0, column=3, sticky="E")

def opacity():
    result = hidden_client()
    if result == 1:
        print('Aplicado')
        return
    print('Nao Aplicado')

btn_opacity = ttk.Button(aba1, text="Aplicar Opacity", command=opacity)
btn_opacity.pack(pady=5)

"""lbl_life = ttk.Label(aba2, text="Life %")
lbl_life.grid(row=0, column=1)
lbl_mana = ttk.Label(aba2, text="Mana %")
lbl_mana.grid(row=1, column=1)
cmb_life = ttk.Combobox(aba2, width=3, values=["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
cmb_life.grid(row=0, column=2)
cmb_mana = ttk.Combobox(aba2, width=3, values=["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
cmb_mana.grid(row=1, column=2)"""

process = None

def start():
    global process
    process = subprocess.Popen(["python", "main.py"])
    btn_start_stop.config(text="Stop", command=stop)

def stop():
    global process
    if process:
        process.terminate()
        process = None
    pyautogui.press('delete')
    btn_start_stop.config(text="Start", command=start)


btn_start_stop.config(command=start)


root.mainloop()
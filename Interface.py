import tkinter as tk
from tkinter import ttk
import subprocess
import pyautogui
import ctypes
import pygetwindow as gw

#Constants da Janela
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

# Main Window 
root = tk.Tk()
root.title("Interface")
root.geometry("300x150")
root.resizable(False, False)

style = ttk.Style()
style.configure('TNotebook.Tab', padding=[10, 5])

menuBarra = ttk.Notebook(root)
menuBarra.grid(row=0, column=2, sticky="N")

aba1 = ttk.Frame(menuBarra)
menuBarra.add(aba1, text="Main")

lbl_window_title = ttk.Label(aba1, text="Nome Janela:")
lbl_window_title.pack(pady=(10,0))

entry_window_title = ttk.Entry(aba1, width=20)
entry_window_title.pack(pady=5)


current_window_title = "Tibia -"
process = None

def apply_opacity():
    global current_window_title
    
    if entry_window_title.get():
        current_window_title = entry_window_title.get()
    
    try:
        target_window = gw.getWindowsWithTitle(current_window_title)[0]
        
        if target_window is not None:
            target_hwnd = target_window._hWnd

            ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
            ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)

            ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, 1, LWA_ALPHA)
            
            print(f"Opacity aplicada: {current_window_title}")
        else:
            print("Window not found.")
    except Exception as e:
        print(f"Error opacity: {e}")

btn_opacity = ttk.Button(aba1, text="Aplicar Opacity", command=apply_opacity)
btn_opacity.pack(pady=10)

"""lbl_life = ttk.Label(aba2, text="Life %")
lbl_life.grid(row=0, column=1)
lbl_mana = ttk.Label(aba2, text="Mana %")
lbl_mana.grid(row=1, column=1)
cmb_life = ttk.Combobox(aba2, width=3, values=["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
cmb_life.grid(row=0, column=2)
cmb_mana = ttk.Combobox(aba2, width=3, values=["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
cmb_mana.grid(row=1, column=2)"""

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

button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=3, sticky="NE", padx=5, pady=5)

btn_start_stop = ttk.Button(button_frame, text="Start")
btn_start_stop.grid(row=0, column=3, sticky="E")
btn_start_stop.config(command=start)

root.mainloop()




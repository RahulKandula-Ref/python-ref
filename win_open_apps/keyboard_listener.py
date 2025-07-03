from pynput import keyboard
import tkinter as tk

root = None

def open():
    print('start')
    root.mainloop()

def close():
    print('destroying')


def init_root():
    global root
    root = tk.Tk()

    # prep it
    root.title('Open Applications')
    root.attributes('-alpha', 0.7)
    root.attributes('-topmost', True)
    
    # position it
    width = 400
    height = 400
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    screen_x = (screen_w / 2) - (width / 2)
    screen_y = (screen_h / 2) - (height / 2)
    root.geometry(f"{width}x{height}+{int(screen_x)}+{int(screen_y)}")

init_root()

with keyboard.Listener(on_press=open, on_release=close) as listener:
    listener.join()
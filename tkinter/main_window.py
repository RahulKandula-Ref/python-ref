import tkinter as tk


def show_open_apps():
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


    root.mainloop()


if __name__ == "__main__":
    show_open_apps()
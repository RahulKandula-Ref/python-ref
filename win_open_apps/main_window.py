import tkinter as tk

def main():
    root = tk.Tk()

    def setup_window():
        # prep it
        root.title(' ')
        root.attributes('-alpha', 0.9)
        root.attributes('-topmost', True)
        
        # position it
        width = 400
        height = 400
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        screen_x = (screen_w / 2) - (width / 2)
        screen_y = (screen_h / 2) - (height / 2)
        root.geometry(f"{width}x{height}+{int(screen_x)}+{int(screen_y)}")

    def close_everything(event):
        root.quit()

    def populate_open_apps_info():
        test_label = tk.Label(root, text="1 - Google Chrome", fg="red", font=("Arial", 18, "bold"), bg="white")
        test_label.pack(pady=10)
        test_label2 = tk.Label(root, text="2 - Eclipse", fg="red", font=("Arial", 18, "bold"), bg="white")
        test_label2.pack(pady=10)

    # do the init process
    setup_window()
    populate_open_apps_info()

    # bind keyboard events
    root.bind("<KeyPress>", close_everything)
    root.bind("<KeyRelease>", close_everything)
    
    # start the loop
    root.mainloop()



if __name__ == "__main__":
    main()
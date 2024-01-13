import tkinter as tk
root = tk.Tk()

root.image = tk.PhotoImage(file='crosshair.png')
label = tk.Label(root, image=root.image, bg='white')
label = tk.Label(root, image=root.image, bg='white', width=-100, height=-100)
root.overrideredirect(True)
root.geometry(f"+623+333")
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()
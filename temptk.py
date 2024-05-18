import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

# Create a grid of widgets
for r in range(3):
    root.rowconfigure(r, weight=1)
    for c in range(3):
        root.columnconfigure(c, weight=1)
        tk.Button(root, text=f'Button {r},{c}').grid(row=r, column=c,sticky='news')

root.mainloop()

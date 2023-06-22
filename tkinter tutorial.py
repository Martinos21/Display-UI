import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.title("Demo")
window.geometry("900x600")


title_label = ttk.Label(master = window, text="", font = "Calibri 24 bold" )
title_label.pack()


output_label = tk.Label(master = window, text = "ahoj", font = "Calibri 24 bold")
output_label.place (x=10,y=10 )



window.mainloop()

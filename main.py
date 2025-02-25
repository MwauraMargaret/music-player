import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Musiki Player")
canvas.geometry("600x800")
canvas.config(bg='black')

rootpath= "C:\\Users\Waithera\Music\Muziki"
pattern = "*mp3"

listBox = tk.Listbox(canvas, fg = "Cyan", bg ="black", width = 100, font = ('DS-Digital', 14))
listBox.pack(padx = 15, pady = 15)

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end', filename)  

canvas.mainloop()
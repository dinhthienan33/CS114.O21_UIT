import csv
import os
import time
from PIL import Image, ImageTk
import tkinter as tk

with open('2.csv','r') as f:
    reader = csv.reader(f)
    data = [row[0] for row in reader]

path='cs114.o21.x.lab01-competition'
for name in data[80:]:
    full_path = os.path.join(path, name)
    if os.path.isfile(full_path):
        window = tk.Tk()

        img = Image.open(full_path)
        img_resized = img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(img_resized)

        label = tk.Label(window, image=tk_img)
        label.pack()

        window.after(1500, lambda: window.destroy())  
        window.mainloop()
    else:
        print(f"File {full_path} does not exist.")
import tkinter as tk
from PIL import Image, ImageTk

#starting of program

root = tk.Tk()

image_path = ("Homepage.png")
image_path = Image.open(image_path)
image_path = image_path.resize((500, 500), Image.LANCZOS)
image_path = ImageTk.PhotoImage(image_path)

label = tk.Label(root, image=image_path)
label.pack()

root.title("General Knowledge Quiz")
root.mainloop()

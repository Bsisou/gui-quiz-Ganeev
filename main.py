import tkinter as tk
from PIL import Image, ImageTk

#Create Tkinter Object

root = tk.Tk()

#Read The Image
image_path = ("Homepage.png")
image = Image.open(image_path)


#Resize The Image
width = 1920
height = 1080
resize_image = image.resize((width, height))

img = ImageTk.PhotoImage(resize_image)

#Add Image To Label
label1 = tk.Label(root, image=img)
label1.image = img
label1.pack()

#Execute Tkinter

root.title("General Knowledge Quiz")
root.mainloop()

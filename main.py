import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from PIL import Image, ImageTk

names_list = []

class quizStarter:
    def __init__(self, parent):
      background_color = "slategray1"

      #Canvas setup to add the widgets on top of the Image like the button
      self.canvas = tk.Canvas(parent, bg=background_color, width=960, height=540)
      self.canvas.pack()

      #Adding the image to the canvas
      image_path = "Homepage.png"
      self.image = Image.open(image_path)
      self.resized_image = self.image.resize((960,540))
      self.img = ImageTk.PhotoImage(self.resized_image)
      self.canvas.create_image(0, 0, anchor='nw', 
image=self.img)

    
      #Entry widget for my user name
      self.entry_box = Entry(parent, bg="slategray1")
      self.entry_box_window = self.canvas.create_window(480, 455, anchor='center', window=self.entry_box)

      #Next button to proceed onto the next page
      self.next_button = Button(parent, text = "Next", bg = "slategray1", command=self.name_collection)
      self.next_button_window = self.canvas.create_window(750, 455, anchor='center', window=self.next_button)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.canvas.destroy()
    

#Create Tkinter Object
root = tk.Tk()

# Create QuizStarter object
quiz_starter_object = quizStarter(root)

#Execute Tkinter
if __name__ == "__main__":
 root.title("General Knowledge Quiz")
 root.mainloop()

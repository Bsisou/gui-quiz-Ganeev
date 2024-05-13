import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from PIL import Image, ImageTk

names_list = []

class quizStarter:
#Init fuction is used each time the class is being used to create a new object
    def __init__(self, parent):
      background_color = "slategray1"

      
      #Frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
      self.quiz_frame.grid()

      #Label widget for my heading
      self.heading_label = Label(self.quiz_frame, text = "Welcome to the quiz", 
 bg=background_color) 
      self.heading_label.grid(row=0, pady=20)

      #Label for username
      self.user_label = Label (self.quiz_frame, text = "Please enter your name below", bg=background_color)
      self.user_label.grid(row=1, pady=20)

      #Label widget for my user name
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, pady=20)

      #Next button
      self.next_button = Button(self.quiz_frame, text = "Next", bg = "blue", command=self.name_collection)
      self.next_button.grid(row=3, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()
    

#Create Tkinter Object
root = tk.Tk()


#Read The Image
image_path = ("Homepage.png")
image = Image.open(image_path)


#Resize The Image
width = 960
height = 540
resize_image = image.resize((width, height))


img = ImageTk.PhotoImage(resize_image)

#Add Image To Label
label1 = tk.Label(root, image=img)
label1.image = img
label1.pack()

next_button = tk.Button(root, text="Next")
next_button.place(x=100, y=200)


#Execute Tkinter
if __name__ == "__main__":
 root.title("General Knowledge Quiz")
 #root = tk.Tk()
 #quizStarter_object = quizStarter(root)
 root.mainloop()

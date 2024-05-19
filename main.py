import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from PIL import Image, ImageTk

names_list = []

class quizStarter:
    def __init__(self, parent):
      self.parent = parent
      self.background_color = "slategray1"
      self.create_homepage_canvas()
    def create_homepage_canvas(self):

      #Canvas setup to add the widgets on top of the Image like the button
      self.canvas = tk.Canvas(self.parent, bg=self.background_color, width=960, height=540)
      self.canvas.pack()

      #Adding the image to the canvas
      image_path = "Homepage.png"
      self.image = Image.open(image_path)
      self.resized_image = self.image.resize((960,540))
      self.img = ImageTk.PhotoImage(self.resized_image)
      self.canvas.create_image(0, 0, anchor='nw', 
image=self.img)

    
      #Entry widget for my user name
      self.entry_box = Entry(self.parent, bg="slategray1", width=27, font=("Arial", 10), bd=1, relief="groove", justify="center",)
      self.entry_box_window = self.canvas.create_window(480, 455, anchor='center', window=self.entry_box)

      #Next button to proceed onto the next page
      self.next_button = Button(self.parent, text = "Next", bg = "slategray1", command=self.name_collection, font=("Arial", 12, "bold"), height=2, width=15, highlightbackground="royalblue1", highlightthickness=5)
      self.next_button_window = self.canvas.create_window(750, 435, anchor='center', window=self.next_button)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.continue_to_the_question_page()
   
    def continue_to_the_question_page(self):
        self.canvas.destroy()

      #Create a new canvas to continue to the questioning and answeering page
        self.next_canvas = tk.Canvas(self.parent, bg="slategray1", width=960, height=540)
        self.next_canvas.pack()

      #Adding a new image to the next questioning page
        next_image_path = "Questionpage.png"
        self.next_image = Image.open(next_image_path)
        self.resized_next_image = self.next_image.resize((960,540))
        self.next_img = ImageTk.PhotoImage(self.resized_next_image) 
        self.next_canvas.create_image(0, 0, anchor='nw', image=self.next_img)

      #Added a back button to go back to the homepage
        self.back_button = Button(self.next_canvas, text='Back', bg="slategray1", command=self.go_back, font=("Arial", 12, "bold"), height=2, width=15, highlightbackground="royalblue1", highlightthickness=5) 
        self.back_button_window = self.next_canvas.create_window(750, 435, anchor='center', window=self.back_button)

      #Creating a label for the question page
        self.next_label = Label(self.next_canvas, text="Question page", bg="slategray1", font=("Arial", 20, "bold"))
        self.next_label_window = self.next_canvas.create_window(130, 30, anchor="center", window=self.next_label)

    def go_back(self):
        self.next_canvas.destroy()
        self.create_homepage_canvas()
    
#Create Tkinter Object
root = tk.Tk()

# Create QuizStarter object
quiz_starter_object = quizStarter(root)

#Execute Tkinter
if __name__ == "__main__":
 root.title("General Knowledge Quiz")
 root.mainloop()

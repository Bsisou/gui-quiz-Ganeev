import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from PIL import Image, ImageTk
import random


username_list = []
request = []

class Questions:
    def __init__(self, parent):
  
      questions_dictionary = {
           1:["How many bones does do sharks have?:", '0', '237', '123', '50', 1],
           2:["What is the distance from Earth to the Sun?:" , '9.2 million km', '93 million km', '149 million km', '259 million km', '2'],
           3:["What is the coldest place on earth?:", 'Iceland', 'Greenland', 'Antarctica', 'Finland', 3],
           4:["Which travels faster, light or sound?:", 'Light', 'Sound', 'Both', 'Neither', 1],
           5:["How many minutes are in a full week?:", '27000', '10080', '14400', '43200', 2],
           6:["Which planet has the most moons?:", 'Jupitar', 'Earth', 'Neptune', 'Saturn', 4],
           7:["What is the world's smallest country?:"," 'Monaco', 'Maldives', 'Vatican City', 'San Marino", 3],
           8:["Who won the last FIFA Worldcup in 2022?:", 'Argentina', 'France', 'Croatia', 'Portugal', 1],
           9:["What is the heighest grossing film of all time?:", 'Titanic', 'Avatar', 'Avengers Endgame', 'Fast And Furious 7', 3], 
          10:["Who invented the light bulb?:", 'Isaac Newton', 'Nikola Tesla', 'Thomas Edison', 'Albert Einstein', 3]
           
      }

      # self.questions_frame = Frame(parent)
      # self.questions_frame.grid()

      # self.question_label = Label(self.questions_frame, text = questions_dictionary[1][0])
      # self.question_label.grid(row = 1, column = 1)
  
    def random_quesion():
        global gKQQnum
        gKQQnum = random.randint(1,10)
        if gKQQnum not in request:
          request.append(gKQQnum)
        elif gKQQnum in request:
         random_quesion()
    
class QuizStarter:
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
      self.next_button = Button(self.parent, text = "Next", bg = "slategray1", command=self.home_page, font=("Arial", 12, "bold"), height=2, width=15, highlightbackground="royalblue1", highlightthickness=5)
      self.next_button_window = self.canvas.create_window(750, 435, anchor='center', window=self.next_button)

    def home_page(self):
        name = self.entry_box.get()
        username_list.append(name)
        print(username_list)
        self.continue_to_the_question_page()
   
    def continue_to_the_question_page(self):
        self.canvas.destroy()
        quiz_starter_object = QuizStarter(self.parent)

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


#Execute Tkinter
if __name__ == "__main__":
  #Create Tkinter Object
 GKQ = tk.Tk()
 GKQ.title("General Knowledge Quiz")
  # Create QuizStarter object
 quiz_starter_object = QuizStarter(GKQ)
 GKQ.mainloop()

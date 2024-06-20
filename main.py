import tkinter as tk
from tkinter import DISABLED, Frame, Label, Entry, Button, Radiobutton, IntVar
from typing import final
from PIL import Image, ImageTk
import random

username_list = []
request = []

    #creates the first page
class QuizStarter:
    def __init__(self, parent):
        self.parent = parent
        self.background_color = "slategray1"

    # Activate the score
        self.score = 0
    # List to store incorrect questions and their correct answers
        self.incorrect_questions = []
        self.incorrect_answers = []

    # Storage for labels to be created on the Questions page
        self.questions_dictionary = {
            1: ["How many bones do sharks have?:", '0', '237', '123', '50', 1],
            2: ["What is the distance from Earth to the Sun?:", '9.2 million km', '93 million km', '149 million km', '259 million km', 2],
            3: ["What is the coldest place on earth?:", 'Iceland', 'Greenland', 'Antarctica', 'Finland', 3],
            4: ["Which travels faster, light or sound?:", 'Light', 'Sound', 'Both', 'Neither', 1],
            5: ["How many minutes are in a full week?:", '27000', '10080', '14400', '43200', 2],
            6: ["Which planet has the most moons?:", 'Jupiter', 'Earth', 'Neptune', 'Saturn', 4],
            7: ["What is the world's smallest country?:", 'Monaco', 'Maldives', 'Vatican City', 'San Marino', 3],
            8: ["Who won the last FIFA Worldcup in 2022?:", 'Argentina', 'France', 'Croatia', 'Portugal', 1],
            9: ["What is the highest grossing film of all time?:", 'Titanic', 'Avatar', 'Avengers Endgame', 'Fast And Furious 7', 3],
            10: ["Who invented the light bulb?:", 'Isaac Newton', 'Nikola Tesla', 'Thomas Edison', 'Albert Einstein', 3]
        }

        self.current_question_index = 0
    #To keep the current question widgets
        self.question_widgets = []

        self.create_homepage_canvas()

    def create_homepage_canvas(self):
    #Canvas setup to add the widgets on top of the Image like the button
        self.canvas = tk.Canvas(self.parent, bg=self.background_color, width=960, height=540)
        self.canvas.pack()

    # Adding the image to the canvas
        image_path = "Homepage.png"
        self.image = Image.open(image_path)
        self.resized_image = self.image.resize((960, 540))
        self.img = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)

    # Entry widget for the username
        self.entry_box = Entry(self.parent, bg="slategray1", width=27, font=("Arial", 10), bd=1, relief="groove", justify="center")
        self.entry_box_window = self.canvas.create_window(480, 455, anchor='center', window=self.entry_box)

    # Next button to proceed onto the next page
        self.next_button = Button(self.parent, text="Next", bg="slategray1", command=self.home_page, font=("Arial", 12, "bold"), height=2, width=15, highlightbackground="royalblue1", highlightthickness=5)
        self.next_button_window = self.canvas.create_window(750, 435, anchor='center', window=self.next_button)

    def home_page(self):
        name = self.entry_box.get()
    # Make sure the name entry box is not empty before the user proceeds 

        if name:
            username_list.append(name)
            self.continue_to_the_question_page()
        else:
            error_label = Label(self.canvas, text="Please enter your name to proceed!", font=("Arial", 12, "bold"), bg="slategray1", fg="black")
            self.canvas.create_window(480, 485, anchor='center', window=error_label)

    #this to continue to the question page
    def continue_to_the_question_page(self):
        self.canvas.destroy()
    #Questions_object = Questions(self.parent)

    #Create a new canvas to continue to the questioning and answeering page
        self.next_canvas = tk.Canvas(self.parent, bg="slategray1", width=960, height=540)
        self.next_canvas.pack()

    # Adding a new image to the next questioning page
        next_image_path = "Questionpage.png"
        self.next_image = Image.open(next_image_path)
        self.resized_next_image = self.next_image.resize((960, 540))
        self.next_img = ImageTk.PhotoImage(self.resized_next_image)
        self.next_canvas.create_image(0, 0, anchor='nw', image=self.next_img)

    # Added a back button to go back to the homepage
        self.back_button = Button(self.next_canvas, text='Back', bg="slategray1", command=self.go_back, font=("Arial", 12, "bold"), height=2, width=15, highlightbackground="royalblue1", highlightthickness=5)
        self.back_button_window = self.next_canvas.create_window(110, 440, anchor='center', window=self.back_button)

    # Creating a label for the question page
        self.next_label = Label(self.next_canvas, text="Question page", bg="slategray1", font=("Arial", 20, "bold"))
        self.next_label_window = self.next_canvas.create_window(130, 30, anchor="center", window=self.next_label)

        self.load_next_question()

    def load_next_question(self):
    #Get rid of the previous question widgets
        for widget in self.question_widgets:
            widget.destroy()
        self.question_widgets.clear()
    
    # Get the current question from the questions dictionary
        if self.current_question_index < 10:
            self.current_question_index += 1
            question_num = self.current_question_index
            question_data = self.questions_dictionary[question_num]
            self.display_question(question_data, question_num)

    #Create label for the quiz questions
    def display_question(self, question_data, question_num):
        question_label_text = question_data[0]
        question_label = Label(self.next_canvas, text=question_label_text, font=("Arial", 10, "bold"), bg="slategray1", fg="black",)
        question_label.place(x=360, y=80)
   
    # Create radio buttons for the answer options    
        self.question_widgets.append(question_label)
        self.create_option_buttons(question_data, question_num)
    def create_option_buttons(self, question_data, question_num):
        options = question_data[1:5]
        correct_option = question_data[5]
        self.var1 = IntVar()
        self.radio_buttons = []

    # Place my 4 answer option button in a square format
        positions = [(350, 380), (350, 435), (530, 380), (530, 435)]
        for i, option in enumerate(options):
            rb = Radiobutton(self.next_canvas, text=option, bg="slategray1", font=("Arial", 12, "bold"), value=i+1, variable=self.var1, pady=10, highlightbackground="royalblue1", highlightthickness=5)
            x, y = positions[i]
            rb.place(x=x, y=y)
            self.radio_buttons.append(rb)
            self.question_widgets.append(rb)

    # Create the confirm button outside of the loop to go the next question
        self.confirm_button = Button(self.next_canvas, text="Confirm", bg="slategray1", font=("Arial", 12, "bold",), highlightbackground="royalblue1", highlightthickness=5, command=lambda: self.check_answer(self.var1.get(), correct_option, question_num))
        self.confirm_button.place(x=450, y=490)
        self.question_widgets.append(self.confirm_button)

    #Disable the confirm button so that the user doesn't accidentaly skip the question
    def check_answer(self, selected, correct, question_num):
        self.confirm_button.config(state=DISABLED)
        selected_rb = None
        for rb in self.radio_buttons:
            if rb.cget('value') == selected:
                selected_rb = rb
                break
    
    #Letting the users know if the answer they picked is correct or incorrect
        if selected == correct:
            selected_rb.config(text="Correct!", bg="green")
    
    #Each answer the user gets right is 1 point added to their score
            self.score += 1
        else:
            selected_rb.config(text="Incorrect!", bg="red")
            correct_answer = self.questions_dictionary[question_num][correct]
            self.incorrect_answers.append((self.questions_dictionary[question_num][0], correct_answer))
    
    #Proceed to the next question automatically after a delay
        self.parent.after(2000, self.load_next_question)

    #Create a function to display a final message saying the quiz is completed
    def show_final_message(self):
        for widget in self.next_canvas.winfo_children():
          widget.destroy()
        final_message = Label(self.next_canvas, text="General Knowledge Quiz Completed!", bg="slategray1", font=("Arial", 20, "bold"))
        final_message.place(x=450, y=270, anchor="center")

    #Next button to go to the final page where score is displayed
        self.next_button = Button(self.next_canvas, text="Next", bg="slategray1", command=self.show_final_message, font=("Arial", 12, "bold"), height=2, width=15, highlightbackground="royalblue1", highlightthickness=5)
        self.next_button.place(x=400, y=300)

    def go_back(self):
        self.next_canvas.destroy()
        self.create_homepage_canvas()
    
    #Exceute tkinter
if __name__ == "__main__":
    #Create Tkinter object
    gKQ = tk.Tk()
    gKQ.title("General Knowledge Quiz")
    #Create Quizstarter object
    quiz_starter_object = QuizStarter(gKQ)
    gKQ.mainloop() 
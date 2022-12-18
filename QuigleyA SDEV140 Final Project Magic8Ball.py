"""
File: magicgui.py
Description: lays out framing of Magic 8-ball program GUI,
"""

import tkinter as tk
import random


def get_question():
    """Asks user for their question."""
    header_label["text"] = "Your efforts will be rewarded. \n" \
                           "What is your question?"
    question_field["state"] = "normal"      # unlocks question field for user entry
    question_field.delete(0, tk.END)        # clears question field of any previous values
    question_field["relief"] = "groove"
    yes_btn["text"] = "I am ready"
    yes_btn["command"] = check_question     # checks if question field was left blank
    no_btn["text"] = ""
    no_btn["state"] = "disabled"            # turns no/exit button off
    no_btn["relief"] = "flat"               # makes no/exit button invisible


def check_question():
    """Checks whether a question was entered. If not, displays error message and
    does not allow user to proceed until something is entered into the question field."""
    if len(question_field.get()) == 0:      # if question_field is blank
        answer_line["text"] = "Question field cannot be blank."
        get_question()                      # sends user back to question form
    else:
        return_answer()                     # allows user to proceed to get an answer


def return_answer():
    """Returns randomly selected answer to user."""
    header_label["text"] = "The universe answered: "
    question_field["state"] = "disabled"    # locks question field from user entry

    """Randomly selects a response from a list of potential answers to user's question."""
    random_num = random.randint(1, 5)
    if random_num == 1:
        answer_line["text"] = "Absolutely not."
    elif random_num == 2:
        answer_line["text"] = "Ask me again later."
    elif random_num == 3:
        answer_line["text"] = "Slip me some cookies \n(the digital chip kind) \nand then we'll talk..."
    elif random_num == 4:
        answer_line["text"] = "I need to sleep on it."
    else:
        answer_line["text"] = "It is most likely."

    yes_btn["text"] = "I have more \nquestions"
    yes_btn["command"] = get_question           # sends user back to question form
    no_btn["text"] = "I am satisfied"
    no_btn["state"] = "normal"                  # turns no/exit button back on
    no_btn["command"] = finished                # sends user back to farewell screen
    no_btn["relief"] = "raised"


def finished():
    """Displays farewell screen"""
    tk.imageLabel = tk.Label(master=win, text="Image of the Universe", compound="none")
    tk.image = tk.PhotoImage(file="universe.gif")   # shows image of the universe
    eight_ball["image"] = tk.image          # displays image
    header_label["text"] = "\nGo and be well."
    question_field.delete(0, tk.END)        # clears question field of any previous values
    question_field["relief"] = "flat"       # makes question_field invisible
    question_field["state"] = "disabled"    # locks question_field from user entry
    answer_line["text"] = " "               # clears answer_line of any previous values
    answer_line["relief"] = "flat"          # makes answer_line field invisible
    yes_btn["text"] = " "
    yes_btn["state"] = "disabled"           # turns yes/proceed button off
    yes_btn["relief"] = "flat"              # makes yes/proceed button invisible
    no_btn["text"] = "Exit program"
    no_btn["relief"] = "raised"
    no_btn["command"] = quit                # closes program


# window
win = tk.Tk()                               # initiates window
win.title("Magic 8 Ball")                   # initiates window title

# entry frames
form_entry = tk.Frame(master=win)           # initiates image frame
eight_ball = tk.Label(master=win, text="", relief="flat")
eight_ball.grid(row=0, column=0, columnspan=2)

# image label
imageLabel = tk.Label(master=win, text="Magic 8-Ball", compound="none")     # sets alt text
tk.image = tk.PhotoImage(file="eight_ball.gif")
eight_ball["image"] = tk.image              # attaches image

# initiates header label, question field, answer line
header_label = tk.Label(master=win, text="Do you seek wisdom?", relief="flat")
header_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
question_field = tk.Entry(master=win, state="readonly", relief="flat")
question_field.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
answer_line = tk.Label(master=win, relief="flat")
answer_line.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# buttons
yes_btn = tk.Button(master=win, text="I must learn", relief="raised", command=get_question)
yes_btn.grid(row=4, column=0, padx=20, pady=10)
no_btn = tk.Button(master=win, text="I am content", relief="raised", command=finished)
no_btn.grid(row=4, column=1, padx=20, pady=10)

win.mainloop()

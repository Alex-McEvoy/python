#Dawson chapter 10 challenge 2
#04/29/17

# create the GUI with a title, label for guess, entry box for the user's number
from tkinter import *

class Guess_your_number(Frame):
    """Creates a GUI application that tries to guess a number your thinking of"""

    def __init__(self,master):
        """Initialize the master frame"""

        super(Guess_your_number, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        """Create widgets to display text, select range, accept input and reset the game"""

        #create title
        Label(self,
              text = 'Please select the range\n for your number'
              ).grid(row = 0, column = 0)

        #create radio buttons for the guess range
        self.range = StringVar()
        self.range.set(50)

        ranges = [10, 50, 100, 150]
        row = 1
        for number in ranges:
            Radiobutton(self,
                        text = '1-{}'.format(number),
                        value = number,
                        variable = self.range
                        ).grid(row = row, column = 0, sticky = W)
            row += 1

        #create the text box to display output
        self.display = Text(self, width = 35, height = 8, wrap = WORD)
        self.display.grid(row = 1, column = 1, rowspan = 4, sticky = E)

        #create the submit button which will process user input
        self.submit_button = Button(self, text = 'Submit', command = self.check_answer)
        self.submit_button.grid(row = 5, column = 0, sticky = W)

        #user entry button
        self.user_entry = Entry(self)
        self.user_entry.grid(row = 5, column = 1, sticky = W)

        #resets the program
        self.reset_button = Button(self, text = 'Reset', command = self.reset_game)
        self.reset_button.grid(row = 6, column = 0, sticky = W)

        #closes the program
        self.quit_button = Button(self, text = "Quit", command = self.master.destroy)
        self.quit_button.grid(row = 7, column = 0, sticky = W)

    def check_answer(self):
        """Checks for one of three possible inputs and updates computers guess"""

        if self.user_entry.get().lower() != 'yes':
            answer = self.user_entry.get().lower()

            if answer == 'higher':
                self.lower_limit = self.guess
            elif answer == 'lower':
                self.upper_limit = self.guess
            else:
                self.display.insert(END, "Sorry, I didn't get what you said. Please respond with higher, lower, or yes\n")

            self.make_guess(self.upper_limit, self.lower_limit)
            self.display.see(END)
        else:
            self.display.insert(END, "Hooray, we got it!!\n")
            self.display.insert(END, "Hit reset to play again or quit to exit.\n")
            self.display.see(END)


    def reset_game(self):
        """Resets the game"""

        self.display.delete(0.0, END)
        self.lower_limit = 1
        self.upper_limit = int(self.range.get())
        self.display.insert(0.0, "Please think of a number between 1 and {} and I will try to guess it.\n\n"\
                            .format(int(self.range.get())))
        self.make_guess(self.upper_limit, self.lower_limit)

    def make_guess(self, upper_limit, lower_limit):
        """Generates our programs guess"""

        self.guess = int((upper_limit + lower_limit) // 2)  # use floor division to avoid floating point numbers
        self.display.insert(END, "Is your number {}?\n\n".format(self.guess))


#main
root = Tk()
root.title("Let me guess your number")
game = Guess_your_number(root)
root.mainloop()

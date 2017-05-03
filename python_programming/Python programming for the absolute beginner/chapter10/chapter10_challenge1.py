from tkinter import *

class Mad_lib(Frame):
    """Class to create mad lib program"""
    def __init__(self, master):
        super(Mad_lib, self).__init__(master)
        self.grid()
        self.make_widgets()

    def make_widgets(self):
        """Creates mad lib widgets"""

        Label(self,
              text = 'Welcome to a really dumb mad-lib.',
              ).grid(row = 0, column = 0, columnspan = 5)

        Label(self,
              text = 'Please select one or more of the following words...',
              ).grid(row = 1, column = 0, columnspan = 5)

        self.is_crazy = BooleanVar()
        Checkbutton(self,
                    text = 'Crazy',
                    variable = self.is_crazy
                    ).grid(row = 2, column = 0)

        self.is_weird = BooleanVar()
        Checkbutton(self,
                    text = 'Weird',
                    variable = self.is_weird
                    ).grid(row = 2, column = 1)

        self.is_cranky = BooleanVar()
        Checkbutton(self,
                    variable = self.is_cranky,
                    text = 'Cranky'
                    ).grid(row = 2, column = 2)

        self.is_stupid = BooleanVar()
        Checkbutton(self,
                    text = 'Stupid',
                    variable = self.is_stupid
                    ).grid(row = 2, column = 3)

        Label(self,
              text = 'Please select from the following words.'
              ).grid(row = 3, column = 0, columnspan = 5)

        self.location = StringVar()
        self.location.set(None)

        rad_buttons = ['farm', 'ranch', 'beach', 'factory', 'photo-booth']
        for column, word in enumerate(rad_buttons):
            Radiobutton(self,
                        text = word,
                        variable = self.location,
                        value = word,
                        ).grid(row = 4, column = 0 + column)
        Label(self,
              text = "Plural Animals: "
              ).grid(row = 5, column = 0, sticky = W)

        self.animal = Entry(self)
        self.animal.grid(row = 5, column = 1)

        Label(self,
              text = "Sound: "
              ).grid(row = 6, column = 0, sticky = W)

        self.sound = Entry(self)
        self.sound.grid(row = 6, column = 1)

        Button(self,
               text = 'Tell story',
               command = self.tell_story
               ).grid(row = 7, column = 0, sticky = W)
        
        self.display = Text(self,
                            width = 75, height = 10, wrap = WORD)
        self.display.grid(row = 8, column = 0, columnspan = 4)

    def tell_story(self):
        """Fill in a story based on user input"""

        #get values from GUI
        adjectives = ''
        adjective_list = {'crazy':self.is_crazy.get(),\
                               'weird': self.is_weird.get(),\
                               'cranky': self.is_cranky.get(),\
                               'stupid':self.is_stupid.get()}
        for key, value in adjective_list.items():
            if value:
                adjectives += ', ' + key

        location = self.location.get()

        animal = self.animal.get()
        sound = self.sound.get()

        #create the story

        story = 'Old' + adjectives + ' McDonald'
        story += ' had a ' + location + '\n'
        story += 'E-I-E-I-O\n'
        story += 'and on that ' + location + ' he had some ' + animal + '\n'
        story += 'E-I-E-I-O\n'
        story += 'with a ' + sound + ' ' + sound + ' here, ' + 'and a ' + sound + ' ' + sound + ' there.\n'
        story += 'Here a ' + sound + ', there a ' + sound + ', everywhere a ' + sound + ' ' + sound + '.\n'
        story += 'Old' + adjectives + ' McDonald'
        story += ' had a ' + location + '\n'
        story += 'E-I-E-I-O\n'
        
        self.display.delete(0.0, END)
        self.display.insert(0.0, story)

#main

root = Tk()
root.title("Mad Lib")
app = Mad_lib(root)
root.mainloop()
        
            

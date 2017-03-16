#Please call this program from the command line with the program name and your
#first and last name. An example might be...
#python final_project.py Alex McEvoy
#Please be sure the accompanying file celebrity_list.txt is in
#the same folder as the program

class Name_generator(object):
    """Pulls in a name list of celebrities and randomly selects one, assigning herpes to every 5th person"""

    def __init__(self, file_path = "./celebrity_list.txt"):
        self.__file_path = file_path
        self.__names_list = []
        self.__generate_names()
        
        
    def __str__(self):
        rep = "Names generated from file " + str(self.__file_path)
        return rep
        
        
    def __generate_names(self):
        with open(self.__file_path, "r") as f:
            celebs_list = f.readlines()
            for index,value in enumerate(celebs_list):
                value = value.strip('\n')
                if index % 5 == 0:
                    value += '+'
                self.__names_list.append(value)
                
    def get_a_name(self):
        from random import randrange
        size = len(self.__names_list)
        number = randrange(size)
        celebrity = self.__names_list.pop(number)
        return celebrity


##########################################################################


class Person(object):
    """Creates a person object that can marry, have coitus or kill"""
    
    name_list = Name_generator()
    
    def __init__(self, name = None):
        self.has_herpes = False
        self.is_married = "Noone"
        self.coitus_with = []
        self.killed = []
        self.is_dead = False
        
        if name:
            self.name = name
        else:
            name = Person.name_list.get_a_name()
            self.name = self.__herpes(name) 


    def __str__(self):
        ref = "Person is " + self.name + '\n'
        ref += "Is married to: " + self.is_married + '\n'
        ref += "Has had coitus with: " + str(self.coitus_with) + '\n'
        ref += "Has killed: " + str(self.killed) + '\n'
        ref += "Has herpes?: " + str(self.has_herpes) + '\n'
        ref += "Is dead?: " + str(self.is_dead) + '\n'
        return ref
    
    def __herpes(self, name):
        if name[len(name)-1] == '+':
            self.has_herpes = True
            new_name = name.replace('+', '')
        else:
            new_name = name
        return new_name

    def marry(self, other_person):
        if self.is_dead == True or other_person.is_dead == True:
            return False
        if self.is_married == 'Noone' and other_person.is_married == 'Noone':
            self.is_married = other_person.name
            other_person.is_married = self.name
            return True
        else:
            return False
    def coitus(self, other_person):
        if other_person.is_dead == True or self.is_dead == True:
            return False
        else:
            self.coitus_with.append(other_person.name)
            other_person.coitus_with.append(self.name)
            if other_person.has_herpes == True or self.has_herpes == True:
                self.has_herpes = True
                other_person.has_herpes = True
            return True
    def kill(self, other_person):
        if other_person.is_dead == True:
            print('{} is already dead.'.format(other_person.name))
            return False
        if self.is_dead == True:
            print("{}'s ghost came back from the grave to kill {}.".format(self.name, other_person.name))
            other_person.is_dead = True
            return True
        other_person.is_dead = True
        self.killed.append(other_person.name)
        return True


          

class Las_vegas(object):
    """Generates X number of people and randomly has them marry, perform coitus on and kill each other"""

    def __init__(self, number_of_people = 100, participant = None):
        self.number_of_people = number_of_people
        self.participant = participant
        self.peoples = self.make_some_peoples(self.number_of_people, self.participant)
        self.dead_peoples = []    
            
    def __str__(self):
        ref = "Las Vegas Object with " + str(self.number_of_people) + " people straight gettin' down"
        return ref

    def make_some_peoples(self, number, lucky_visitor = None):
        peoples = []
        if lucky_visitor:
            peoples.append(lucky_visitor)
            number -= 1
        for count in range(number):
            peoples.append(Person())
        return peoples

    def get_dirty(self):
        from random import randrange
        while len(self.peoples) > 1:
            rand_person = randrange(len(self.peoples))
            self.peoples[rand_person].marry(self.peoples[randrange(len(self.peoples))])
            self.peoples[rand_person].coitus(self.peoples[randrange(len(self.peoples))])
            self.peoples[rand_person].kill(self.peoples[randrange(len(self.peoples))])
            self.bring_out_ya_dead()
        return self.dead_peoples, self.peoples

    def bring_out_ya_dead(self):
        for person in self.peoples:
            if person.is_dead == True:
                self.dead_peoples.append(person)
                self.peoples.remove(person)
        return


class Marry_coitus_kill(object):
    """An interactive game of marry, coitus kill"""
    
    import sys
    
    def __init__(self, player = sys.argv[1] + ' ' + sys.argv[2]):
        if player:
            self.player = Person(player)
        else:
            self.player = Person()
        self.peoples = []
        self.peoples = [self.player, Person(),Person(),Person()]

    def __str__(self):
        ref = "A game of marry, coitus, kill with player "\
              + str(self.peoples[0].name) + '\n'
        return ref

    def get_value(self, options):
        value = None
        while not value:
            try:
                value = int(input(" "))
            except ValueError:
                value = None
            if value in range(1,4) and value in options:
                options.remove(value)
                return value, options
            else:
                print("Please enter a number between 1-3 that you have not yet selected")
                value = None
  
    
    def play(self):

        print("""
                    Welcome {} to Marry, Coitus, Kill!

                    The game of harsh judgement and rash decisions!
                    
                """.format(self.peoples[0].name))

        print("So....here are the options....\n")

        for index, person in enumerate(self.peoples):
            if index > 0:
                print(index, ": ", person.name)
        print("Please enter the number of your choices below..")    
        options = [1,2,3]
        
        print("Marry: ", end = " ")
        marry_choice, options = self.get_value(options)
        marry_choice = self.peoples[marry_choice]

        print("Coitus: ", end = " ")
        coitus_choice,options = self.get_value(options)
        coitus_choice = self.peoples[coitus_choice]
        
        print("Kill: ", end = " ")
        kill_choice,options = self.get_value(options)
        kill_choice = self.peoples[kill_choice]
        
        self.peoples[0].marry(marry_choice)       
        self.peoples[0].coitus(coitus_choice)
        self.peoples[0].kill(kill_choice)
        
        return self.peoples


def main():
    
    game = Marry_coitus_kill()

    peoples = game.play()

    input("Here's an overview of how that just went...\n\n")
    for person in peoples:
        print(person)
        input()

    print("""
        That was fun! But now lets scale it up a bit
        and take a trip to sunny Las Vegas!!!
        If you're feeling saucy, just enter the number of other people you'd
        like to take on your trip with you
        and get ready for fireworks!!!

            """)
    number = 0
    while number not in range(4,51):
        try:
            number = int(input("Please enter a number between 4 and 50: "))
        except ValueError:
            print("We needed a number between 4 and 100...")
            
    party = Las_vegas(number, peoples[0])

    dead, survivors = party.get_dirty()   
        
    for person in survivors:
        print("Wow, what a night.")
        input()
        print("Unfortunately with one of our guests getting killed every turn,")
        print("eventually there can be only one...")
        print("It looks like the only person walking away from this shindig is...")
        print("{}!! Here are their stats..\n".format(person.name))
        print(person)
    input()
    print("The ones who didn't make it are...\n\n\n\n")
    f = open("./police_report.txt", "w+")
    f.close()
    for person in dead:
        print(person)
        f = open("./police_report.txt", "a+")
        f.write(str(person) + '\n')
        input()
        
    sexual_history = {}     #This is to satisfy the dictionary requirement
    for person in peoples:
        sexual_history[person.name] = person.coitus_with
    search = None
    print("Your participants were..\n", sexual_history.keys())
    while search not in sexual_history.keys():
        search = input("Please enter the name of a person to see with whom they have had coitus with..")

    print(sexual_history[search])
    input()
    

main()





# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 4, boredom = 4):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __str__(self):
        me = ("Your Critter....\n")
        me += "name: " + self.name + "\n"
        me+= "hunger = " + str(self.hunger) + '\n'
        me+= "boredom = " + str(self.boredom) + '\n'
        return me        

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("{} says brruppp.  Thank you.".format(self.name))
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("{} says Wheee!".format(self.name))
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()



class farm(object):
    def __init__(self, name, critter_farm = []):
        self.__critter_farm = critter_farm
        self.__name = name   
    
    def __str__(self):
        print("Your farm {}\n".format(self.__name))
        the_farm = self.__critter_farm
        for critter in the_farm:
            print(critter)
        return str(len(the_farm)) + " animals in your farm"
    
#property for the list critter_farm. Allows both get and set
    @property
    def critter_farm(self):
        return self.__critter_farm
    @critter_farm.setter
    def critter_farm(self, new_farm):
        self.__critter_farm = new_farm
        
#farm's methods
    def talk(self):
        for critter in self.critter_farm:
            critter.talk()
    def eat(self, food = 4):
        for critter in self.critter_farm:
            critter.eat(food)
    def play(self, fun = 4):
        for critter in self.critter_farm:
            critter.play(fun)

def populate_farm():
    bud = Critter(name = "Bud", hunger = 2, boredom = 4)
    alex = Critter(name = 'Alex', hunger = 10, boredom = 6)
    steve = Critter(name = 'Steve', hunger = 20, boredom = 2)
    ray = Critter(name = 'Ray', hunger = 2, boredom = 2)
    
    farm_name = input("What would you like to call your farm??")
    our_farm = farm(farm_name, [bud,alex,steve,ray])
    return our_farm

def get_choice(farm = None):
        choice = None
        if not farm:
            new_farm = []
        else:
            new_farm = farm
        while choice != '0':
            print \
                  ("""
                Critter Farm
                0 - Quit
                1 - Add Critter
                2 - Delete Critter
                3 - Show the lil' guys
                """)
            choice = input("Choice: ")
            print()
            if choice == '0':
                   print("Goodbye")
            elif choice == '1':
                new_farm = add_critter(new_farm)
            elif choice == '2':
                new_farm = delete_critter(new_farm)
            elif choice == '3':
                for critter in new_farm:
                    print(critter)
            else:
                print("I'm sorry, we didn't understand your input")
                choice = 99
        return new_farm

    
def add_critter(farm):
    new_farm = farm
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    new_farm.append(crit)
    return new_farm

def delete_critter(farm):
    if not farm:
        print("There aren't any animals in your farm!")
    else:
        new_farm = farm
        
    for index, critter in enumerate(new_farm):
        print(index + 1, " - ", critter)
        
    try:
        choice = int(input("Which critter number would you like to delete?"))
    except TypeError:
        print("Please enter the number corresponding to the critter you'd \
like to exterminate. Killing the first critter we find instead")
        choice = 0

    print("{} deleted".format(new_farm[choice - 1]))
    del new_farm[choice - 1]
    return new_farm
 

def main():
    our_farm = populate_farm()
    
    print(our_farm)
    
    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters
        4 - Add/Delete Critters
        7 - The secret choice for all critters
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            our_farm.talk()
        
        # feed your critter
        elif choice == "2":
            food = input("How many food units would you \
like to give your critter?")
            our_farm.eat(int(food))
         
        # play with your critter
        elif choice == "3":
            hours = input("How many hours would you like to\
 play with your critter?")
            our_farm.play(fun = int(hours))

        elif choice == "4":
            our_farm.critter_farm = get_choice(our_farm.critter_farm)
            
        elif choice == "7":
            print(our_farm)
            
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")


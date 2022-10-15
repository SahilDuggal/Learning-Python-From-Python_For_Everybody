# OOPs --> Obvject Oriented Programming

# What is Object Oriented Programming ?
#   It is all the things we earlier did but now in depth. Basically, it is
#   the way to solve a perticular problem by creating certain objects.
#   It is generally based on real world problems

# What is a Class, Method/Message, Field/Attribute and Object/Instance ?
#   Class:  It is a template of object we will be creating.
#           E.g. --> String is a class:
#                                   x = 'Hello Sahil'
#                                   y = 'Hello Saloni'
#                                   z = 'Hello Pranav'
#           x, y and z are strings(class)
#   Method/Message: Defined capability of a class.
#           E.g. --> string.uppercase
#                           Which means to convert a sting to all uppercases alphabets.
#   Field/Attribute: Bit of data in a class.
#           E.g. --> x = 'Hello Sahil'
#                    y = 70
#                    z = 80 + y
#           here, in x there is a string attribute
#                 in y there is an integer
#                 in z there a attribute telling to do addition of 80 in y
#   Object/Instance: Let's say that an object is a well baked cake. So, to make that cake;
#                       there is class which is like a mould and its functionalities,
#                            like: shape of mould;
#                       there is method which will be the certain feature of that mould,
#                            like: quantity of that mould;
#                       there are attributes which are like the batter of cake,
#                            like: ingrediendts of that cake;
#                       and then there is the object which will be our cake.

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x +1
        print("So far", self.x)

    def name(n):
        n = input('Enter the name:')
        print("and name is", n)

an = PartyAnimal()
# an.party()
# an.name()
# an.party()
# an.name()
# an.party()
# an.name()

tr = PartyAnimal()
PartyAnimal.name(tr)                # tr.name()             ---> Same
PartyAnimal.name(PartyAnimal())     # PartyAnimal.name(tr)  ---> Same

#################################################################################################################

class PartyAnimal:
    x = 0

    def __init__(self) -> None:             # Constructor is called when we say to construct us certain object
        print('I am Constructed')
        
    def party(self):
        self.x = self.x +1
        print("So far", self.x)
        
    def __del__(self) -> None:              # Destructor is called when we want to destruct or is automatically called when variable is reassigned or the programm ends
        print('I am Destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
an.party()

an = 19
print('now an contains:', an)

#################################################################################################################

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, n) -> None:
        self.name = n
        print(self.name,'Constructed')
        
    def party(self):
        self.x = self.x +1
        print(self.name, "Party count", self.x)

s = PartyAnimal("Sahil")
s.party()

p = PartyAnimal("Pranav")
p.party()
s.party()

# Inheritance, also known as sub-class
# Sub-class is more specialized version of class... Sometimes parent class is the broad class and then it is devided into sub-classes
# Like is school: there is Primary classes then Middle and then High.
# All three of these have sub-classes(for primary it's generally class 1st to 5th and soo on...).
# This is for DRY (Do not Repeat Yourself)

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, n) -> None:
        self.name = n
        print(self.name,'Constructed')
        
    def party(self):
        self.x = self.x +1
        print(self.name, "Party count", self.x)
        
class FootBallFan(PartyAnimal):
    points = 0
    def touchDown(self):
        self.points = self.points +1
        self.party()
        print(self.name,"points are:",self.points)

s = PartyAnimal("Sahil")
s.party()

p = FootBallFan("Pranav")
p.party()
p.touchDown()

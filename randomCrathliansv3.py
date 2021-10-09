# python 3 version

import random

def pickRandom(kind):
    if (kind=="boy"):
        f = open("boy-names.txt")
        names = f.read().split()
        f.close()
    elif (kind=="girl"):
        f = open("girl-names.txt")
        names = f.read().split()
        f.close()
    elif (kind=="amalgam"):
        f = open("amalgam-surnames.txt")
        names = f.read().split()
        f.close()
    elif (kind=="dreg"):
        f = open("dreg-surnames.txt")
        names = f.read().split()
        f.close()
    elif (kind=="paragon"):
        f = open("paragon-surnames.txt")
        names = f.read().split()
        f.close()
    elif (kind=="drainer"):
        f = open("drainer-surnames.txt")
        names = f.read().split()
        f.close()
    elif (kind=="concubine"):
        f = open("colonial-girls.txt")
        names = f.read().split()
        f.close()
    elif (kind=="warrior"):
        f = open("colonial-boys.txt")
        names = f.read().split()
        f.close()
    elif (kind=="fathers"):
        f = open("colonial-surnames.txt")
        names = []
        for name in f:
            name = name.rstrip()
            names.append(name)
        f.close()
    elif (kind=="dragon"):
        f = open("dragon-boys.txt")
        names = f.read().split()
        f.close()
    elif (kind=="dragoness"):
        f = open("dragon-girls.txt")
        names = f.read().split()
        f.close()
    #names = ["John", "Jacob", "Jingleheimer", "Smith"]
    name = names[random.randint(0, len(names)-1)]
    return name

class Crathlian(object):
    def __init__(self, gender):
        if (gender == "male"):
            self.givenName = pickRandom("boy")
        else:
            self.givenName = pickRandom("girl")
        self.firstSurname = ""
        self.secondSurname = ""
        self.score = 0.00
    def __str__(self):
        return "{} {} {}, {}".format(self.givenName, self.firstSurname, self.secondSurname, self.score)
class Dreg(Crathlian):
    def __init__(self, gender):
        Crathlian.__init__(self, gender)
        self.firstSurname = pickRandom("dreg")
        self.secondSurname = pickRandom("dreg")
        self.score = round(random.triangular(0,50.00,40.00), 2)
class Amalgam(Crathlian):
    def __init__(self, gender):
        Crathlian.__init__(self, gender)
        self.firstSurname = pickRandom("amalgam")
        self.secondSurname = pickRandom("amalgam")
        self.score = round(random.triangular(50.00,100.00,75.00), 2)
class Paragon(Crathlian):
    def __init__(self, gender):
        Crathlian.__init__(self, gender)
        self.firstSurname = pickRandom("paragon")
        self.secondSurname = pickRandom("paragon")
        self.score = round(random.triangular(100.00,125.00,107.00), 2)
class Drainer(Crathlian):
    def __init__(self,gender):
        Crathlian.__init__(self, gender)
        self.firstSurname = pickRandom("drainer")
        self.score = round(random.triangular(100.00,125.00,102.00), 2)
    def __str__(self):
        return "{} {}, {}".format(self.givenName, self.firstSurname, self.score)
class Colonial(Crathlian):
    def __init__(self, gender):
        Crathlian.__init__(self, gender)
        if (gender == "male"):
            self.givenName = pickRandom("warrior")
        else:
            self.givenName = pickRandom("concubine")
        self.firstSurname = pickRandom("fathers")
        self.score = round(random.triangular(20.00,399.99,250.00), 2)
    def __str__(self):
        return "{} {}, {}".format(self.givenName, self.firstSurname, self.score)
class Shapeshifter(object):
    def __init__(self, gender):
        if (gender == "male"):
            self.gender = "male"
            self.givenName = pickRandom("dragon")
        else:
            self.gender = "female"
            self.givenName = pickRandom("dragoness")
        self.motherName = pickRandom("dragoness")
        self.fatherName = pickRandom("dragon")
        self.score = round(random.triangular(400.00,499.99,490.00), 2)
    def __str__(self):
        if (self.gender == "male"):
            return "{} son of {} and {}, {}".format(self.givenName, self.motherName, self.fatherName, self.score)
        else:
            return "{} daughter of {} and {}, {}".format(self.givenName, self.motherName, self.fatherName, self.score)

while(True):
    choice = input("Pick One: (Shapeshifter = S, Colonial Human = C, Modern Crathlian = M) ")
    choice.lower()
    print

    if choice == 's':
        for n in range(6):
            print (Shapeshifter("male"))
        print()
        for n in range(6):
            print (Shapeshifter("female"))

    elif choice == 'c':
        for n in range(6):
            print (Colonial("female"))
        print()
        for n in range(6):
            print (Colonial("male"))

    elif choice == 'm':
        for n in range(6):
            print (Dreg("male"))
        print()
        for n in range(6):
            print (Amalgam("female"))
        print()
        for n in range(6):
            print (Paragon("male"))
        print()
        for n in range(6):
            print (Drainer("female"))

    print()
    s = input("Generate more? ")
    if s == 'n':
        break

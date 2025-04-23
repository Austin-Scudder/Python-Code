import csv

def __init__ (self):
    filename = open('Magic card  Comparison\Moxfield Selling List 4-21-2025.csv', 'r' )

    file = csv.DictReader(filename)

    name = []

def nameget(self):
    for col in self.file:
        self.name.append(col['Name'])


def printnc(self):
    #debug name line check
    print ('Name:', self.name)
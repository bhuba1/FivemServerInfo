import re

class Player:
    def __init__(self, name=None, identifiers=None, readDict=None): 
        if readDict is not None:
            self.__dict__ = readDict
        else:   
            self.name  = re.sub(' +', ' ', name.replace('\n', '').replace('\r', ''))[1:-1]
            self.steam  = re.sub(' +', ' ', identifiers[0].replace('\n', '').replace('\r', ''))[1:-1]
            self.license = re.sub(' +', ' ', identifiers[1].replace('\n', '').replace('\r', ''))[1:-1]
            self.discord = None

            if len(identifiers) == 3:
                self.discord = re.sub(' +', ' ', identifiers[2].replace('\n', '').replace('\r', ''))[1:-1]
            else:
                self.discord = re.sub(' +', ' ', identifiers[4].replace('\n', '').replace('\r', ''))[1:-1]
    

    def __str__(self):
        return str(self.name)  + " | " + str(self.steam) + " | "  + str(self.license) + " | "  + str(self.discord)

    def __repr__(self):
        return str(self.name)  + " | " + str(self.steam) + " | "  + str(self.license) + " | "  + str(self.discord)
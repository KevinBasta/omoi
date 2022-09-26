import datetime
from time import sleep

class entry: 
    def __init__(self, title, body, locked):
        self.title = title
        self.body = body
        self.creationDate = datetime.datetime.now()
        self.editDate = self.creationDate
        self.locked = locked
    
    def getCreationDate(self): 
        return self.creationDate

    def getEditDate(self): 
        return self.editDate

    def updateEditDate(self): 
        self.editDate = datetime.datetime.now()

    def updateEntryText(self, newBody): 
        self.body = newBody
        self.updateEditDate()

    def lockEntry(self): 
        self.locked = True

    def unlockEntry(self): 
        self.locked = False

    def getBody(self):
        return self.body

if __name__ == '__main__': 
    day1 = entry("normal day", "Today I made a sandwich", False)
    print(day1.getBody())
    print("creation date: " + str(day1.getCreationDate()))
    print("edit date: " + str(day1.getEditDate()))

    sleep(60)

    day1.updateEntryText("Today I made a jam sandwich")
    print(day1.getBody())
    print("creation date: " + str(day1.getCreationDate()))
    print("edit date: " + str(day1.getEditDate()))

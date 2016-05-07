class Character:
    def __init__(self):
        self.first = ''
        self.last = ''
        self.gender = ''
        self.friend = 0
        self.image = ''

    def load(self,data):
        self.first = data[0]
        self.last = data[1]
        self.gender = data[2]
        self.friend = data[3]
        self.image = data[4]

    def label(self):
        return self.first.upper()

    def full(self):
        return self.first + " " + self.last

    def __str__(self):
        return self.full()

class Scene:
    def __init__(self):
        self.speaker = ''
        self.image = ''
        self.line = ''
        self.scene = 0
        self.act = 0
        self.show = False
        self.choice = []
        self.tag = ''
        self.bg = ''
        self.spkrobj = ''

    def load(self,data,chars):
        self.act = data[0]
        self.scene = data[1]
        self.speaker = data[2]
        self.line = data[3]
        self.show = self.findImage(chars,data[4])
        self.choice.extend(data[5])
        self.tag = data[6]
        self.bg = data[7]
        self.spkrobj = self.findSpeaker(chars)

    def findSpeaker(self,chars):
        for c in chars:
            if c.label() == self.speaker:
                return c

    def findImage(self,chars,spkr):
        if (spkr == None):
            return None
        for c in chars:
            if c.label() == spkr:
                return c

    def speakerImg(self):
        if (self.show == None):
            return '<img id="sprite" alt="placeholder" src="static/img/versoza.png" style="visibility:hidden;">'
        else:
            return '<img id="sprite" alt="' + self.show.label() + '" src="' + self.show.image + '" >'

    def isColor(self):
        if (self.bg == "black"):
            return "true"
        else:
            return "false"

    def __str__(self):
        return "Act " + self.act + " Scene " + self.scene + ": " + self.line

# Class Iterates Over Scene Instances
class Play:
    def __init__(self):
        self.pointer = 0
        self.act = 0
        self.count = 0
        self.scenes = []

    def append(self,data):
        self.scenes.append(data)
        self.count += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer < self.count:
            self.pointer += 1
            return self.scenes[self.pointer - 1]
        else:
            if (self.pointer == 0):
                return self.first()
            else:
                return self.scenes[self.pointer - 1]

    def first(self):
        return self.scenes[0]

    def __str__(self):
        return "Current Scene: Act " + self.act + " Scene " + self.pointer.scene

if __name__ == '__main__':
    import csv
    p = Play()
    try:
        f = open("text.csv", 'r')
        f.readline()
        cf = csv.reader(f, delimiter=",", quotechar='"')
        for line in cf:
            s = Scene()
            s.load(line)
            #print(s)
            p.append(s)
    except IOError as e:
            print('{}: {}'.format(e.__class__.__name__, "Invalid file name"))
    for i in range(len(p.scenes)):
        print(p.next())
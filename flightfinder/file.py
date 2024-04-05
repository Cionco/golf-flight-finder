

class FileReader:
    def __init__(self, filename):
        self.slots = None
        self.date = None
        self.hour = None
        self.driver_file = None
        self.locations = None
        self.filename = filename

    def load(self):
        file = open(self.filename, "r")
        lines = file.readlines()

        self.slots = int(lines.pop(0).split(": ")[1])
        self.date = lines.pop(0).split(": ")[1].strip()
        self.hour = int(lines.pop(0).split(": ")[1])
        self.driver_file = lines.pop(0).split(": ")[1].strip()
        self.locations = [line.strip() for line in lines]
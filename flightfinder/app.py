from flightfinder.controller import Controller
from flightfinder.file import FileReader


class App:

    def __init__(self):
        pass

    def run(self, argv):
        if len(argv) > 1:
            filename = argv[1]
        else:
            filename = "/Users/nicolaskepper/Downloads/Absolut.txt"

        config = FileReader(filename)
        config.load()

        controller = Controller(config.locations, config.slots, config.driver_file)
        times = controller.run(config.date, config.hour)
        print("Free tee times for {} players on day {} after hour {}".format(config.slots, config.date, config.hour))
        for course in times:
            print(course, times[course])
            print()

import sys
from flightfinder.controller import Controller
from flightfinder.file import FileReader

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "/Users/nicolaskepper/Downloads/Absolut.txt"

config = FileReader(filename)
config.load()

controller = Controller(config.locations, config.slots)
times = controller.run(config.date, config.hour)
print("Free tee times for {} players on day {} after hour {}".format(config.slots, config.date, config.hour))
for course in times:
    print(course, times[course])
    print()
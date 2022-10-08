from flightfinder.app import App
import sys
import schedule
import time


def exec():
    App().run(sys.argv)


if __name__ == "__main__":
    schedule.every(30).seconds.do(exec)

    while True:
        schedule.run_pending()
        for i in range(29, -1, -1):
            sys.stdout.write('\r')
            sys.stdout.write(str(i))
            sys.stdout.flush()
            time.sleep(1)
        print()


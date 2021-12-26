import monitor 
import time

RESOURCES_PATH = 'resources/'


def main():
    mon = monitor.Monitor()
    print("Start")

    while True:
        print(mon.grab_coord())
        time.sleep(.10)

        



if __name__ == '__main__':
    main()

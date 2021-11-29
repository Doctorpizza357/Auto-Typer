import pyautogui
from pynput.keyboard import *
import time

messageinput = input("What do you want to autotype?: ")

#  ======== settings ========
delay = 0.9  # in seconds
message = messageinput
resume_key = Key.home
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// - Settings: ")
    print("\t message = " + message)
    print("\t delay = " + str(delay) + '\n')

    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t ESC = Exit")
    print("-----------------------------")
    print('Press Home to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.typewrite(message)
            time.sleep(delay)

    lis.stop()


if __name__ == "__main__":
    main()
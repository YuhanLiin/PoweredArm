import pigpio
from sys import argv
from enum import Enum

pi = pigpio.pi()


class Servo:
    SAFE_MODE = True

    class Mode(Enum):
        Off = 0
        Very_Low = 500
        Low = 1000
        Neutral = 1500
        High = 2000
        Very_High = 2500

    def __init__(self, pin):
        self.pin = pin

    def drive(self, mode):
        if mode == Servo.Mode.Very_High or mode == Servo.Mode.Very_Low:
            if Servo.SAFE_MODE:
                print("Can't drive servos with extreme values in safe mode")
                return
        pi.set_servo_pulsewidth(self.pin, mode.value)

def main():
    print('Servo Testing')
    if len(argv) < 2:
        print("Usage: servo.py [comma-separated-list-of-servo-gpios] [unsafe]")
        return
    if len(argv) > 2:
        if argv[2] == 'unsafe': Servo.SAFE_MODE = False
        else: print("2nd arg isn't 'unsafe', ignoring")

    servos = [Servo(int(s)) for s in argv[1].split(',')] 
    print("Enter two numbers. The 1st specifies which servo to control and the second specifies the level to drive the servo at (0-5, 1 and 5 are unsafe)")
    try:
        while True:
            cmd = input("Enter two numbers: ")
            idx = int(cmd[0])
            mode = list(Servo.Mode)[int(cmd[1])] 
            servos[idx].drive(mode)
    except Exception as e:
        print(e)
        for servo in servos:
            servo.drive(Servo.Mode.Off)

if __name__ == '__main__':
    main()


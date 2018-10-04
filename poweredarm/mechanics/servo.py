import pwm

import atexit
from sys import argv
from enum import Enum

def reset(pwm_num):
    # Call this before drive()
    pwm.pwm_period_micro(pwm_num, 20000)
    pwm.pwm_off(pwm_num)

def drive(pwm_num, micro):
    if micro == 0:
        pwm.pwm_off(pwm_num)
        return
    if micro < 550 or micro > 2500:
        print("Can only safely operate between 550 and 2500")
        return
    pwm.pwm_duty_micro(pwm_num, micro)
    pwm.pwm_on(pwm_num)

def exit():
    for i in range(pwm.pwm_count()):
        reset(i)

def main():
    atexit.register(exit)
    print('Servo Testing')
    while True:
        cmd = raw_input("Enter PWM number and the duty cycle in microseconds: ")
        cmd = cmd.split(',')
        idx = int(cmd[0])
        duty = int(cmd[1]) 
        reset(idx)
        drive(idx, duty)

if __name__ == '__main__':
    main()


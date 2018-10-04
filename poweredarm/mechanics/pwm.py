paths = ['48300000.epwmss/48300200.pwm/pwm/pwmchip0/pwm-0:0/', 
         '48300000.epwmss/48300200.pwm/pwm/pwmchip0/pwm-0:1/',
         '48302000.epwmss/48302200.pwm/pwm/pwmchip2/pwm-2:0/',
         '48304000.epwmss/48304200.pwm/pwm/pwmchip4/pwm-4:0/',]

basepath = '/sys/devices/platform/ocp/'

# There are 4 distinct PWMs, as described in the docs. Each is accessed in a different path.
# The PWMs need to be enabled via config-pin and exported before this code is run

def pwm_dir(i):
    return basepath + paths[i]

def pwm_action(i, filename, action):
    with open(pwm_dir(i) + filename, 'w') as f:
        return action(f)

def pwm_on(i):
    pwm_action(i, 'enable', lambda f: f.write('1'))

def pwm_off(i):
    pwm_action(i, 'enable', lambda f: f.write('0'))

def pwm_period_nano(i, period):
    pwm_action(i, 'period', lambda f: f.write(str(period)))

def pwm_period_micro(i, period):
    pwm_action(i, 'period', lambda f: f.write(str(period * 1000)))

def pwm_duty_nano(i, period):
    pwm_action(i, 'duty_cycle', lambda f: f.write(str(period)))

def pwm_duty_micro(i, period):
    pwm_action(i, 'duty_cycle', lambda f: f.write(str(period * 1000)))

def pwm_count():
    return len(paths)

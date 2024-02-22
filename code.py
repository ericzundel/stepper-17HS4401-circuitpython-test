"""Control a stepper motor from a raspberry pi pico w"""
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
import time

from adafruit_motor.stepper import (
    StepperMotor,
    FORWARD,
    BACKWARD,
    SINGLE,
    DOUBLE,
    INTERLEAVE,
)

print("Hello World!")

# pwm0 = PWMOut(board.GP0, duty_cycle=0, frequency=2048)
# pwm1 = PWMOut(board.GP1, duty_cycle=0, frequency=2048)
# pwm2 = PWMOut(board.GP2, duty_cycle=0, frequency=2048)
# pwm3 = PWMOut(board.GP3, duty_cycle=0, frequency=2048)

# So little torque!
# stepper0 = StepperMotor(pwm0, pwm1, pwm2, pwm3)
# steps_per_rotation=200
# style=SINGLE

# Not much better
# stepper0 = StepperMotor(pwm0, pwm1, pwm2, pwm3)
# steps_per_rotation=200
# style=DOUBLE

pins = [
    DigitalInOut(board.GP0),
    DigitalInOut(board.GP1),
    DigitalInOut(board.GP2),
    DigitalInOut(board.GP3),
]

for pin in pins:
    pin.direction = Direction.OUTPUT
    pin.value = False

stepper0 = StepperMotor(pins[0], pins[1], pins[2], pins[3], microsteps=None)
steps_per_rotation = 200
style = SINGLE
style = DOUBLE
delay = .0035  #.0035 is about as fast as it will reliably go

while True:
    print("Forward %d steps" % (steps_per_rotation))
    for i in range(steps_per_rotation):
        stepper0.onestep(direction=FORWARD, style=style)
        time.sleep(delay)
    #time.sleep(1)
    #print("Backward %d steps" % (steps_per_rotation))
    #for i in range(steps_per_rotation):
    #    stepper0.onestep(direction=BACKWARD, style=style)
    #    time.sleep(delay)
    #time.sleep(1)

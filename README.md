# stepper-17HS4401-circuitpython-test
Testing a 17HS4401 stepper motor (3.8V/1.5A 200 steps/revolution) with an L298N hbridge and circuitpython

The power side of the HBridge was powered by my power supply running at 4V.  The pico was powered by a USB cable.

I discovered a few things:

The fastest I could reliably turn the motor was with a .0035 (3.5ms) delay between steps with DOUBLE style set.  Faster than that andI lost a lot of torque (it skipped steps.)

Using the "DOUBLE" noticeably increased torque.

In the circuit, it is critical to connect the ground of the Pico to the ground of the L298N.

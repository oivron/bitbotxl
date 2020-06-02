"""
Author: Øivind Rønning, Statped
Github: https://github.com/oivron/bitbotxl
"""

from microbit import *
from utime import ticks_us, sleep_us


class __Bitbot:
    """Holder of the left and right motors"""

    def __init__(self):
        self.__leftMotor = __Motor(pin8, pin16)
        self.__rightMotor = __Motor(pin12, pin14)
        self.__LEFT_BIAS = 1.0
        self.__RIGHT_BIAS = 1.0

    def bias(self, direction, percent):
        """Set left/right bias to match motors."""

        factor = (percent + 100)/100
        if direction == LEFT:
            self.__RIGHT_BIAS = float(factor)
        elif direction == RIGHT:
            self.__LEFT_BIAS = float(factor)

    def go(self, direction, speed):
        """Move robot forwards or backwards at speed."""

        self.__drive(direction, speed)

    def goms(self, direction, speed, duration):
        """Move robot forwards or backwards at speed for milliseconds."""

        self.__drive(direction, speed)
        sleep(duration)
        self.stop()

    def spin(self, direction, speed):
        """Rotate robot in direction at speed.
        direction: LEFT or RIGHT
        speed in %"""

        self.__drive(direction, speed)

    def spinms(self, direction, speed, duration):
        """Rotate robot in direction at speed for milliseconds.
        direction: LEFT or RIGHT
        speed in %
        duration in milliseconds"""

        self.__drive(direction, speed)
        sleep(duration)
        self.stop()

    def buzz(self, duration):
        """Sound a buzz for milliseconds."""

        pin0.write_digital(1)
        sleep(duration)
        pin0.write_digital(0)

    def linesensor(self, direction):
        """Read line sensor."""

        dir = direction
        if dir == LEFT:
            return bitbot.__getLine(0)
        elif dir == RIGHT:
            return bitbot.__getLine(1)

    def sonar(self):
        """Read ultrasonic distance sensor.
        Returns distance to nearest object in cm."""

        pin15.write_digital(1)
        sleep_us(10)
        pin15.write_digital(0)
        pin15.set_pull(pin15.NO_PULL)
        while pin15.read_digital() == 0:
            pass
            start_time = ticks_us()
        while pin15.read_digital() == 1:
            pass
            end_time = ticks_us()
        elapsed = end_time - start_time
        distance = int(0.01715 * elapsed)
        return distance

    # This method needs an additional parameter (Brake el. Coast)
    def stop(self):
        """Stops the Bit:bot"""

        pin8.write_digital(0)
        pin12.write_digital(0)
        pin16.write_analog(0)
        pin14.write_analog(0)

    # Help function for linesensor().
    def __getLine(self, bit):
        """Reads value of left or right line sensor."""

        mask = 1 << bit
        value = 0
        try:
            value = i2c.read(__I2CADDR, 1)[0]
        except OSError:
            pass
        if (value & mask) > 0:
            return 1
        else:
            return 0

    def __drive(self, direction, speed):
        """Starting robot with given directon and speed."""

        # Recalculates from percent to absolute (0 - 1023)
        speed = speed * __SPEED_RATIO

        if direction == FORWARD:
            pin8.write_digital(0)
            pin12.write_digital(0)
            # Corrects speed for bias
            pin16.write_analog(speed * self.__LEFT_BIAS)
            pin14.write_analog(speed * self.__RIGHT_BIAS)
        elif direction == REVERSE:
            pin8.write_digital(1)
            pin12.write_digital(1)
            # Corrects speed for bias and reverse
            pin16.write_analog((speed * self.__LEFT_BIAS) * __REVERSE_RATIO)
            pin14.write_analog((speed * self.__RIGHT_BIAS) * __REVERSE_RATIO)
        elif direction == LEFT:
            pin8.write_digital(1)
            pin12.write_digital(0)
            # Corrects speed for bias and reverse
            pin16.write_analog((speed * self.__LEFT_BIAS) * __REVERSE_RATIO)
            pin14.write_analog(speed * self.__RIGHT_BIAS)
        elif direction == RIGHT:
            pin8.write_digital(0)
            pin12.write_digital(1)
            # Corrects speed for bias and reverse
            pin16.write_analog(speed * self.__LEFT_BIAS)
            pin14.write_analog((speed * self.__RIGHT_BIAS) * __REVERSE_RATIO)


class __Motor:
    """Class definition for the Bit:bot motors"""

    def __init__(self, directionPin, speedPin):
        self.dPin = directionPin
        self.sPin = speedPin


LINESENSORLEFT = "linesensorleft"
LINESENSORRIGHT = "linesensorright"
FORWARD = "forward"
REVERSE = "reverse"
RIGHT = "right"
LEFT = "left"

# Initializing
__REVERSE_RATIO = 0.7 # Very simple correction of reverse speed
__SPEED_RATIO = 10.23  # Converts from % to pin speed
__I2CADDR = 0x1c  # address of PCA9557

bitbot = __Bitbot()

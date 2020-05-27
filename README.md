# bitbotxl

A Python module for the 4tronix Bit:bot XL.

To be used with the Visual Studio Code extension found at [https://github.com/oivron/microbit-extension-vscode](https://github.com/oivron/microbit-extension-vscode). The extension is also available from [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/).

## Installation
```pip install bitbotxl```

## Usage
See documentation and examples below.

See [micro:bit Micropython API](https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html) for a complete documentation/API on how to use the micro:bit.

### Import
To use this module in your Python script:
```
from bitbotxl import *
```

### Bit:bot XL API
```
# Set left/right bias to match motors.
# Direction: LEFT or RIGHT.
# Bias in %.
bias(direction, percent)
```

```
# Move robot forward or reverse at speed.
# Direction: FORWARD or REVERSE.
# Speed in %.
go(direction, speed)
```

```
# Move robot forward or reverse at speed for milliseconds.
# Direction: FORWARD or REVERSE.
# Speed in %.
# Duration in milliseconds.
goms(direction, speed, duration)
```

```
# Rotate robot left or right at speed.
# Direction: LEFT or RIGHT.
# Speed in %.
spin(direction, speed)
```

```
# Rotate robot left or right at speed for milliseconds.
# Direction: LEFT or RIGHT.
# Speed in %.
# Duration in milliseconds.
spinms(direction, speed, duration)
```

```
# Sound a buzz for milliseconds.
# Duration in milliseconds.
buzz(duration)
```

```
# Read line sensor.
# Directon: LEFT or RIGHT.
linesensor(direction)
```

```
# Read ultrasonic distance sensor.
# Returns distance in cm.
def sonar()
```

```
# Stops the Bit:bot.
stop()
```

## Examples
These are some simple examples on how to use the line sensor and the ultrasonic distance sensor.

Adjust the arguments for speed and duration according to your own preferences.

### Line sensor
```
# Let Bit:bot follow a dark line.
if (bitbot.linesensor(RIGHT) == 1):
    bitbot.spinms(RIGHT, 10, 1) # Corrects direction. Arguments need to have very small values.
elif (bitbot.linesensor(LEFT) == 1):
    bitbot.spinms(LEFT, 10, 1) # Corrects direction. Arguments need to have very small values.
else:
    bitbot.go(FORWARD, 50)
```

```
# Let Bit:bot drive between two dark lines.
if (bitbot.linesensor(RIGHT) == 1):
    bitbot.spinms(LEFT, 10, 1)
elif (bitbot.linesensor(LEFT) == 1):
    bitbot.spinms(RIGHT, 10, 1)
else:
    bitbot.go(FORWARD, 50)
```

### Sonar
```
# Stop, reverse and spin the Bit:bot when it gets close to an object in front of it.
# The sonar() method returns the distance to the nearest object in cm.
bitbot.go(FORWARD, 50)
if bitbot.sonar() < 15:
    bitbot.stop()
    bitbot.goms(REVERSE, 50, 700)
    bitbot.spinms(RIGHT, 50, 200)
```

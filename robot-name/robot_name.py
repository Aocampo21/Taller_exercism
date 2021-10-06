from string import ascii_uppercase
from string import digits
from random import choice


class Robot():
    names_used = {}

    def newname():
        alpha = ''.join([choice(ascii_uppercase) for i in range(2)])
        numbr = ''.join([choice(digits) for i in range(3)])
        name = f'{alpha}{numbr}'
        Robot.names_used.setdefault(name, 1)
        return name

    def __init__(self):
        self.name = Robot.newname()

    def reset(self):
        name_reset = Robot.newname()
        if name_reset in Robot.names_used:
            name_reset = Robot.newname()
        self.name = name_reset
        return self.name

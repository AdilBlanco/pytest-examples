import sys
from datetime import date


class Container:

    def __init__(self):
        if date.today().day % 2 == 0:
            self.code = 'XC-0'
        else:
            self.code = 'XC-1'


class ContainerPlatform:

    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'

import os
from time import sleep as _sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep(seconds):
    _sleep(seconds)

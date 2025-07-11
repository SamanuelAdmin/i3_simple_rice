#!/usr/bin/python3
from controller import Controller
import sys

def main():
    if len(sys.argv) != 3:
        print('Incorrect args! Use: python3 file.py path/to/led on_or_off')
        exit(1)

    kbc = Controller(sys.argv[1])
    
    if sys.argv[2] == 'on':
        kbc.set_brtn(1)
    elif sys.argv[2] == 'off':
        kbc.set_brtn(0)
    elif sys.argv[2] == 'switch':
        if kbc.cur_brtn == 1:
            kbc.set_brtn(0)
        else: kbc.set_brtn(1)
    else:
        print(f'Incorrect {sys.argv[2]}, use [on] or [off] instead!')

if __name__ == "__main__": main()

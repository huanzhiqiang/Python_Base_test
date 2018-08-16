#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import time,threading


def print_help():
    print('Usage: ')
    print('  python killmem.py 100MB')
    print('  python killmem.py 1GB')

def main():
    if len(sys.argv) == 2:
        pattern = re.compile('^(\d*)([M|G]B)$')
        match = pattern.match(sys.argv[1].upper())
        if match:
            num = int(match.group(1))
            unit = match.group(2)
            con.acquire()
            if unit == 'MB':
                s = ' ' * (num * 1024 * 1024)
            else:
                s = ' ' * (num * 1024 * 1024 * 1024)
            con.wait()
            # time.sleep(10000)
        else:
            print_help()
    else:
        print_help()

if __name__ == "__main__":
    con = threading.Condition()
    while True:
        main()
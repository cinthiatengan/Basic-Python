#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import os
import sys
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    s = sys.platform
    print(s)
    o = os.name
    print(o)
    t = os.getenv('PATH')
    print(t)
    u = os.getcwd()
    print(u)
    x = os.urandom(25).hex()
    print(x)
    y = list(range(25))
    print(y)
    random.shuffle(y)
    print(y)
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if __name__ == '__main__': main()

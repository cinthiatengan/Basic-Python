#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('lalala')
    print("ola estou fora do bloco")
    if False:
        print('linha 3')
    else:
        print('falso')

if __name__ == '__main__': main()

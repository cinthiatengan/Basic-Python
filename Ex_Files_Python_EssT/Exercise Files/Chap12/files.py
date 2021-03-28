#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt') # segundo argumento r= read, w = write, a = append r+ = read and write, r+t = binary mode
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()

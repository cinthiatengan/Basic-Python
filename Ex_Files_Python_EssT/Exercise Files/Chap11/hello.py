#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World. {}'.format(3*2))

print("""
      HELL IS
      HERE.
      
      {}
      
      """.format(2*1015))

s='FORA BOZO. {}'
print(s.format(2*8.5))

class MyString(str):
    def __str__(self):
        return self[::-1]

s= MyString('GENOCIDA BASCULHO')
print(s)
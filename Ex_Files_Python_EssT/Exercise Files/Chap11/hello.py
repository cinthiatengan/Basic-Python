#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World. {}'.format(3*2))

print("""
      HELL IS
      HERE AND
      WE ARE ALL DOOMED.
      
      {}
      
      """.format(2*1015))

s='FORA BOZO. {}'
print(s.format(2*8.5))

class MyString(str):
    def __str__(self):
        return self[::-1]

s= MyString('GENOCIDA BASCULHO')
print(s)

x = 42
y=73
print("the number is {} {}".format(x, y))
print("the number is {xx} {bb}".format(xx=x, bb=y))
print("the number is {1} {0}".format(x, y)) #posicao
print("the number is {0:<05} {1:>05}".format(x, y))
a=43*66*22*10000
print("the number is {:,}".format(a))
print("the number is {:.3f}".format(a))
print("the number is {:f}".format(a)) 
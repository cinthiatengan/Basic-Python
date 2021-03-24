#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

x = 'seven'.upper()
print('x is {}'.format(x))
print(type(x))

y = 'seven'.capitalize()
print('y is {}'.format(y))
print(type(y))

z = 'seven {1:<9} {0:>9}'.format(8,9)
print('z is {}'.format(z))
print(type(z))

w = 'seven {} {}'.format(8,9)
print('w is {}'.format(w))
print(type(w))

v = 'seven {1} {0}'.format(8,9)  #muda a posição
print('v is {}'.format(v))
print(type(v))

u = 'seven {1:<09} {0:>09}'.format(8,9)  #adiciona espaços, no caso zeros
print('u is {}'.format(u))
print(type(u))

a=9
b=8
i = f'seven {a} {b}'            #olha esse caraio de f kkkkkkkkkkkkkkkkkkkkk se nao coloca ele nao chama fstrings se chama
print('i is {}'.format(i))
print(type(i))

j = f'seven {a:<09} {b:>09}'            
print('j is {}'.format(j))
print(type(j))

k = 7*4.35678 #coisas de python3
print('k is {}'.format(k))
print(type(k))

n=Decimal('.10')
m=Decimal('.30')
f = n+n+n-m
print('f is {}'.format(f))
print(type(f))

t = True
print('t is {}'.format(t))
print(type(t))

c = 5<3
print('c is {}'.format(c))
print(type(c))


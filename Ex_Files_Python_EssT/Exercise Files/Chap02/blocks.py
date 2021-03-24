#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = 112 #a variavel possui escopo mesmo fora do bloco que ela se encontra !!!!
    print('x < y: x is {} and y is {}'.format(x, y))
    print('adeus vida de madao')
    print('agora é trabalhar 9h por dia, 5 dia por semana')
    print('gosto de: trabalhar')
    print('não gosto de: trabalhar')
elif x == y:
    print('x == y: x is {} and y is {}'.format(x, y))
else:    
    print('x is {}'.format(x))

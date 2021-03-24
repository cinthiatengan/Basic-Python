#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


y = ( 1, 2, 3, 4, 5 ) # tupla imutavel os valores dentro
x = [ 1, 2, 3, 4, 5 ] # lista pode se alterar seus valores
z = range(5, 50, 5) # aceita mais parametros (inicio, fim, passo) aqui ele forma uma tupla e nao deixa alterar
# x[2] = 43
for i in z:
    print('i is {}'.format(i))

#w = list(range(5)) # lista que pode ser alterada os elementos
#w[2] = 50
#for a in w:
    #print('a is {}'.format(a))
v = { "one" : 1, "two" : 2, "three" : 3, "four" : 4 } #dicionario, com chave e valor
for k, v in v.items():
    print("k: {}, v: {}".format(k,v))

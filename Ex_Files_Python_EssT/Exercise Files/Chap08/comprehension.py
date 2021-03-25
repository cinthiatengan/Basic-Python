#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11) # gera uma lista de 0 a 10
    from math import pi
    #seq2 = [x*2 for x in seq] # multiplica por 2 todos os elementos da lista original seq
    #seq2 = [x for x in seq if x%3 !=0] #mostra apenas os elementos q sobra resto quando divididos por 3
    #seq2 = [(x, x**2) for x in seq] #transforma em tuplas de duplo elemento dele mesmo
    #seq2 = [round(pi, i) for i in seq] # pi arredondado pelo numero numero de lugares de cada elemento na sequencia
    #seq2 = { x: x**2 for x in seq } # criação do dicionario obs. mudar o print_list para print para funcionar.
    seq2 = { x for x in 'superduper' if x not in 'pd'} # cria um set e mostra as letras 

    
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

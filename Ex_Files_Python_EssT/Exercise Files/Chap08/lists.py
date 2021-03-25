#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ] #List
    print(game[1:3]) #pode se usar o metodo de 3 parametros
    i= game.index('Paper')
    #game.append("João")
    #game.insert(0, "Corea")
    print(', '.join(game)) # coloca uma virgula entre os elementos da lista
    print(len(game))
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()

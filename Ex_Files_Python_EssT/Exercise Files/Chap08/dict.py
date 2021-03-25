#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    friends = dict(Joao = 'aoba', Correa = 'ai credo', Nita = "au au")
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    #for v in friends.values(): print(v)
    #animals['lion'] = 'I am a lion'
    #animals["bird"] = 'piu piu'
    print('found!' if 'lion' in animals else 'nope!')
    print_dict(animals)
    

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()

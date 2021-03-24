#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quaaaack!'
    walking = 'Walks like a duck.'
    
    def quack(self):
        print(self.sound)

    def walk(self):
        print('self.walking')

def main():
    donald = Duck()   # donald eh um objeto da classe duck
    donald.quack()    # chama o metodo quack
    donald.walk()     # chama o meoto walk

if __name__ == '__main__': main()

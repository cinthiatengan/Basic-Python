#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Aluno:
    estuda = "digita os codigos"
    boceja = "aaaaahhhh"
    
    def estuda(self):
        print(self.estuda)
        
    def boceja(self):
        print(self.boceja)
        
def main():
    joao = Aluno()
    joao.estuda()
    joao.boceja()

if __name__ == '__main__': main()
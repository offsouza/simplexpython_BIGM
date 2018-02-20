# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 18:30:03 2017

@author: Otávio Felipe Ferreira de Souza 
Matricula: 130916

"""
import numpy as np
import pandas as pd 

 

class Usuario(object):
    
    
    def criar_tabela(self):
        

        tabela = [] 
        z = raw_input("Digite a funcao Z (Separado por virgulas): "  )
     
        #eqz = raw_input("Digite para funcao z: \n <= \n >= \n =")
        valorbz = 0 #int(raw_input("Digite valor da inequacao: "))
        
        z = z.split(",")
        
        z = [int(numero) for numero in z] # converte str para int
        
        tamanhoz = len(z)
        listaz= [] # ira receber as variaveis 
        listaeq = []
        #listaeq.append(eqz)
        
        
        for u in range(0, tamanhoz):    
             a11 = z[u]
             #print a11
             locals()['zx{0}'.format(u)] = a11 #cria variaveis x1,x2...'''
             letra = locals()['zx{0}'.format(u)]
             listaz.append(letra)
             
        
        
        listaz.append(valorbz)   #adiciona valor de b          
        tabela.append(listaz)
        print tabela
        
         
        
        self.nrestricao = int(raw_input("Digite o numero de restricoes:" ))
        
        
        
        for j in range(0,self.nrestricao):
            
            r = raw_input("Digite a funcao da "+str(j+1)+"o restricao (Separado por virgulas): "  )
            r = r.split(",")
            r = [int(numero) for numero in r] # converte str para int
            tamanhoz = len(r)
            locals()['listar{0}'.format(j)] = [] # cria lista para receber lista com os nomes da restricoes
            
            
            eq = raw_input("Digite para as restricoes (separar por virgula)  :\n <= \n >= \n = \n")
            valorbr = int(raw_input("Digite valor da inequacao de R: "))
            #valorbr = valorbr.split(",")
            #valorbr = [int(numero) for numero in valorbr]
            #valorbr.append(valorbz)
            #print valorbr
            locals()['valorbr{0}'.format(j)]= valorbr #cria e varia a varialel valorbr responsavel por guarda valor da inequação
            valorbr = locals()['valorbr{0}'.format(j)] #pego valor da variavel valorb{0} e guarda na variavel valorbr para ser adicionado a lista no final
            
            #locals()['eqr{0}'.format(j)] = eq
            #eq = locals()['eqr{0}'.format(j)]
            listaeq.append(eq)
            
                        
            for i in range(0, tamanhoz):
                               
                
                #----------------------------------------------------------
                a22 = r[i]
                locals()['r{0}'.format(j)+'_{0}'.format(i)] = a22
                letra = locals()['r{0}'.format(j)+'_{0}'.format(i)]
                locals()['listar{0}'.format(j)].append(letra)
                
            
            locals()['listar{0}'.format(j)].append(valorbr) # adiciona lista da restricao o valorb
            tabela.append(locals()['listar{0}'.format(j)]) # adiciona a lista na tabela
            print tabela
            print listaeq
        print "tabela : \n", tabela   
        self.igualdade(listaeq,tabela)
        self.tabela = np.array(self.tabela, dtype = float )
        return self.tabela
        
        
        
    def numero (self):
        numero11 = artii 
        
        return numero11
        
    def igualdade(self, listaeq, tabela) :   
        self.listaeq = listaeq
        self.tabela = tabela
        self.numartifi = 0
        #lista = ['<=','>=']
        for p in range(1,2+1):
   
        
            locals()['folga{0}'.format(p)] = [[0]]
           # locals()['artifi{0}'.format(p)] =[0]
            for ww in range (0,2):
                locals()['folga{0}'.format(p)].append([0])            
            
            listaeq = self.listaeq[p-1]
        
            if listaeq == '>=':
                
                locals() ['folga{0}'.format(p)] [p] = [-1]
                locals()['artifi{0}'.format(p)] =[[0]]
                for ww in range (0,2):
                    locals()['artifi{0}'.format(p)].append([0])   
                    
                locals()['artifi{0}'.format(p)][p] = [1]
                self.numartifi += 1
                
                                
            if listaeq == '<=':
                locals() ['folga{0}'.format(p)][p] = [1]
                
            if listaeq == '=':
                locals()['artifi{0}'.format(p)] =[[0]]
                for ww in range (1,2+1):
                    locals()['artifi{0}'.format(p)].append([0])
                locals()['artifi{0}'.format(p)][p] = [1]
                self.numartifi += 1 
                
           
            a = np.array(locals()['folga{0}'.format(p)])
            self.tabela = np.hstack((self.tabela, a ))
            print self.tabela
             
        for qq in range(1,2+1):
            try: 
                
                    
                    add_arti =  np.array(locals()['artifi{0}'.format(qq)])
                    self.tabela = np.hstack((self.tabela, add_arti))
                    
            except KeyError :
                pass
                
        print (self.tabela)
            #print (locals()['folga{0}'.format(p)])
            
        #colocando coluna b no final 
        tamanho_tabela = len (self.tabela[0,:])
        print 'tamanho tabela', tamanho_tabela
        ordem = []
        for nn in range(0, tamanho_tabela-1 ):
            indiceb = (tamanho_tabela-1)- (self.numartifi + self.nrestricao)
            print 'indiceb', indiceb
            if indiceb == nn:
                ordem.append(tamanho_tabela-1)
                
            ordem.append(nn)
        print ordem
        i = np.argsort(ordem)
        self.tabela = self.tabela[:,i]
        self.tabela = np.array(self.tabela, dtype = float )
        print pd.DataFrame(self.tabela)
        
        global artii 
        artii =  self.numartifi
        
                
                
                
                                
                
            
        
        
        
        
        
        
        
        

#Usuario().criar_tabela()






        
#tabela = [listaz, listar1 ]
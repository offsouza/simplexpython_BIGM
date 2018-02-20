# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 13:53:57 2017

@author: Otávio Felipe Ferreira de Souza 
Matricula: 130916

"""

#import scipy as sp
import numpy as np
import pandas as pd
import criartabela as ct 




class simplex_BIG_M(object):

    def __init__(self, tabela):
        self.a = tabela
        self.a = np.array(self.a, dtype = float)
       

        print 'tabela alterada : \n', self.a
        result1 = self.simplexM(self.a)
        print 'PASSSO 222222'
            
        
    
            
        self.simplexnormal(result1)



    def variaveis_arti(self):
        pass


        
    def simplexnormal(self, tabela2):
        a = tabela2
        check = False
        a = tabela2
        x=1
        ver = (tabela2 [0, :] >= 0 ).all()
                #print ver 
                
        if ver == True:
                    
            check = True
            
        while check == False:
            
                
                
                # escolher menor numero da primeira linha
                xentra_pos = np.argmin(a[0,:]) #xentra = indice da coluna
                print 'xpivo', xentra_pos
                numero_colunas = len(a[0,:])
                numeor_linhas = len (a[:,0])
                #x sai
                coluna_entra = a[1:,xentra_pos]
                #print coluna_entra
                b = a[1:,numero_colunas-1] # captura dados da coluna b, para dividir pela coluna pivo e achar linha pivo
                #print b
                xsai = b / coluna_entra
                print xsai
                xsai = xsai[np.where( xsai>0)]
                print xsai
                xsai_pos = np.argmin(xsai)+ 1  # xsai = indice da linha
                print 'xsai', xsai_pos
        
                # Dividir linha pivo pelo numero pivo
                numeropivo = a[xsai_pos, xentra_pos]
                print 'linha pivo: ', numeropivo
                linhapivo = a[xsai_pos, :]
                print 'linha pivo:', linhapivo
                novalinhapivo = linhapivo / numeropivo
                print 'nova linha pivo: ', novalinhapivo
        
                #zerar os valores da coluna pivo
        
                tabela = []
                for i in range(0,numeor_linhas):
                    linha = a[i,:]
                    print 'linha de selecao: ', linha
                    if np.array_equal(linha, linhapivo)== True :
                        #novalinhapivo = list(novalinhapivo)
                       
                        tabela.append(novalinhapivo)
                    else:
                        elementox = a[i,xentra_pos]
                        print 'elementox', elementox
                        linha = linha - (novalinhapivo * elementox)
                        print 'linha' , linha
                        tabela.append(linha)
                        
                print '\n\n'
                tabela = pd.DataFrame(tabela)
                tabela = np.array(tabela)
               
                print "Interação nº:", x
                print tabela
               
                '''for i in range(0,numeor_linhas):
                    tabela 
                if tabela [i,:] > 0 '''
                        
                
                ver = (tabela [0, :] >= 0 ).all()
                #print ver 
                
                if ver == True:
                    
                        check = True
                        
                        
                        
                #print"check", check
                a = tabela
                #raw_input("Press Enter to continue...")
                x +=1
                    
                        
                        
        print("solucao otima\n")
        print pd.DataFrame(a)
        
        
    def simplexM (self, tabela1):
                
                a = tabela1
                x =1
                #a= np.array(a)
                
                numartifi = 2 
                
                #numero_colunas = len(a[0,:])
                numeor_linhas = len (a[:,0])
                
                tamanho_a = len(a[0,:])-1
                
                listaa=[]
                
                for ii in range(1, numartifi+1):
                    
                  indice = np.argmax(a[:,tamanho_a-numartifi + ii-1])
                  
                  colunas = a[indice, :tamanho_a]
                  listaa.append(colunas)
                  
                
                listaa = sum(listaa)
                print listaa
                check2 = True
                
                while check2 == True:
                    
                
                    icolunaentra = np.argmax(listaa)
                    print 'mairo valor ', icolunaentra
                    
                    colunaentra = a[1:,icolunaentra]
                    print colunaentra
                    
                    b = a[1:,tamanho_a]
                    print 'asdfasdfaf'
                    print b 
                    
                    linhaentra = b / colunaentra
                    print linhaentra
                    ilinhaentra = np.argmin (linhaentra) + 1 
                    print ilinhaentra
                    numeropivo = a[ilinhaentra, icolunaentra]
                    
                    print 'numero pivo: ', numeropivo
                    linhapivo = a[ilinhaentra, :]
                    
                    print 'linha pivo:', linhapivo
                    novalinhapivo = linhapivo / numeropivo
                    print 'nova linha pivo: ', novalinhapivo
                    
                    tabela = []
                    for i in range(0,numeor_linhas):
                        
                                        linha = a[i,:]
                                        print 'linha de selecao: ', linha
                                        if np.array_equal(linha, linhapivo)== True :
                                            #novalinhapivo = list(novalinhapivo)
                                            
                                            tabela.append(novalinhapivo)
                                        else:
                                            elementox = a[i,icolunaentra]
                                            print 'elementox', elementox
                                            linha = linha - (novalinhapivo * elementox)
                                            print 'linha' , linha
                                            tabela.append(linha)
                                            
                    print '\n\n'
                    tabela = pd.DataFrame(tabela)
                    tabela = np.array(tabela)
                    
                    print "Interação para eliminacao artificial nº:", x
                    print tabela
                 
                    check2 = False
                    for ii in range(1, numartifi+1):
                        indice = tamanho_a-numartifi + ii-1
                        
                        if np.array_equal( a[:, indice], tabela[:,indice]) == True:
                             
                            aaa = tabela[:,indice]
                            print 'aaa', aaa
                            iver = np.argwhere( aaa == 1)
                            #iver =iver.flatten()
                            
                            print 'iver', iver 
                            listaa = tabela[iver,:tamanho_a]
                            #listaa = listaa.flatten()
                            print 'listaa', listaa 
                            check2 = True
                    a= tabela
                    print 'a', a
                    x+=1
                a[0,tamanho_a]= -a[0,tamanho_a] # inverte pois e de minimizar
                for nn in range(0, numartifi):
                        indiceartifi = (tamanho_a) - (numartifi) 
                        print 'indice', indiceartifi
                        a = np.delete(a,  indiceartifi,1)
                        print a 
                        
                        
                print 'INDO PASSO 2'
                return a      
                         
                        
                
        
            
        
a=ct.Usuario().criar_tabela()
#b=ct.Usuario().numero()


#print b

simplex_BIG_M(a)

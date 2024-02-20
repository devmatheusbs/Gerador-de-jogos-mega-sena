from tkinter import *
from random import randint

class Interface():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Gerador de Números - Mega Sena')
        self.root.geometry('600x400')
        self.qtd_numeros = Label(self.root, text='Digite a quantidade de Números (6 a 20)')
        self.qtd_numeros.pack()
        self.qtd_numeros_entry = Entry(self.root)
        self.qtd_numeros_entry.pack()
        self.qtd_jogos = Label(self.root, text='Digite a quantidade de Jogos (1 a 3)')
        self.qtd_jogos.pack()
        self.qtd_jogos_entry = Entry(self.root)
        self.qtd_jogos_entry.pack()
        self.gerarNumeros_button = Button(self.root, text='Gerar', command=self.gerar_numeros)
        self.gerarNumeros_button.pack()
        self.limparNumeros_button = Button(self.root, text='Limpar', command=self.limpar_label)
        self.limparNumeros_button.pack()
        self.gerados_label = Label(self.root, text='')
        self.gerados_label.pack()
        self.resultado1 = Label(self.root, text=  '')
        self.resultado1.pack()
        self.resultado2 = Label(self.root, text= '')
        self.resultado2.pack()
        self.resultado3 = Label(self.root, text= '')
        self.resultado3.pack()

    def gerar_numeros(self):
        
        try:
            self.gerados_label.config(text= 'Numeros Gerados:')
            qtd_numeros = int(self.qtd_numeros_entry.get())
            qtd_jogos = int(self.qtd_jogos_entry.get())            
            if qtd_numeros >0 and qtd_numeros <21 and qtd_jogos > 0 and qtd_jogos <4: 
                for i in range(qtd_jogos):
                    numeros_gerados = []
                    separador = ' - '                       
                    while len(numeros_gerados) != qtd_numeros:
                        numero = str(randint(1,60))
                        if numero in numeros_gerados:
                            numeros_gerados.pop()
                        else:
                            numeros_gerados.append(numero)                                      
                    getattr(self, f"resultado{i+1}").config(text=separador.join(numeros_gerados))
                  
            else:
                self.resultado1.config(text=f'O valor "{qtd_numeros}" e/ou "{qtd_jogos}" não correspondem ao exemplo')
                      
        except KeyError as e :
            print(e)                        
            self.resultado1.config(text=f'O valor "{qtd_numeros}" e/ou "{qtd_jogos}" não correspondem ao exemplo')         
              
    def limpar_label(self):
        try:
            self.gerados_label.config(text= '')
            self.resultado1.config(text= '')
            self.resultado2.config(text='')
            self.resultado3.config(text='')
        except:
            pass

    def run(self):
        self.root.mainloop()
        
janela = Interface()

janela.run()

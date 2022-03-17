import sqlite3 as bd
from Projetos.Agenda_funcionarios.Agenda import Agenda

class Banco_dados_Agenda(Agenda):
    __linhas = []
    

    def __init__(self, nome, telefone, email, nome_tabela):
        
        super().__init__(nome, telefone, email)

        self.Funcionario = nome
        self.Telefone = telefone
        self.Email = email
        self.Nome_Tabela= nome_tabela

    def Criar_linhas_tabela(self):
        
        return self.__linhas.append(self.Funcionario, self.Telefone, self.Email)
    
    def Nomear_Tabela(self ):

        return  bd.connect(self.Nomear_Tabela)
    
    def Criar_banco_dado(self):

        conexão = self.Nomear_Tabela()
        cursor = conexão.cursor()
        cursor.executemany(''' insert into agenda(nome, telefone) 
        values(?,?) ''',self.Criar_linhas_tabela())
        conexão.commit()
        cursor.close()
        conexão.close()

    
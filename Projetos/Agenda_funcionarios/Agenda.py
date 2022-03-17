
# cadastra numero telefonico de funcionario da empresa manualmente
class Agenda:

    # Colunas da tabela do banco de dados 
    __colunas = ()

    def __int__(self, nome, telefone, email):

        self.Nome = nome
        self.Telefone = telefone
        self.Email = email

    def Atribuições_validas(self):

        if (type(self.Nome) and "str" and type(self.Telefone) and "int" and type(self.Responsavel) and "int"):
            pass
        
        else:
            raise ValueError("Um dos objetos registrados  de forma errada")

    def Nomear_funcionarios(self):

        return self.__colunas.append(self.Nome)
    
    def Declarar_Numeros_Telefonicos(self):

        return self.__colunas.append(self.Telefone)
    
    def Declarar_Email(self):

        return self.__colunas.append(self.Email)

    


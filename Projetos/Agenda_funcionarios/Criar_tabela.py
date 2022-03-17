from Projetos.Agenda_funcionarios.Banco_dados import Banco_dados_Agenda


Nome_da_Tabela = input("Escreva o nome da tabela")

while(True):
    try:
        nome = input("Escreva o nome do usuário Funcionario")
        
        Telefone = int(input("Escreva o numero Telefonico do Funcionario"))
        
        e_mail = input("E-mail do Funcionario")

        banco = Banco_dados_Agenda(nome, Telefone, e_mail, Nome_da_Tabela) 
        banco.Criar_linhas_tabela()
        banco.Nomear_Tabela()
        banco.Criar_banco_dado()


    except ValueError:
        print("Lembrar que o número telefônico deve possuir números de 0 a 9(Sem vírgulas, ponto e '-')")  

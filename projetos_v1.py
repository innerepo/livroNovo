#Importar a biblioteca que permite limpar a tela quando o código é executado em um terminal (nas primeiras versões ainda não existe front end)
import os
'''Controle de projetos por atividades.

    A idéia é criar uma ferramenta que armazene uma lista de projetos com suas
    respectivas atividades. Um projeto pode ter "N" atividades.'''

# Criação das variáveis que vão receber os nomes dos projetos e das atividades. São duas listas criadas vazias.
projetos=[]
atividades=[]

# Função que limpa a tela do terminal. Identifica qual o sistema operacional e executa o comando referente ao sistema utilizado.
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Função que cria novos projetos.
def cria_projeto():
''' Criar a variável projeto com o nome do projeto que será criado. Ao pressionar enter, o programa vai permitir criar um novo projeto. Nenhuma atividade é adicionada aqui.
Se a letra "q" for digitada, a criação de projetos é finalizada'''
    projeto = input('Digite o nome do Projeto ou "q" para sair: ')
    while projeto != 'q':
        projetos.append(projeto)
        print (projetos)
        projeto = input('Digite o nome do Projeto ou "q" para sair: ')

''' Criar as atividades de um projeto. É necessário informar qual o projeto em que as atividades serão inseridas, o menu exibe qual o código de cada projeto.
Depois de selecionar o projeto, as atividades podem ser inseridas, sempre pressionando "Enter" quando terminar. Ao informar a letra "q" a criação de atividades é finalizada
e o programa exibe o projeto e as suas atividades.'''
def cria_atividades():

# Identifica o código de cada projeto. O código é o número do índice na lista
    for i in range(0,len(projetos)):
        atividades.append([])
        print('Digite {} para Projeto '.format(i) + str(projetos[i]))

# Recebe o código do projeto ao qual serão associadas as atividades criadas. Na prática, não existe vínculo ainda. Isso será resolvido com a versão que tenha banco de dados
    prj = int(input('Informe para qual projeto serão as atividades: '))
    clear()

# Recebe a descrição da atividade. O texto não tem limite de tamanho, mas algo muito grande pode causar problemas de exibição.
    atividade = input('Digite a descrição da atividade: ')
    while atividade != 'q':
        atividades[prj].append (atividade)
        print (atividades[prj])
        atividade = input('Digite a descrição da atividade: ')
    return prj

#Executa o programa chamando as funções conforme a solicitação do utilizador, até que a letra "f" seja informada
status = str()
while status != 'f':
    status = input('Digite "p" para projeto, "a" para atividade ou "f" para sair: ')
    clear()
    if status == 'p':
        projeto = cria_projeto()
    elif status == 'a':
        prj = cria_atividades()
        print(projetos[prj])
        print(atividades[prj])
    elif status == 'f':
        clear()
        break

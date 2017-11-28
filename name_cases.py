'''
def imprimir(nome_pessoa):
    print('Alô {}, você gostaria de aprender um pouco '
          'de Python hoje?'.format(nome_pessoa))

nome_pessoa = 'henrique moraes'
imprimir(nome_pessoa.title())
imprimir(nome_pessoa.lower())
imprimir(nome_pessoa.upper())

print('Jesus Disse: "Eu vim para que tenham vida e vida em abundância."')
'''

famouse_person = 'Jesus'
mensagem = '"Eu vim para que tenham vida e vida em abundância."'

print(famouse_person + ': ' + mensagem)
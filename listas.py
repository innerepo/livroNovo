lista = ['minha mãe', 'meu pai', 'meu irmão', 'minha mulher', 'meus filhos']
for i in lista:
    print('Olá {}, você gostaria de jantar comigo?'.format(i))

print ('Meus pais não poderão comparecer ({} e {})'.format(lista[0],lista[1]))

lista[0]='Minhas tias'
lista[1]='Minhas sobrinhas'

for i in lista:
    print ('Olá {}, você gostaria de jantar comigo?'.format(i))

print('Encontramos uma mesa maior para o jantar, a nova lista de convidados é a seguinte:')
lista.insert(0,'Minha avó')
lista.insert(3,'Minhas tias pelo lado da minha mãe')
lista.append('Meus tios pelo lado da minha mãe')

x = 0
for i in lista:
    lista[x]=i.lower()
    x = x + 1

#print(sorted(lista))

#lista.sort(reverse=True)
for i in sorted(lista, reverse=True):
    print (i)




print ('Foram convidados: {} pessoas'.format(len(lista)))

def imprimir(param):
    print('Ops! A mesa nova não chegará a tempo. {}, sinto muito por não manter o convite'.format(param))

while len(lista) >=2:
    for i in lista:
        lista.pop(-1)
        listapop = i
        imprimir(listapop)
for i in lista:
    del lista[0]

print (lista)
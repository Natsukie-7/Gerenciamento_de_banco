# Percorra todo os vetor e quando a condição de enontrar um menor saldo for executada, guarde o índice
# Fora do laço de repetição, exclua pelo índice, por exemplo com o comando pop(índice)

class TipoUsuario:
  conta = ''
  nome = ''
  saldo = 0


def cadastrar():
  usuario = TipoUsuario()
  while len(usuario.conta) != 8 or usuario.conta.isnumeric() != True:
    usuario.conta = input('Numero da conta: ')
  usuario.nome = input('Nome: ').lower()

  return usuario


def visualizar_geral(usuarios):
  if len(usuarios) == 0:
    print('Não há usuários cadastrados!.....')

  else:
    for i in range(len(usuarios)):
      print(f'''
Nome: {usuarios[i].nome.title()}
Conta: {usuarios[i].conta[0:4]}-{usuarios[i].conta[4:8]}
Saldo: R${usuarios[i].saldo}
''')
      

def consultar(lista_usuarios):
  if len(lista_usuarios) > 0:
    resposta = 'Usuário não encontrado!..'
    conta = input('Conta a averiguar: ')
    for i in range(len(lista_usuarios)):
      if conta == lista_usuarios[i].conta:
        resposta = f'''
Nome: {lista_usuarios[i].nome.title()}
Conta: {lista_usuarios[i].conta[0:4]}-{lista_usuarios[i].conta[4:8]}
Saldo: R${lista_usuarios[i].saldo}   
'''
        break
        
  else:
    resposta = 'Error: Não há usuarios cadastrados'

  return resposta



def alterar_conta(usuarios):
  if len(usuarios) == 0:
    print('Não há usuarios para alterar')
  
  else:
    conta = input('Conta: ')
    for i in range(len(usuarios)):
      if conta == usuarios[i].conta:
        while True:
          op = int(input('Qual ação deseja realizar:\n1.Alterar o nome\n2.Modificar o saldo\n3.Sair\nEscolha: '))

          if op == 1:
            nome_antigo = usuarios[i].nome
            usuarios[i].nome = input('Insira o nome: ')
            print(f'O usuario titular da Conta: {usuarios[i].conta[0:4]}-{usuarios[i].conta[4:8]} teve seu nome alterado de\n {nome_antigo} --> {usuarios[i].nome}')

          elif op == 2:
            while True:
              resposta = int(input('O que gostaria de fazer\n1.Subtrarir o saldo\n2.Adicionar Saldo\n3.Substituir Saldo\n4.Zerar o saldo\n5.Voltar\n6.Sair\nEscolha: '))

              if resposta == 1:
                usuarios[i].saldo -= float(input(f'\nInforme o valor a retirar do saldo:\nSaldo atual: R${usuarios[i].saldo}\n-R$'))
                print(f'\nO saldo foi atualizado para: R${usuarios[i].saldo}')

              elif resposta == 2:
                usuarios[i].saldo += float(input(f'\nInforme o valor a adicionar ao saldo:\nSaldo atual: R${usuarios[i].saldo}\nR$'))
                print(f'\nO saldo foi atualizado para: R${usuarios[i].saldo}')

              elif resposta == 3:
                usuarios[i].saldo = float(input(f'\nInforme o valor para por ao saldo:\nSaldo atual: R${usuarios[i].saldo}\nR$'))
                print(f'\nO saldo foi atualizado para: R${usuarios[i].saldo}')

              elif resposta == 4:
                usuarios[i].saldo = 0
                print(f'\nO saldo foi atualizado para: R${usuarios[i].saldo}')

              elif resposta == 5:
                break

              elif resposta == 6:
                op = 3
                break

              else:
                print('error: Opção invalida!....\n')

          elif op == 3:
            break

          else:
            print('error: Opção invalida!....\n')
  return usuarios


def excluir_menor_saldo(usuarios):
  if len(usuarios) == 0:
    print('Não há usuarios para excluir\n')

  else:
    lista_saldos = []

    for i in range(len(usuarios)):
      lista_saldos.append(usuarios[i].saldo)

    MenorValor = min(lista_saldos)
    posicao_MenorValor = lista_saldos.index(MenorValor)
    usuario_removido = usuarios.pop(posicao_MenorValor)
    print(f'''

Remoção da conta: {usuario_removido.conta}
Titular: {usuario_removido.nome}
Saldo: {usuario_removido.saldo}

''')

  return usuarios
    


def main():
  lista_de_usuarios = []

  while True:
    item_menu = int(input(f'''
Menu de opções:

  1.Cadastrar contas
  2.Visualizar todas as contas
  3.Consultar pelo numero da conta
  4.Alterar nome e/ou saldo de um número de conta
  5.Excluir a conta com menor saldo
  6.Sair
'''))
    print()
    if item_menu == 1:
      if len(lista_de_usuarios) <= 15:
        lista_de_usuarios.append(cadastrar())

      else:
        print('Error: Limite de usuarios atingido!.....')

    elif item_menu == 2:
      visualizar_geral(lista_de_usuarios)

    elif item_menu == 3:
      print(consultar(lista_de_usuarios))

    elif item_menu == 4:
      lista_de_usuarios = alterar_conta(lista_de_usuarios)

    elif item_menu == 5:
      lista_de_usuarios = excluir_menor_saldo(lista_de_usuarios)

    elif item_menu == 6:
      print('Finalizando sistema....')
      break
    
    else:
      print('Error: Opção aderida invalida, tente uma listada abaixo!....')


main()
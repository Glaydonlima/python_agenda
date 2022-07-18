AGENDA ={}
AGENDA['EXEMPLO1'] = {
    'telefone':'98000-9000',
    'email':'exemplo1@hotmail.com',
    'endereco':'av:1',
}
AGENDA['EXEMPLO2'] = {
    'telefone':'98100-9100',
    'email':'exemplo2@gmail.com',
    'endereco':'av:2',}
AGENDA['EXEMPLO3'] = {
    'telefone':'98200-9200',
    'email':'exemplo3@gmail.com',
    'endereco':'av:3',}

def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone', AGENDA[contato]['telefone'])
    print('E-mail', AGENDA[contato]['email'])
    print('Endereço', AGENDA[contato]['endereco'])

def mostrar_contatos():
    for contato in AGENDA:
     buscar_contato(contato)
     print('--------------------------------------')

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    'telefone':telefone,
    'email':email,
    'endereco':endereco,
    }
    print('Contato {} adcionado/editado com sucesso'.format(contato))

def excluir_contato(contato):
    AGENDA.pop(contato)
    print('Contato excluido com sucesso')
    print('----------------------------')

def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - incluir contato')
    print('4 - editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')

imprimir_menu()
opcao = input("Escolha uma opção:")

if opcao == "1":
    mostrar_contatos()
elif opcao =="2":
    contato = input('Digite o nome do contato:')
    buscar_contato(contato)
elif opcao =="3" or opcao == "4":
    contato = input('Digite o nome do contato:')
    telefone = input('Digite o numero do telefone:')
    email = input('Digite o nome do email:')
    endereco = input('Digite o nome do endereço:')
    incluir_editar_contato(contato, telefone, email, endereco)
elif opcao =="5":
    contato = input('Digite o nome do contato:')
    excluir_contato(contato)
elif opcao =="0":
    print("Fechando agenda...")
    pass
else:
    print('Opção invalida')




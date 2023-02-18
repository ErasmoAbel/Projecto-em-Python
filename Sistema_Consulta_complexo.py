opcaoEscolhida = [1, 2, 3, 4, 5, 6, 7]
opcoes = [1, 2]
print("1.Transferir dinheiro")
print("2.Levantar diheiro no agente")
print("3.Levantar no ATM")
print("4.Pagamento de servicos")
print("5.Solicitar o codigo de levantamento")
print("6.Mudar o PIN")
print("7.Minha conta")
print(" ")

while True:
    servico = input("Porfavor seleccione uma opção: ")

if (opcaoEscolhida[0] == int(servico)):
    input("Digite o numero de telefone: ")
    input("Digite o valor: ")
    input("Digite o teu PIN: ")
    print("1.Confirmar")
    print("2.Cancelar")
    confirmar = input("Opcao 1 ou 2: ")
    if (opcoes[0] == int(confirmar)):
       print("Confirmado com sucecesso.")
    elif (opcoes[1] == int(confirmar)):
       print("Operacao cancelada.")
    else:
       print("Opcao invalida.")
elif (opcaoEscolhida[1] == int(servico)):
    input("Digite o codigo do agente: ")
    input("Digite o valor: ")
    input("Digite o teu PIN: ")
    print("1.Confirmar")
    print("2.Cancelar")
    confirmar = input("Opcao 1 ou 2: ")
    if (opcoes[0] == int(confirmar)):
       print("Confirmado com sucecesso.")
    elif (opcoes[1] == int(confirmar)):
       print("Operacao cancelada.")
    else:
       print("Opcao invalida.")
elif (opcaoEscolhida[2] == int(servico)):
    print("Sucesso! Opção 3 selecionada.")
elif (opcaoEscolhida[3] == int(servico)):
    print("Sucesso! Opção 4 selecionada.")
elif (opcaoEscolhida[4] == int(servico)):
    print("Sucesso! Opção 5 selecionada.")
elif (opcaoEscolhida[5] == int(servico)):
    input("Digite o PIN actual: ")
    input("Digite o o novo PIN: ")
    input("Repita o novo PIN: ")
    print("1.Confirmar")
    print("2.Cancelar")
    confirmar = input("Opcao 1 ou 2: ")
    if (opcoes[0] == int(confirmar)):
       print("Confirmado com sucecesso.")
    elif (opcoes[1] == int(confirmar)):
       print("Operacao cancelada.")
    else:
       print("Opcao invalida.")
elif (opcaoEscolhida[6] == int(servico)):
    print("1.Verificar saldo")
    print("2.Ultima operacao")
    print("3.Transferencia para numero errado")
    print("4.Extrato da conta")
    print("5.Meus dados pessoais")
    print("")
    servico = input("Selecione uma opcao: ")
else:
    print("Opção inválida!")
print("")
quit(input("Precione para sair: "))


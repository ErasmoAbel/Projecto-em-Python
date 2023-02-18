opcaoEscolhida = [1, 2, 3, 4, 5, 6, 7]
print("1.Transferir dinheiro")
print("2.Levantar diheiro no agente")
print("3.Levantar no ATM")
print("4.Pagamento de servicos")
print("5.Solicitar o codigo de levantamento")
print("6.Mudar o PIN")
print("7.Minha conta")
print(" ")
servico = input("Porfavor seleccione uma opção: ")

if (opcaoEscolhida[0] == int(servico)):
    print("Sucesso! Opção 1 selecionada.")
elif (opcaoEscolhida[1] == int(servico)):
    print("Sucesso! Opção 2 selecionada.")
elif (opcaoEscolhida[2] == int(servico)):
    print("Sucesso! Opção 3 selecionada.")
elif (opcaoEscolhida[3] == int(servico)):
    print("Sucesso! Opção 4 selecionada.")
elif (opcaoEscolhida[4] == int(servico)):
    print("Sucesso! Opção 5 selecionada.")
elif (opcaoEscolhida[5] == int(servico)):
    print("Sucesso! Opção 6 selecionada.")
elif (opcaoEscolhida[6] == int(servico)):
    print("Sucesso! Opção 7 selecionada.")
else:
    print("Opção inválida!")

print("")
quit(input("Precione ENTER para sair: "))

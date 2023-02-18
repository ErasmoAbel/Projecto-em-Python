confirm = input("Porfavor digite sim para continuar: ")
dados_pessoais = ["nome", "idade", "senha", "sobrenome", "profissao",
                  "morada", "telefone"]

tentativas = 2
if(confirm == "sim"):
    dados_pessoais[0] = input("Digite o teu nome: ")
    dados_pessoais[1] = input("Digite o teu sobrenome: ")
    dados_pessoais[2] = input("Digite a tua idade: ")
    dados_pessoais[3] = input("Digite a tua profissao: ")
    dados_pessoais[4] = input("Digite a tua morada: ")
    dados_pessoais[5] = input("Digite o teu telefone: ")
    dados_pessoais[6] = input("Digite a senha porfavor: ")
#    if (int(dados_pessoais[6]) != 844013):
#        dados_pessoais[6] = input("Senha incorrecta, digite novamente: ")
else:
    while(tentativas >= 0):
        tentativas = tentativas - 1
        print(input("Resposta incorrecta, digite novamente: "))
        
#input("Precione qualquer tecla para sair: ")
    
if (int(dados_pessoais[2]) <= 17) or (int(dados_pessoais[6]) == 844013):
    print("O usuario menor de idade ou senha incorrecta.")
elif (int(dados_pessoais[2]) > 17) or (int(dados_pessoais[6]) != 844013):
    print("O usuario menor de idade ou senha incorrecta.")
elif (int(dados_pessoais[2]) >= 17) and (int(dados_pessoais[6]) == 844013):
    print("Autenticado com sucesso.")
elif (int(dados_pessoais[2]) >= 17) or (int(dados_pessoais[6]) == 844013):
    print("Autenticado com sucesso.") 
else:
    print("Usuario nao reconhecido no sistema")

print("Os teus dados sao: ")
print(dados_pessoais)

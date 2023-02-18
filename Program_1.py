confirm = input("Porfavor digite sim para continuar: ")
dados_pessoais = ["nome", "idade", "senha", "sobrenome", "profissao",
                  "morada", "telefone"]

tentativas = 2
while(tentativas >= 0):
    tentativas = tentativas - 1
if(confirm == "sim"):
    dados_pessoais[0] = input("Digite o teu nome: ")
    dados_pessoais[1] = input("Digite o teu sobrenome: ")
    dados_pessoais[2] = input("Digite a tua idade: ")
    dados_pessoais[3] = input("Digite a tua profissao: ")
    dados_pessoais[4] = input("Digite a tua morada: ")
    dados_pessoais[5] = input("Digite o teu telefone: ")
    dados_pessoais[6] = input("Digite a senha porfavor: ")

if (int(dados_pessoais[2]) <= 16):
    print("O usuario menor de idade.")
elif (int(dados_pessoais[2]) <= 17) or (int(dados_pessoais[2]) >= 18):
    print("Autenticado com sucesso.")
    print("Os teus dados sao: ")
    print(dados_pessoais)
else:
    confirm = print(input("Resposta incorrecta, digite novamente: "))
    print("Usuario nao reconhecido no sistema")

input("Precione qualquer tecla para sair: ")

def dadosPessais(name, morada):
    name = input("Teu nome por favor: ")
    morada = input("Tua morada por favor: ")
    dados = name, morada
    return dados
quit()

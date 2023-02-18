filename = input("Qual e o nome do ficheiro? ")
content = input("Digite o conteudo do ficheiro: ")

with open(filename, 'w') as file:
    file.write(content)
open_file = input("Gostaria de abrir o ficheiro? ")
if open_file in ['sim', 'nao']:
    if open_file == 'sim':
        with open(filename, 'r') as file:
            print(file.read())
else:
    print("Opcao invalida")

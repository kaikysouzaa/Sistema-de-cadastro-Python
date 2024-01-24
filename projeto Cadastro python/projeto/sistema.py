from projeto.funcoes import *
lista = []
interface()
while True:
    try:
        opc = int(input("Qual sua opção? "))
        print("-"*40)
        if opc == 1:
            nome = str(input("Nome do usuário: ")).capitalize().strip()
            idade = tratamento("Idade do Usuário: ")
            lista.append((nome, idade))  #armazena como tupla dentro da lista
            print(f"\033[32mUsuário {nome} cadastrado com sucesso!\033[m")
        elif opc == 2:
            if not lista:
                print("Nenhum usuário cadastrado!")
            else:
                for nome, idade in lista:
                    usuario_dados = f"{nome} - {idade} Anos"
                    print(usuario_dados)
        elif opc == 3:
            print("Finalizando... e gerando o arquivo txt")
            with open("arquivo.txt", "w") as arquivo:
                for nome, idade in lista:
                    arquivo.write(nome + "\n")
                    arquivo.write(str(idade) + "\n")
            break
        else:
            print("\033[0;31mErro! Marque uma opção válida\033[m")
    except (ValueError):
        print("-"*40)
        print("\033[0;31mErro! Por favor, insira um número inteiro.\033[m")

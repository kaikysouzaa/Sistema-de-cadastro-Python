def interface():
    print("-"*40)
    print(f"{'Sistema de cadastro:'}".center(35))
    print("-"*40)
    print("1 - Cadastrar usuário")
    print("2 - Mostrar todos os usuários")
    print("3 - Encerrar programa")

def tratamento(idade = "Não informado"):
    ok = False
    valor = 0
    n = str(idade)
    while True:
        n = str(input(idade))
        if n.isnumeric():  # verifica se n é número
            valor = n
            ok = True
        else:
             print("\033[0;31mERRO! digite uma idade válida!\033[m")  # se não dá erro e manda perguntar novamente
             ok = False  # lógica falsa
        if ok == True:
            break
    return valor





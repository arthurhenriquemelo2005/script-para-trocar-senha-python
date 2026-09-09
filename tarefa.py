print ("=== TELA DE LOGIN ===")


senhaFixa = "1234"
while True:

    print("[1] tela de login")
    print("[2] trocar senha")
    print("[3] Sair")

    opcao = input("informe qual área você quer entrar: ")

    if opcao == "1":
        
        loginUsuario = input("Informe o seu login: ")
        senhaUsuario = input("Informe a sua senha: ")

        if loginUsuario == "admin" and senhaUsuario == senhaFixa:
            print("Acesso liberado!")
           
        else:
            print("Acesso negado. Usuário ou senha incorretos.")

    if opcao == "2":
        mudarSenha = input(str("Você quer mudar de senha? [S/N]"))

        if mudarSenha == "S":

            novaSenha = input(str("Adicione sua nova senha: "))
            senhaFixa = novaSenha

            print("Nova senha realizada sua senha agora é: ", novaSenha)

    if opcao == "3":
        print("Saindo...")
        break
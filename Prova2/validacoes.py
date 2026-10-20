def validar_senha(senha):
    senha_validada = str
    if  len(senha) <= 3:
        senha_validada = "Senha deve possuir mais de 3 caracteres!"
    elif len(senha) > 100:
        senha_validada = "Por favor digite uma senha menor que 100!"
    else:
        senha_validada = "Senha Válida!"

    return senha_validada
    
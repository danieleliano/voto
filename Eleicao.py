def poder_de_voto():
    idade = int(input("Informe a idade do eleitor: "))
    if idade >= 0 and idade < 16:
        print(f"Eleitor com {idade} ano(s), não tem direito a voto ainda.")
    elif idade >= 16 and idade < 18 or idade >= 70:
        print(f"Eleitor com {idade} ano(s), voto facultativo.")
    elif idade >= 18 and idade < 70:
        print(f"Eleitor com {idade} ano(s), voto obrigatório.")
    else:
        print(f"A idade informada é inválida. Não é possível ter {idade} ano(s)")

poder_de_voto()
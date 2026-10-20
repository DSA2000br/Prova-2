def calculo_de_frete(distancia, peso):
    if distancia <= 100:
       taxa = 1.5*peso
    else:
       taxa = 2*peso
    return taxa

print(calculo_de_frete(61, 69))
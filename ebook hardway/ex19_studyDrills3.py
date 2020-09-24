def quantidade_racao_diaria(peso_cachorro, tamanho_racao):
    print "Vamos calcular a quantidade ideal de comida que seu cachorro deve receber por dia"
    print "Seu cachorro pesa %d gramas." % peso_cachorro
    #vamos adotar que a quantidade de racao deve ser 5% do peso do animal
    qnt_racao = peso_cachorro * 0.05
    print "Um cachorro com esse peso deve receber %f kilos" % qnt_racao
    dias_pacote = tamanho_racao / qnt_racao
    print "Seu pacote de racao ira durar %f dias" % dias_pacote

quantidade_racao_diaria(24, 15)
def calculatePointsValue(points, stock_code, number_contract):
    if stock_code == 1 or stock_code == 3:
            if stock_code == 1:
                valueReais = points * 0.2 * number_contract
            else:
                valueReais = points * 5 * number_contract
    elif stock_code == 2 or stock_code == 4:
            if stock_code == 2:
                valueReais = points * 10 * number_contract
            else:
                valueReais = points * 250 * number_contract

    return valueReais

print "Vamos transformar o valor de pontos para reais"
print "Para WIN = 1, WDO = 2, IND = 3, DOL = 4"

resultado = calculatePointsValue(100, 1, 3)
print resultado
    
   
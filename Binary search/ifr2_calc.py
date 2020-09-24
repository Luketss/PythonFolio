#receber plano, estrategia, lote, caixa,

plans = {
    "lite": 99,
    "pro": 299,
    "expert": 799,
    "advanced": 1399
}

ifr2 = {
    "silver": 239,
    "gold": 389
}

def calculate_strategy_costs(strategy_id, plan_id):
    if plan_id == 1: #plano lite
        if strategy_id == 1:
            return plans["lite"] + ifr2["silver"]
        elif strategy_id == 2:
            return plans["lite"] + ifr2["gold"]
        else:
            print "Estrategia nao existe"
    elif plan_id == 2: #plano pro
        if strategy_id == 1:
            return plans["pro"] + ifr2["silver"]
        elif strategy_id == 2:
            return plans["pro"] + ifr2["gold"]
        else:
            print "Estrategia nao existe"
    elif plan_id == 3: #plano expert
        if strategy_id == 1:
            return plans["expert"] + ifr2["silver"]
        elif strategy_id == 2:
            return plans["expert"] + ifr2["gold"]
        else:
            print "Estrategia nao existe"
    elif plan_id == 4: #plano advanced
        if strategy_id == 1:
            return plans["advanced"] + ifr2["silver"]
        elif strategy_id == 2:
            return plans["advanced"] + ifr2["gold"]
        else:
            print "Estrategia nao existe"
    else:
        print "Plano não existe"

custo = calculate_strategy_costs(3, 1)

print custo
from random import randint

km = 'Камень'
bm = 'Бумага'
ng = 'Ножницы'


async def game_1():
    d = [km, bm, ng]
    return d[randint(0, 2)]


async def result(pleyer_sms, comp_sms):
    if pleyer_sms == comp_sms:
        return 'У нас ничья'
    elif (pleyer_sms == km and comp_sms == ng) or (pleyer_sms == bm and comp_sms == km) or (
            pleyer_sms == ng and comp_sms == bm):
        return 'Поздровляю. Ты победил'
    else:
        return 'Извини ты проиграл. Попробуй в следущий раз'
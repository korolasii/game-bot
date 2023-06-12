from random import randint


async def bot_kybiki():
    b = [randint(1, 6), randint(1, 6)]
    a = sum(b)
    return [b, a]


async def pleyer_kybiki():
    d = [randint(1, 6), randint(1, 6)]
    v = sum(d)
    return [d, v]


async def result_kybiki(b_kybiki , k_kybiki):
    if  b_kybiki > k_kybiki:
        return 'Поздравляю ты выйграл.'
    elif b_kybiki < k_kybiki:
        return 'Ты проиграл, попробуй в следущий раз.'
    else:
        return 'У нас ничья.'
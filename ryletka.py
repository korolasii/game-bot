from random import randint

red = 'Красный'
black = 'Черный'


async def pleyer_ryletka(pleyer_sms_ryletka):
    a = randint(0, 36)
    b = {
        1: red,
        2: black,
        3: red,
        4: black,
        5: red,
        6: black,
        7: red,
        8: black,
        9: red,
        10: black,
        11: black,
        12: red,
        13: black,
        14: red,
        15: black,
        16: red,
        17: black,
        18: red,
        19: red,
        20: black,
        21: red,
        22: black,
        23: red,
        24: black,
        25: red,
        26: black,
        27: red,
        28: black,
        29: black,
        30: red,
        31: black,
        32: red,
        33: black,
        34: red,
        35: black,
        36: red}
    c=[a,b.get(a)]
    if (a % 2 == 0 and pleyer_sms_ryletka == 'Чётная') or (a % 2 != 0 and pleyer_sms_ryletka == 'Нечётная') \
            or (pleyer_sms_ryletka == a) or (pleyer_sms_ryletka == b.get(a)):
        return ['Поздравляю, ты выиграл.',c]
    else:
        return ['К сожелению ты проиграл.',c]

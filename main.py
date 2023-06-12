from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
import configure
from game_kmd import game_1, result
from kybiki import bot_kybiki, pleyer_kybiki, result_kybiki
from ryletka import pleyer_ryletka

km = 'Камень'
bm = 'Бумага'
ng = 'Ножницы'

data = {
    'peaper_kmb': bm,
    'stone': km,
    's_1': ng
}

bot = Bot(token=configure.config['token'])
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def del_InLineKeyboard(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)


async def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_info = types.KeyboardButton('Info')
    item_1 = types.KeyboardButton('Камень ножницы бумага')
    item_2 = types.KeyboardButton('Рулетка')
    item_3 = types.KeyboardButton('Кубики')
    keyboard.row(item_1, item_2, item_3)
    keyboard.row(item_info)
    return keyboard


async def keyboard_back():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_back = types.KeyboardButton('Назад')
    keyboard.add(item_back)
    return keyboard


async def inline_keyboard_kmb():
    keyboard = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton('Да', callback_data='yes_kmb')
    item_no = types.InlineKeyboardButton('Нет', callback_data='no_kmb')
    keyboard.add(item_yes, item_no)
    return keyboard


async def keyboard_kmb():
    keyboard = types.InlineKeyboardMarkup()
    item_b = types.InlineKeyboardButton(bm, callback_data='peaper_kmb')
    item_k = types.InlineKeyboardButton(km, callback_data='stone')
    item_n = types.InlineKeyboardButton(ng, callback_data='s_1')
    keyboard.add(item_b, item_k, item_n)
    return keyboard


async def keyboard_kybiki():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_get = types.KeyboardButton('Бросить кубики.')
    keyboard.add(item_get)
    return keyboard


async def keyboard_ryletka_start():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_color = types.KeyboardButton('Красный или черный')
    item_numbre = types.KeyboardButton('Определённая цифра')
    item_chet = types.KeyboardButton('Чётная или нечётная')
    keyboard.add(item_color, item_chet, item_numbre)
    return keyboard


async def keyboard_ryletka_color():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_red = types.KeyboardButton('Красный')
    item_black = types.KeyboardButton('Черный')
    keyboard.add(item_red, item_black)
    return keyboard


async def keyboard_ryletka_chet():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_red = types.KeyboardButton('Чётная')
    item_black = types.KeyboardButton('Нечётная')
    keyboard.add(item_red, item_black)
    return keyboard


async def keyboard_kybiki_answer():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_red = types.KeyboardButton('Да, пожалуйста')
    item_black = types.KeyboardButton('Нет, спасибо')
    keyboard.add(item_red, item_black)
    return keyboard


async def keyboard_ryletka_answer():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_red = types.KeyboardButton('Да, конечно')
    item_black = types.KeyboardButton('Нет, спасибо')
    keyboard.add(item_red, item_black)
    return keyboard


@dp.callback_query_handler(lambda call: True)
async def answer(call: types.CallbackQuery):
    await del_InLineKeyboard(call)
    
    if call.data == 'yes_kmb':
        await bot.send_message(call.message.chat.id, 'Выбери камень, ножницы или бумагу.', reply_markup=await keyboard_kmb())
    elif call.data == 'no_kmb':
        await bot.send_message(call.message.chat.id, 'Выбери пункт меню.', reply_markup=await start_keyboard())
    elif call.data in ['peaper_kmb', 'stone', 's_1']:
        global pleyer_sms
        pleyer_sms = call.data
        await bot.send_message(call.message.chat.id, f"Ты выбрал {data[call.data]}.", reply_markup=await keyboard_back())
        comp_sms = await game_1()
        await bot.send_message(call.message.chat.id, f"Я выбрал {comp_sms}.")
        await bot.send_message(call.message.chat.id, await result(data[call.data], comp_sms))
        await bot.send_message(call.message.chat.id, 'Хочешь ещё поиграть?', reply_markup=await inline_keyboard_kmb())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    b = await start_keyboard()
    await message.reply('Привет. Выбери пункт меню.', reply_markup=b)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def get(message: types.Message):
    if message.text == 'Info':
        await message.reply('Я игровой бот. К сожелению у меня есть только три игры.', reply_markup= await keyboard_back())
    elif message.text == 'Назад':
        await message.reply('Выбери пункт меню.', reply_markup= await start_keyboard())
    elif message.text == 'Камень ножницы бумага':
        await message.reply('Отлично начинаем игру.', reply_markup= await keyboard_back())
        await message.reply('Выбери камень ножници или бумага.', reply_markup= await keyboard_kmb())
    elif message.text == 'Кубики':
        await message.reply('Бросте кубики.', reply_markup= await keyboard_kybiki())
    elif message.text == 'Бросить кубики.':
        a_kybiki, b_kybiki = await pleyer_kybiki()
        v_kybiki, k_kybiki = await bot_kybiki()
        await message.reply(f'Тебе выпало - {a_kybiki[0]} {a_kybiki[1]}. В суме у тебя  {b_kybiki}.', reply_markup= await keyboard_back())
        await message.reply(f'Мне выпало - {v_kybiki[0]} {v_kybiki[1]}. В суме у меня  {k_kybiki}.', reply_markup=await keyboard_back())
        await message.reply(await result_kybiki(b_kybiki, k_kybiki), reply_markup=await keyboard_back())
        await message.reply('Не желаете сыграть ещё раз?', reply_markup=await keyboard_kybiki_answer())
    elif message.text=='Да, пожалуйста':
        await message.reply('Бросить кубики.', reply_markup= await keyboard_kybiki())
    elif message.text == 'Рулетка':
        await message.reply('Выберете тип ставки.', reply_markup= await keyboard_ryletka_start())
    if message.text == 'Красный или черный':
        await message.reply('Выберете цвет.', reply_markup= await keyboard_ryletka_color())
    elif message.text == 'Определённая цифра':
        await message.reply('Введите число от 0 и до 36.', reply_markup= await keyboard_back())
    elif message.text == 'Чётная или нечётная':
        await message.reply('Выберете вариант', reply_markup= await keyboard_ryletka_chet())
    elif message.text in ['Красный', 'Черный', 'Чётная', 'Нечётная', '0', '1', '2', '3', '4', '5', '6', '8', '9', '10',
                      '11', '12', '13', '14', '15', '16', '18', '19', '20', '21', '22', '23', '24', '25', '26', '28',
                      '29', '30', '31', '32', '33', '34', '35', '36', '7', '17']:
        global pleyer_sms_ryletka
        pleyer_sms_ryletka = message.text
        w = await pleyer_ryletka(pleyer_sms_ryletka)
        await message.reply(f'На колесе выпало - {w[1][0]}, {w[1][1]}', reply_markup=await keyboard_back())
        await message.reply(w[0], reply_markup=await keyboard_back())
        await message.reply('Не желаете сыграть ещё раз?', reply_markup= await keyboard_ryletka_answer())
    elif message.text== 'Да, конечно':
        await message.reply('Выберете тип ставки.', reply_markup= await keyboard_ryletka_start())
    elif message.text == 'Нет, спасибо':
        await message.reply('Приходите ещё.', reply_markup= await start_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

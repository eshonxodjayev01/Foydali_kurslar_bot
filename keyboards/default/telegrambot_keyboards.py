from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
botmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#01 Kurs haqida'),
            KeyboardButton(text='#02 Kerakli dasturlar'),
        ],
        [
            KeyboardButton(text='#03 Python va Pycharm o\'rnatamiz'),
            KeyboardButton(text='#04 Terminalda ishalsh'),
        ],
        [
            KeyboardButton(text='#05 Dasturlash metodologiyasi'),
            KeyboardButton(text='#06 botFather'),
        ],
        [
            KeyboardButton(text='#07 Aiogram bilan tanishamiz'),
            KeyboardButton(text='#08 Wikibot'),  #txt
        ],
        [
            KeyboardButton(text='#09 API nima?'),
            KeyboardButton(text='#10 Bot uchun Api lar'), #txt 2x
        ],
        [
            KeyboardButton(text='#11 Pythonda Api bilan ishlash'), #txt 2x
            KeyboardButton(text='#12 SpeakEnglish bot')
        ],
        [
            KeyboardButton(text='#13 So\'zlarning xatosini tekshirish'),
            KeyboardButton(text='#14 imloBot dasturi'),
        ],
        [
            KeyboardButton(text='#15 Botni Heroku serveriga yuklash'), #txt
            KeyboardButton(text='#16 Endi nima?'),
        ],
        [
            KeyboardButton(text='Menu⬇️'),
        ],
    ],
)


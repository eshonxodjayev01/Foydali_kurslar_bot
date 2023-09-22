from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='FrontEnd🌐'), #done
            KeyboardButton(text='BackEnd🖥'),
        ],
        [
            KeyboardButton(text='HTML'),  #done
            KeyboardButton(text='Flutter (Android📱)'), #done
        ],
        [
            KeyboardButton(text='Telegram bot🤖'), #done
            KeyboardButton(text='Kotlin⌨️'),  #done
        ],
        [
            KeyboardButton(text='React JS Full-Stack💻'), #done
            KeyboardButton(text=''),
        ],
    ],
    resize_keyboard=True
)
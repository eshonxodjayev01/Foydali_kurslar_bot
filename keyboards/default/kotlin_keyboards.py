from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kotlinmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#01 Kotlin dasturlash asoslari'),
            KeyboardButton(text='#02 Kotlin OOP'),
        ],
        [
            KeyboardButton(text='#03 Kotlin Collections'),
            KeyboardButton(text='#04 Kotlin Advanced'),
        ],
        [
            KeyboardButton(text='Menu⬇️'),
        ]
    ],
    resize_keyboard=True
)

basickotlinmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#00 Kirish'),
            KeyboardButton(text='#01 O\'zgaruvchilar, ma\'lumot turlari'),
        ],
        [
            KeyboardButton(text='#02 Char,Boolean,String'),
            KeyboardButton(text='#03 Ma\'lumot tulari'),
        ],
        [
            KeyboardButton(text='#04 Matematik amallarni bajarish'),
            KeyboardButton(text='#05 Matematik funksiyalar ustida ishlash'),
        ],
        [
            KeyboardButton(text='#06 Shart operatorlari'),
            KeyboardButton(text='#07 Shart operatori ustida ishlash'),
        ],
        [
            KeyboardButton(text='#08 When operatori'),
            KeyboardButton(text='#09 Range-Oraliq funksiya'),
        ],
        [
            KeyboardButton(text='#09 When operatori ustida ishlash'),
            KeyboardButton(text='#10'),
        ],
        [
            KeyboardButton(text='#11 Sikl Operatori'),
            KeyboardButton(text='#12 Sikr Operatori 2-qism'),
        ],
        [
            KeyboardButton(text='#13 Break va Continue'),
            KeyboardButton(text='#14 Array-Massivlar'),
        ],
        [
            KeyboardButton(text='#15 Ko\'p o\'lchovli massivlar'),
            KeyboardButton(text='#16 Ko\'p o\'lchovli massivlarda ishlash'),
        ],
        [
            KeyboardButton(text='#17 Stringlar'),
            KeyboardButton(text='#18 Stringlar ustida amallar'),
        ],
        [
            KeyboardButton(text='#17 Funksiyalar'),
            KeyboardButton(text='#18 Rekursiyaviy funksiyalar'),
        ],
        [
            KeyboardButton(text='#17 Xatoliklar-Exceptions'),
            KeyboardButton(text='Ortga'),
        ],
    ],
    resize_keyboard=True
)

oopkotlinmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#00 OOP tushunchasi'),
            KeyboardButton(text='#01 Vorislik'),
        ],
        [
            KeyboardButton(text='#02 Encapsulation'),
            KeyboardButton(text='#03 Abstaction'),
        ],
        [
            KeyboardButton(text='#04 Polymorphism'),
            KeyboardButton(text='#05 Data class'),
        ],
        [
            KeyboardButton(text='#06 Nested va Inner classlar'),
            KeyboardButton(text='#07 Sealed class'),
        ],
        [
            KeyboardButton(text='#08 Enum class'),
            KeyboardButton(text='#09 Object va Companion object'),
        ],
        [
            KeyboardButton(text='#10 Generics'),
            KeyboardButton(text='Ortga'),
        ],
    ],
    resize_keyboard=True
)

collectionskotlinmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#01 Listlar'),
            KeyboardButton(text='#02 Setlar'),
        ],
        [
            KeyboardButton(text='#03 Maplar'),
            KeyboardButton(text='Ortga'),
        ],
    ],
    resize_keyboard=True
)

advancedkotlinmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#01 Extension funksiyalar'),
            KeyboardButton(text='#02 Filelar'),
        ],
        [
            KeyboardButton(text='#03 Lateinit va Lazy'),
            KeyboardButton(text='#04 Equals va hashCode'),
        ],
        [
            KeyboardButton(text='#05 Scope Functions'),
            KeyboardButton(text='Ortga'),
        ],
    ],
    resize_keyboard=True
)
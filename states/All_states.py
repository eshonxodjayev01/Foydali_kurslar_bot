from aiogram.dispatcher.filters.state import StatesGroup, State

class Send(StatesGroup):
    backend = State()
    flutter = State()
    frontend = State()
    kotlin = State()
    bot = State()

class BackEnd(StatesGroup):
    python = State()
    java = State()

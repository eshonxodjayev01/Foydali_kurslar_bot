from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_keyboards import menu
from loader import dp


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message,state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu)
    await state.finish()

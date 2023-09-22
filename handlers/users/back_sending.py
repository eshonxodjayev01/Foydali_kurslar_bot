from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_keyboards import menu
from keyboards.default.backend_keyboards import backmenu,basicmenuBack,oopmenuback
from keyboards.default.flutter_keyboards import fluttermenu
from keyboards.default.frontend_keyboards import basicFront,menuHtml,menucss,menucss2,menujs
from keyboards.default.kotlin_keyboards import kotlinmenu,basickotlinmenu,oopkotlinmenu,collectionskotlinmenu,advancedkotlinmenu
from keyboards.default.telegrambot_keyboards import botmenu
from loader import dp
from states import All_states
from states.All_states import Send,BackEnd

@dp.message_handler(text='Dasturlash asoslari',state=BackEnd.python)
async def sendpython(message: Message):
    photo_url = 'AgACAgIAAxkBAAIFcGSxxs6rYNdOLyilrMFRIWJhQ_vcAAIO0DEb9wGRSZuyRMYWzweXAQADAgADeAADLwQ'
    video_id = 'BAACAgIAAxkBAAIFOWSxwIEFjrFPjZgxXirZJHIRobnLAAKiHwACx_p5SFDen2rcSheMLwQ'
    await message.answer_photo(photo=photo_url,caption="<b>Keling tanishamiz</b>\n\n<b>Anvar Narzullayev</b>\n\n"
                         "<b>University Sains Islam Malaysia</b> oliygohining Axborot Texnologiyalari kafedrasida yetakchi mutaxassis lavozimida ishlayman. Raqamli Texnologiyalar, Kompyuter Arxitekturasi, Axborot Xavfsizligi fanlaridan dars beraman.\n\n"
                         "2004 yilda <b>Toshkent Axborot Texnologiyalar Universitetini Telekommunikatsiya yo'nalishini</b> bitirganman.\n\n"
                         "2006 yilda <b>Janubiy Koreyaning Yeungnam Universitetida Axborot Texnologiyalari Muhandisi</b> yo'nalishida <b>Magistrlik</b>, 2012 yilda esa shu oliygohda Doktorlik <b>(PhD)</b> unvonini himoya qilganman.\n\n"
                         "2013 yildan beri Malayziyaning turli oliy o'quv yurtlarida <b>Computer Science</b> va <b>Axborot Texnologiyalari</b> yo'nalishlarida dars berib kelaman.\n\n"
                         "Birinchi professional dasturimni 13 yoshda yozganman. Turli yillar davomida <b>C, C++, Delphi, Matlab, Java va Python </b>tillaridan foydalanib kelganman.\n\n"
                         "Oxirgi yillarda asosan ikki yo'nalishda ilmiy izlanishlar qilaman: <b>IoT (Internet of things)</b> va <b>AI (Artificial Intelligence)</b>.\n\n"
                         "<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>Websayt</a>")
    await message.answer_video(video=video_id,caption="<b>Dasturlash asoslari. Kirish so'z</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️",reply_markup=basicmenuBack)


@dp.message_handler(text="Darslarni o'zlashtirish", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIFnWSxyKcWxB3_EnIoo-uag2bpjDKcAAKVCgACoSfpSROkzqCV4XrJLwQ'
    await message.answer_video(video=video_id, caption="<b>Darslarni qanday o'zlashtiramiz</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#00 Kerakli dasturlar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIFqmSxyVCJsO3SEvwn1a4Lzb__WwnqAALRCwACO564SX1bHmeo-0FwLwQ'
    await message.answer_video(video=video_id, caption="<b>#00 Kerakli dasturlar</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#01 Hello World!", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIF_2SyOreb4NTfbmbLiCFthWYhRHfwAAJaDQAC7yywSeB3fzSYaNnALwQ'
    await message.answer_video(video=video_id, caption="<b>#01 Hello World!</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#02 print(),sinteks", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGAWSyOsdP2edRCighdea1QKa1qrNoAAIQCQACI9vRSRe1UGlFJPZ9LwQ'
    await message.answer_video(video=video_id, caption="<b>print(), Arifmetik amallar va Sinteks</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#03 O\'zgaruvchilar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGA2SyOtzGwuehkGRjrBk6W9k_39_tAAIRCQACI9vRSREcj7LI-tYYLwQ'
    await message.answer_video(video=video_id, caption="<b>#03 O'zgaruvchilar (Variables)</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#04 String", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGBWSyOvlvhkSx9drQOS2v2O2_PhzxAAISCQACI9vRSUt5q3MH-_8WLwQ'
    await message.answer_video(video=video_id, caption="<b>#04 Matn bilan ishlash (Strings)</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#05 Sonlar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGB2SyOw_3SAOGf4i0SipcpGwIzAIrAAITCQACI9vRSWyJfmN9NqUILwQ'
    await message.answer_video(video=video_id, caption="<b>#05 Sonlar bilan ishlash</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#06 List(Ro\'yhat)", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGCWSyOyrNOld6a_NO4i_cu9X3XE7RAAIUCQACI9vRSct1XXth2VM_LwQ'
    await message.answer_video(video=video_id, caption="<b>#06 Lists (Ro'yxatlar)</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#07 Ro\'yhat bilan ishlash", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGC2SyOznaS0nJMZZCGhyQc85R4tt2AAIWCQACI9vRSVBVHKdaKSoZLwQ'
    await message.answer_video(video=video_id, caption="<b>#07 Ro'yxat bilan ishlash. O'zgarmas ro'yxatlar (Tuples)</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#08 For operatori", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGDWSyO0_cLse7F_iZwSCUamqwu-vfAAIXCQACI9vRSSyj7YHbA5F3LwQ'
    await message.answer_video(video=video_id, caption="<b>#08 for tsikli bilan tanishamiz</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#09 If-Else", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGD2SyO8uh2vSjg-fKl8d3EsU97hIwAAJaCgACVwjZScViq36LAeDnLwQ'
    await message.answer_video(video=video_id, caption="<b>#09 if-else shartlari va tarmoqlanish</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#10 Elif", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGEWSyO91BhSl0kTZFWyec_EUm6vQEAALECgACHlEAAUpQxR1MBJxHgy8E'
    await message.answer_video(video=video_id, caption="<b>#10 if-elif-else</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#11 Xatolar bilan ishlash", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGE2SyPBnB-8qRy2BmVzTUwZdyO0SoAAIpCgACsoYISk2AONEM5Yb-LwQ'
    await message.answer_video(video=video_id, caption="<b>#11 Eng ko'p uchraydigan xatolar</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#12 Github portfolio", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGFWSyPC1gG2YJD_DmdfD2ha9qwdPHAAL4CgACbks5Su1U_gABRhpQJy8E'
    await message.answer_video(video=video_id, caption="<b>#12 GitHub bilan tanishuv</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#13 Dictionary(Lug\'at)", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGF2SyPEEnUdKgT8wNe4tPmnXrsBNdAAIUCgACv6dISoQalsYUbmyqLwQ'
    await message.answer_video(video=video_id, caption="<b>#13 Lug'at (Dictionary)</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#14 Lug\'at bilan ishlash", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGGWSyPFOpye-JXF4d2fQBWB0h2HRfAAJkCQACcmtRSgxSs5j6wWoqLwQ'
    await message.answer_video(video=video_id, caption="<b>#14 Lug'at bilan ishlaymiz</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#15 Nesting", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGG2SyPGl0K6Sbx3CMpAPlGs7MX4diAAIWCwACpvloStzS_Ja7qzMiLwQ'
    await message.answer_video(video=video_id, caption="<b>#15 Nesting</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#16 While tsikli", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGHWSyPHH5M7otVw9fY96c29uCZr-SAAIkCgACE16hStQYK0GgUsROLwQ'
    await message.answer_video(video=video_id, caption="<b>#16 While tsikli</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#17 While,List,Dictionary", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGH2SyPHg-84EAAbS_EBmWi0BMw0-sHQACUAcAAmvxuEqD-f0EOKTw9i8E'
    await message.answer_video(video=video_id, caption="<b>#17 While, Ro'yxatlar va Lug'atlar</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#18 Funksiyalar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGIWSyPH6Q_HLYhc_Rzf-RtTYtmylcAAJICgACMZvYSs2xssmjj1cQLwQ'
    await message.answer_video(video=video_id, caption="<b>#18 Funksiya</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#19 Qiymat beruvchi funksiya", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGI2SyPIQN6e89MljaV49tdDMgGOVvAAJ-CgACGSPpSl1RiZ0rBF49LwQ'
    await message.answer_video(video=video_id, caption="<b>#19 Funksiyadan qiymat qaytarish</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#20 Funksiya va Ro\'yhat", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGJWSyPIqUe5JcmNDAbsnA0Ygr_PF7AALlDAACozcRSzv_6PS_CpItLwQ'
    await message.answer_video(video=video_id, caption="<b>#20 Funksiyaga ro'yxat uzatish</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#21 Moslashuvchan Funksiya", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGJ2SyPJKtWhV7kA3BdrY9UbHvwX_vAAIlCQAC7qQxS--bKF0l9gcELwQ'
    await message.answer_video(video=video_id, caption="<b>#21 Moslashuvchan funksiyalar</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#22 Modullar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGKWSyPJuuJb6sNJV2P_7xY3qzMT7YAAKSCQAClapBS_YeqPRaL_5fLwQ'
    await message.answer_video(video=video_id, caption="<b>#22 Modullar</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#23 Funksiya.So\'nggi so\'z", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGK2SyPKWvUtrzLXsF3I1txSChQWF6AALACAAC5-eIS9llxU0eb-YsLwQ'
    await message.answer_video(video=video_id, caption="<b>#23 Funksiya. So'ngso'z</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#24 SON TOPISH O\'YINI 1-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGLWSyPK5dEOoqDJ31r6O2IS_OCrisAAJNCwACDIqxS8qSTVLPecPSLwQ'
    await message.answer_video(video=video_id, caption="<b>#24 Son topish o'yini. 1-qism</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#25 SON TOPISH O\'YINI 2-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGL2SyPLV2mjyuP-dq4WYWIth51J9cAAJ7DAACDIqxS_uafdoNvXzhLwQ'
    await message.answer_video(video=video_id, caption="<b>#25 Son topish o'yini. 2-qism</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#26 SON TOPISH O\'YINI 3-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAISjmTYog8EVNQcAjkH4FfMl00d4Y8tAAIiCgAChFTRSwV4oL_-8Es_MAQ'
    await message.answer_video(video=video_id, caption="<b>#26 So'z topish o'yini. 3-qism.Kod</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#27 SO\'Z TOPISH O\'YINI 1-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGMWSyPNJZri1i2MIY-uaQA63IVL8dAAJTCQAClpzQSxoPNGh80B2ULwQ'
    await message.answer_video(video=video_id, caption="<b>#27 So'z topish o'yini. 1-qism. Kod</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#28 SO\'Z TOPISH O\'YINI 2-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGM2SyPOCJ8X_bCpJsen9ge6H1788KAAK-CwACwt7ZS7wZSqkdD4TJLwQ'
    await message.answer_video(video=video_id, caption="<b>#28 So'z topish o'yini. 2-qism. Kod</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#29 Krill-Lotin bot 1-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGNWSyPOhMzv2LAc0eZetAmWI2qnhVAAJcCgACc7oJSFO78zvf_I5QLwQ'
    await message.answer_video(video=video_id, caption="<b>#29 Kirill-Lotin Transliterator Bot. 1-qism</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#30 Krill-Lotin 2-qism", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGN2SyPPHLBt_c0bGopQLYUzJrXPJ6AAJeCgACc7oJSAet_402C-BcLwQ'
    await message.answer_video(video=video_id, caption="<b>#30 Kirill-Lotin Transliterator Bot. 2-qism</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

#=============================OOOOOOOOOOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP===================================

@dp.message_handler(text="#00 OOP nima?", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGgGSyeMLTCCCUnBXeXEpg0RkYzfxiAAIGDQACGAYgSJSzUF0wMgbuLwQ'
    await message.answer_video(video=video_id, caption="<b>Object Oriented Dasturlash nima?</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#01 Class va Obyektlar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGgmSyeNKpPEViZhb_5fhXmqqzxtXUAAJhDAACu8RYSJqIRMJA-uCELwQ'
    await message.answer_video(video=video_id, caption="<b>Object Oriented Dasturash. Klass va Obyekt</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#02 Obyektlar bilan ishlash", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGhGSyeN4UNPv6ZCNRSIUW4LgDkTVgAALzCgACWop5SD3SpAimGXyVLwQ'
    await message.answer_video(video=video_id, caption="<b>Object Oriented Dasturash. Obyektlar bilan ishlash</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#03 Vorislik va Polimorfizm", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGhmSyeOWyrSpKGg3dQSgrjxui3QYMAAIPDAACs6uhSIy6d_fu6kNKLwQ'
    await message.answer_video(video=video_id, caption="<b>Object Oriented Dasturash. Vorislik va Polimorfizm</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#04 Inkapsulatsiya, Classning xususiyatlari va metodlari", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGiGSyeO1VTKnNYiCueyi39cQVixqGAAJtDAACJSLRSGySiMy61Bq9LwQ'
    await message.answer_video(video=video_id, caption="<b>Object Oriented Dasturash. Inkapsulyatsiya. Klassga xos xususiyat va metodlar</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#05 Dunder metodlar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGimSyePT7GraplBGsDUgxUjVep7sWAAJWCQACj6XpSCTLkTvP-efSLwQ'
    video_id2 = 'BAACAgIAAxkBAAITjmTYr6nyJFXXVDsEFVm0-0ra9TXnAAKDDAACugfgSL8L_A9w7y72MAQ'
    await message.answer_video(video=video_id, caption="<b>Object Oriented Dasturash. Dunder Metodlar. 1-qism</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")
    await message.answer_video(video=video_id2, caption="<b>Object Oriented Dasturash. Dunder Metodlar. 2-qism</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#06 Fayllar bilan ishlash", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGjGSyePwSsP4lBoW31ZwOur-vF-AgAAKdDAACqYIoSVpuh7JjtQizLwQ'
    await message.answer_video(video=video_id, caption="<b>Fayllar bilan ishlash. Pickle</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#07 Json Format", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGjmSyeQf6Pl1NNzFUMH70aJM3wJWHAAKHDAACXzVQSXwlYyZf3khaLwQ'
    await message.answer_video(video=video_id, caption="<b>JSON</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#08 Xatolar bilan ishlash", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGkGSyeRFSpQABkN3HDv8wG1ruO1LlmQAC2QoAAuJreUlrvJwqi56Sti8E'
    await message.answer_video(video=video_id, caption="<b>Xatolar bilan Ishlash. try-except</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#09 Funksiyani tekshirish", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGkmSyeTIxw97vcc7RDMjvltEkHj8xAAIUCgAC_LepSWIC4Q-3ceKhLwQ'
    await message.answer_video(video=video_id, caption="<b>Funksiyalarni tekshirish. unittest moduli</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#10 Klassni tekshirish", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGlGSyeT75OD3nnwtcxRwFBCxAFLvVAAKECgACl0nYSRXvQ28PwUQyLwQ'
    await message.answer_video(video=video_id, caption="<b>Klasslarni tekshirish</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#11 Python Standart kutubxonasi", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGlmSyeV1tqjNNuUJyq2vTDnHBQel3AALbCwACrXY4Sh7NNK4wmLpNLwQ'
    await message.answer_video(video=video_id, caption="<b>Python Standart Kutubxonasi</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#12 Pip va tashqi kutubxonalar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGmGSyeXFpOtR9OWn6F8JX8fJSQZCHAAJPCgACFpNYSszd1y6JR80dLwQ'
    await message.answer_video(video=video_id, caption="<b>Python Tashqi Kutubxonasi PyPi.org</b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="#13 So\'ngso\'z va keyingi qadamlar", state=BackEnd.python)
async def sendpython(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIGmmSyeXgjc9tkcuae5ud_B2Gos4OyAAIEDgACxChwSk2Q8WHEV3KBLwQ'
    await message.answer_video(video=video_id, caption="<b>Soʻngsoʻz </b>\n\n<b>©️Ustoz</b>: <i>Anvar Narzullayev</i>\n\nTarmoqdagi manzillar🌐:\n<a href='https://t.me/sariqdev'>Telegram</a> <b>|</b> <a href='https://www.youtube.com/sariqdev'>You Tube</a><b>|</b> <a href='https://python.sariq.dev/'>WebSayt</a>\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")






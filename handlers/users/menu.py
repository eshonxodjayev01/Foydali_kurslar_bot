from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_keyboards import menu
from keyboards.default.backend_keyboards import backmenu, basicmenuBack, oopmenuback, pythonmenu
from keyboards.default.flutter_keyboards import fluttermenu
from keyboards.default.frontend_keyboards import basicFront,menuHtml,menucss,menucss2,menujs
from keyboards.default.kotlin_keyboards import kotlinmenu,basickotlinmenu,oopkotlinmenu,collectionskotlinmenu,advancedkotlinmenu
from keyboards.default.telegrambot_keyboards import botmenu
from loader import dp
from states import All_states
from states.All_states import Send,BackEnd
#==========================================FrontEnd================================================
@dp.message_handler(text='FrontEnd🌐')
async def send_front(message:types.Message):
    await message.answer('salom siz frontendni tanladingiz',reply_markup=basicFront)
    await Send.frontend.set()

@dp.message_handler(text='HTML🌐',state=Send.frontend)
async def States(message: Message):
    await message.answer('Bilib Oling!',reply_markup=menuHtml)
    video = 'BAACAgIAAxkBAAINi2S0X4gISQ3_PCJ1zPR1YP73brwpAAKvCQACOtDxSg6ELXDxuH9VLwQ'
    await message.answer('''<b>HTML Nima? va Kurs haqida</b>\n\n<b>HTML</b> – bu (ing. HyperText Markup Language, uzb. Giper matnli belgilash tili) bo’lib, umumjahon internet tarmog’idagi hujjatlar uchun standartlashtirilgan belgilash tili hisoblanadi.\n\nBarcha <b>veb-sahifalarda</b> HTML-belgilar mavjud bo’lib ular brauzerlar tomonidan izohlanadi. Natijada formatlangan matn kompyuter yoki mobil qurilmaning ekranida aks etadi.\n\n<b>WEB</b>da HTML sahifalar odatda HTTP yoki HTTPS orqali serverdan oddiy matn shaklida yoki shifrlangan holda brauzerlarga uzatiladi.\n\n<b>HTML</b> gipermatnli belgilash tili ingliz olimi <b>Tim Berners-Li</b> tomonidan 1986–1991 yillarda Shveytsariyaning Jenevadagi CERN labaratoriyasida ishlab chiqilgan.''')
    await message.answer_video(video=video,caption='<b>HTML va Kurs haqida</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️')

@dp.message_handler(text='CSS📙',state=Send.frontend)
async def States(message: Message):
    await message.answer('Mavzuni tanlang',reply_markup=menucss)

@dp.message_handler(text='Java Script📚',state=Send.frontend)
async def States(message: Message):
    await message.answer('Mavzuni tanlang',reply_markup=menujs)

@dp.message_handler(text='Back🔙',state=Send.frontend)
async def sendback(message:Message):
    await message.answer('Kurslarni tanlang',reply_markup=basicFront)


@dp.message_handler(text='Next🔜',state=Send.frontend)
async def sendback(message: types.Message,state: FSMContext):
    await message.answer('Keyingi ro\'yhat:',reply_markup=menucss2)

@dp.message_handler(text='Menu🔝',state=Send.frontend)
async def sendback(message: types.Message,state: FSMContext):
    await message.answer('Kurslarni tanlang',reply_markup=basicFront)

@dp.message_handler(text='Menu⬇️',state=Send.frontend)
async def sendback(message: types.Message,state: FSMContext):
    await message.answer('Kurslarni tanlang',reply_markup=menu)
    await state.finish()

#==========================================FrontEnd================================================

@dp.message_handler(text='BackEnd🖥')
async def sendpython(message: Message):
    await message.answer('Tanlang:',reply_markup=backmenu)
    await BackEnd.python.set()

@dp.message_handler(text='Python🐍',state=BackEnd.python)
async def sendpython(message: types.Message,state: FSMContext):
    await message.answer('Bo\'limni tanlang:',reply_markup=pythonmenu)

@dp.message_handler(text='OOP dastulash',state=BackEnd.python)
async def sendpython(message: types.Message,state: FSMContext):
    await message.answer('Bo\'limni tanlang:',reply_markup=oopmenuback)

@dp.message_handler(text='Dasturlash Asoslari',state=BackEnd.python)
async def sendpython(message: types.Message,state: FSMContext):
    await message.answer("Siz  Python🐍 dasturlash tilida avval barcha dasturlashda bo'lganidek avval <b>Dasturlash asoslari</b>ni o'rganasiz keyin esa <b>OOP</b>(Object Oriented Programming)ni o'ranasiz"
                         "\n\nPython haqida:\n\n<b>Python</b> — o'rganish uchun oson, foydalanish uchun qulay, ko'p qirrali dasturlash tili bo\'lib, dasturlashga yangi kirganlar uchun ham, soha mutaxassislari uchun ham zo'r tanlov\n\n"
                         "<b>Python o\'rganish uchun 5 sabab</b>:\n\n"
                         "🔘1.Python dasturlash tiliga bo\'lgan talab yildan yilga oshib kelmoqda. CodingDojo portalining tadqiqotlariga ko\'ra, 2020 yilda aynan Python tilida dasturlovchi mutaxassislarga eng ko\'p talab bo\'lgan\n"
                         "🔘2.Python Artificial Intelligence (Sun\'iy intellekt) va Data Science (Ulkan ma\'lumotlar bilan ishlash) sohalarining tili hisoblanadi. Bugungi kunda keng ommalashib borayotgan sun\'iy intellekt asosida ishlovchi dasturlarning aksari Pythonda yozilgan. <b>Bu sohalardagi mutaxassislar bugungi kunda eng noyob va qimmatbaho kadrlar hisoblanadi.</b>\n"
                         "🔘3.Keng qamrovli va universal til. Python dasturlari deyarli barcha operativ tizimlarda va platformalarda ishlaydi.\n"
                         "🔘4.O\'rganish uchun ham, tushunish uchun ham juda qulay va sodda kod.\n"
                         "🔘5.Moslashuvchanlik —Python dasturlash tili ma\'lum bir masalalarni yechish bilan chegaralanmagan. Bu til dasturchilarga yangi va yangi yo\'nalishlarga ki\'rish imkonini beradi. Python quyidagi sohalarda qo\'llaniladi: Web va Internet dasturlash, kompyuter o\'yinlarini yaratish, ma\'lumotlar bazasi bilan ishlash (DB), computer vision, foydalanuvchilar uchun grafik interfeys (GUI), juda tez rivojlanayotgan buyumlar interneti (IoT) texnologiyasi va hokazo ",reply_markup=basicmenuBack)
    await BackEnd.python.set()

@dp.message_handler(text='Back🔙',state=BackEnd.python)
async def sendback(message:Message):
    await message.answer('Kurslarni tanlang',reply_markup=pythonmenu)

@dp.message_handler(text='Menu🔝',state=BackEnd.python)
async def sendback(message: types.Message,state: FSMContext):
    await message.answer('Kurslarni tanlang',reply_markup=backmenu)


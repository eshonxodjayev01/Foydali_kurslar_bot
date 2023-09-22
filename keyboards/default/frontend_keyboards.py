from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

basicFront = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='HTML🌐'),
            KeyboardButton(text='CSS📙'),
        ],
        [
            KeyboardButton(text='Java Script📚')
        ],
        [
            KeyboardButton(text='Menu⬇️'),
        ],
    ],
    resize_keyboard=True
)



menuHtml = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='01 Web haqida'),
            KeyboardButton(text='02 Kirish'),
        ],
        [
            KeyboardButton(text='03 Dasturlash muhiti'),
            KeyboardButton(text='04 <<!DOCTYPE>>'),
        ],
        [
            KeyboardButton(text='05 Elementlar va attributelar'),
            KeyboardButton(text='06 Headings'),
        ],
        [
            KeyboardButton(text='07 Paragraphs'),
            KeyboardButton(text='08 Styles'),
        ],
        [
            KeyboardButton(text='09 Formatting'),
            KeyboardButton(text='10 Comments'),
        ],
        [
            KeyboardButton(text='11 CSS 1-qism'),
            KeyboardButton(text='12 CSS 2-qism'),
        ],
        [
            KeyboardButton(text='13 Links'),
            KeyboardButton(text='14 Images'),
        ],
        [
            KeyboardButton(text='15 Lables'),
            KeyboardButton(text='16 Lists'),
        ],
        [
            KeyboardButton(text='17 ID'),
            KeyboardButton(text='18 Class'),
        ],
        [
            KeyboardButton(text='19 Block va Inline'),
            KeyboardButton(text="20 'div' va 'span'"),
        ],
        [
            KeyboardButton(text='21 Forms 1-qism'),
            KeyboardButton(text='22 Forms 2-qism'),
        ],
        [
            KeyboardButton(text='23 Forms 3-qism'),
            KeyboardButton(text='24 Layout va Semantics'),
        ],
        [
            KeyboardButton(text='25 Head'),
            KeyboardButton(text='26 Audio,Video va YouTube'),
        ],
        [
            KeyboardButton(text='27 Best Practises'),
            KeyboardButton(text='28 Project (Loyiha)'),
        ],
        [
            KeyboardButton(text='Back🔙')
        ],
    ],
    resize_keyboard=True
)


menucss = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='01 Kirish'),
            KeyboardButton(text='02 CSS haqida'),
        ],
        [
            KeyboardButton(text='03 Loyiha strukturasi'),
            KeyboardButton(text='04 Selectors'),
        ],
        [
            KeyboardButton(text='05 Comments'),
            KeyboardButton(text='06 Specificity'),
        ],
        [
            KeyboardButton(text='07 Inheritance'),
            KeyboardButton(text='08 Combinators'),
        ],
        [
            KeyboardButton(text='09 Classlar'),
            KeyboardButton(text='10 Class yoki ID'),
        ],
        [
            KeyboardButton(text='11 Loyihani yangilash'),
            KeyboardButton(text='12 Box model'),
        ],
        [
            KeyboardButton(text='13 Margin collapsing'),
            KeyboardButton(text='14 Height,Width..'),
        ],
        [
            KeyboardButton(text='15 Display xossa'),
            KeyboardButton(text='16 Text align..'),
        ],
        [
            KeyboardButton(text='17 Text Decoration'),
            KeyboardButton(text='18 Loyihani yangilash'),
        ],
        [
            KeyboardButton(text='19 Loyihani yangilash 2-qism'),
            KeyboardButton(text='20 Loyihani yangilash 3-qism'),
        ],
        [
            KeyboardButton(text='21 Joylashish/Static'),
            KeyboardButton(text='22 Relative/Fixed'),
        ],
        [
            KeyboardButton(text='23 Absolute/Sticky'),
            KeyboardButton(text='24 Z-index/Overflow'),
        ],
        [
            KeyboardButton(text='25 Loyihani yangilash'),
            KeyboardButton(text='26 Background'),
        ],
        [
            KeyboardButton(text='27 Styling Images'),
            KeyboardButton(text='28 Gradient/Filters'),
        ],
        [
            KeyboardButton(text='29 Loyihani yangilash'),
            KeyboardButton(text='30 Formalarga style berish 1-qism'),
        ],
        [
            KeyboardButton(text='Back🔙'),
            KeyboardButton(text='Next🔜'),
        ],
    ],
resize_keyboard=True
)


menucss2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='31 Formalarga style berish 2-qism'),
            KeyboardButton(text='32 Loyihani yangilash'),
        ],
        [
            KeyboardButton(text='33 Units'),
            KeyboardButton(text='34 Foiz(%)'),
        ],
        [
            KeyboardButton(text="35 'em' o'lchov birligi"),
            KeyboardButton(text="36 'rem' o'lchov birligi"),
        ],
        [
            KeyboardButton(text='37 Viewport o\'lchov birligi'),
            KeyboardButton(text='38 Loyihani yangilash'),
        ],
        [
            KeyboardButton(text='39 Responsive Web Design'),
            KeyboardButton(text='40 Media queries'),
        ],
        [
            KeyboardButton(text='41 Breakpoints'),
            KeyboardButton(text='42 Loyihani yangilash 1-qism'),
        ],
        [
            KeyboardButton(text='43 Loyihani yangilash 2-qism'),
            KeyboardButton(text='44 Fonts'),
        ],
        [
            KeyboardButton(text='45 Yangi font qo\'shish'),
            KeyboardButton(text='46 Local font qo\'shish'),
        ],
        [
            KeyboardButton(text='47 Font xossalari'),
            KeyboardButton(text='48 Loyihani yangilash'),
        ],
        [
            KeyboardButton(text='49 2D transforms'),
            KeyboardButton(text='50 3D transforms'),
        ],
        [
            KeyboardButton(text='51 Transitions'),
            KeyboardButton(text='52 Animations 1-qism'),
        ],
        [
            KeyboardButton(text='53 Animations 2-qism'),
            KeyboardButton(text='54 Loyihani yangilash'),
        ],
        [
            KeyboardButton(text='55 Flexbox'),
            KeyboardButton(text='56 Flex-direction..'),
        ],
        [
            KeyboardButton(text='57 Align-items'),
            KeyboardButton(text='58 Order,flex-grow'),
        ],
        [
            KeyboardButton(text='59 Flex-basis'),
            KeyboardButton(text='60 Loyihani yangilash'),
        ],
        [
            KeyboardButton(text='61 CSS Grid'),
            KeyboardButton(text='62 Best Practices'),
        ],
        [
            KeyboardButton(text='63 Kurs yakuni.Loyihani yakunlash'),
        ],
        [
            KeyboardButton(text='Menu🔝'),
        ],
    ],
    resize_keyboard=True
)


menujs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='01 Kirish JS'),
            KeyboardButton(text='02 Javascript o\'zi'),
        ],
        [
            KeyboardButton(text='03 Hello World'),
            KeyboardButton(text='04 O\'zgaruvchilar'),
        ],
        [
            KeyboardButton(text='05 Ma\'lumot turlari'),
            KeyboardButton(text='06 Let,const va var'),
        ],
        [
            KeyboardButton(text='07 Asosiy operatorlar'),
            KeyboardButton(text='08 String'),
        ],
        [
            KeyboardButton(text='09 Mantiqiy operator'),
            KeyboardButton(text='10 Typeni o\'zgartirish'),
        ],
        [
            KeyboardButton(text='11 Funksiya'),
            KeyboardButton(text='12 Expression/Arrow'),
        ],
        [
            KeyboardButton(text='13 Funksiyani ishlatish'),
            KeyboardButton(text='14 Array'),
        ],
        [
            KeyboardButton(text='15 Array methods'),
            KeyboardButton(text='16 Objects'),
        ],
        [
            KeyboardButton(text='17 Objects method'),
            KeyboardButton(text='18 If-Else'),
        ],
        [
            KeyboardButton(text='19 Switch'),
            KeyboardButton(text='20 For'),
        ],
        [
            KeyboardButton(text='21 While'),
            KeyboardButton(text='22 Oqim boshqaruvi'),
        ],
        [
            KeyboardButton(text='23 DOM'),
            KeyboardButton(text='24 Elementni tanlash'),
        ],
        [
            KeyboardButton(text='25 Elementni o\'zgartirish'),
            KeyboardButton(text='26 Elementni qo\'shish'),
        ],
        [
            KeyboardButton(text='27 Events(Hodisalar)'),
            KeyboardButton(text='28 Lots events'),
        ],
        [
            KeyboardButton(text='29 DOM (ma\'lumot)'),
            KeyboardButton(text='30 Kurs yakuni'),
        ],
        [
            KeyboardButton(text='Back🔙'),
        ],
    ],
    resize_keyboard=True
)
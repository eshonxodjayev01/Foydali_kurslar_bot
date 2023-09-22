import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types
from keyboards.default.frontend_keyboards import basicFront,menuHtml,menucss,menucss2,menujs
from loader import dp
from states.All_states import Send

@dp.message_handler(content_types='video')
async def SendFront(message: types.Message):
    videos=message.video
    logging.info(videos)
    id = message.video.file_id
    await message.answer(id)

@dp.message_handler(content_types='photo')
async def sendphoto(message: types.Message):
    photos=message.photo
    logging.info(photos)
    id = message.photo[-1]
    await message.answer(id)

@dp.message_handler(text='01 Web haqida',state=Send.frontend)
async def sendfront(message:Message):
    video_id1 = 'BAACAgIAAxkBAAINYWS0W7k73ojgpBebkO0Ecj9LF9rKAALABwACFaPoSsRhHVhmiOI_LwQ'
    await message.answer_video(video=video_id1,caption="<b>HTMLda dasturlash | 1. WEB haqida</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️'")

@dp.message_handler(text='02 Kirish',state=Send.frontend)
async def sendfront(message:Message):
    video_id2 = 'BAACAgIAAxkBAAIBKmSPH62mAi3ZYL7-ZppmGeHpCbjYAALKDAACUL-BS8RgUHftUeYeLwQ'
    await message.answer_video(video=video_id2,caption='<b>HTMLda dasturlash | 2. Kirish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️')

@dp.message_handler(text="03 Dasturlash muhiti",state=Send.frontend)
async def sendfront(message:Message):
    video_id3 = 'BAACAgIAAxkBAAIBL2SPH95qcLy5tRgQfcdgYNBVl8H3AAIaCwACW1mZSEcoUrE7r86iLwQ'
    await message.answer_video(video=video_id3,caption='<b>HTMLda dasturlash | 3. Development Environment (Dasturlash Muhiti)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube:↘️\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️')

@dp.message_handler(text="04 <<!DOCTYPE>>",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id4='BAACAgIAAxkBAAICJWSjEyj9yPzfgUMIo77X51GnQNZDAAIcCwACW1mZSBHFrcpJYRewLwQ'
    await message.answer_video(video=video_id4,caption="<b>HTMLda dasturlash | 4. Hujjat strukturasi va !DOCTYPE</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="05 Elementlar va attributelar",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id5='BAACAgIAAxkBAAIBd2SQZjzQoApynA32HCF1_4etWp9jAAIdCwACW1mZSIzbu_oCoalKLwQ'
    await message.answer_video(video=video_id5,caption="<b>HTMLda dasturlash | 5. Elementlar va attributelar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="06 Headings",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id6='BAACAgIAAxkBAAICSWSjFFD88EtVhhyIEw1V2D-fmKHcAAIeCwACW1mZSPmhePkoDp3eLwQ'
    await message.answer_video(video=video_id6,caption="<b>HTMLda dasturlash | 6. Headings (Sarlavhalar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="07 Paragraphs",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id7='BAACAgIAAxkBAAICOGSjE6NqvXIQxXoL3LXuRDPAImz4AAJhDAAC2CWgS84U07uKYw--LwQ'
    await message.answer_video(video=video_id7,caption="<b>HTMLda dasturlash | 7. Paragraphs (Xatboshilar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="08 Styles",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id8='BAACAgIAAxkBAAICWGSjFK6Q4oHtiUyb5ygPgYGO3gw9AAIfCwACW1mZSNyjKW1MxjyKLwQ'
    await message.answer_video(video=video_id8,caption="<b>HTMLda dasturlash | 8. Styles (Stillar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="09 Formatting",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id9='BAACAgIAAxkBAAICbWSjHOjILzQE2FLvz7Dgd-_2vifTAAJiDAAC2CWgS5VDpDW5CqfjLwQ'
    await message.answer_video(video=video_id9,caption="<b>HTMLda dasturlash | 9. Formatting (Formatlash)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="10 Comments",state=Send.frontend)
async def sendfront(message: types.Message):
    video_id10='BAACAgIAAxkBAAICcmSjHWpDLnO3S3JLhcxjHCRVQRSHAAIgCwACW1mZSKyg_F0cAsCILwQ'
    await message.answer_video(video=video_id10,caption="<b>HTMLda dasturlash | 10. Comments (Izohlar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="11 CSS 1-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id11 = 'BAACAgIAAxkBAAICmWSjIhVFsfGwBl_aQ_YFYOlkNKW9AAIhCwACW1mZSBxj5fdIJA3VLwQ'
    await message.answer_video(video=video_id11, caption="<b>HTMLda dasturlash | 11. CSS 1-qism</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="12 CSS 2-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id12 = 'BAACAgIAAxkBAAICm2SjIjuyyXWVvvEqu3EaAAG6qlJM5gACIgsAAltZmUixc64TLylvkS8E'
    await message.answer_video(video=video_id12, caption="<b>HTMLda dasturlash | 12. CSS 2-qism</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="13 Links", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id13 = 'BAACAgIAAxkBAAICnWSjIlCA3tRdS3Fcz3GR_-aL2mAZAAIkCwACW1mZSG8r_8pLIo1vLwQ'
    await message.answer_video(video=video_id13, caption="<b>HTMLda dasturlash | 13. Links (Havolalar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="14 Images", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id14 = 'BAACAgIAAxkBAAICn2SjImQe8b-Khuwn25UhbUektTBlAAIlCwACW1mZSDrEcjFCw1cLLwQ'
    await message.answer_video(video=video_id14, caption="<b>HTMLda dasturlash | 14. Images (Rasmlar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="15 Lables", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id15 = 'BAACAgIAAxkBAAICoWSjInfHVFoDluXEQ9Fdu7XZlFYJAAInCwACW1mZSCH_nEE08MFSLwQ'
    await message.answer_video(video=video_id15, caption="<b>HTMLda dasturlash | 15. Tables (Jadvallar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="16 Lists", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id16 = 'BAACAgIAAxkBAAICtGSjIrg3ja2CTUT7XgErzzpjDd15AAIoCwACW1mZSHrOATmALqrOLwQ'
    await message.answer_video(video=video_id16, caption="<b>HTMLda dasturlash | 16. Lists (Ro'yhatlar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="17 ID", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id17 = 'BAACAgIAAxkBAAICtmSjItHrLYCb9e-EkjvfCHecvBSaAAIqCwACW1mZSMr26gsrqylMLwQ'
    await message.answer_video(video=video_id17, caption="<b>HTMLda dasturlash | 17. ID</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="18 Class", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id18 = 'BAACAgIAAxkBAAICuGSjIuMJ1v4bCJvAVwGHuptF_arQAAIrCwACW1mZSGMD1YJWC6yoLwQ'
    await message.answer_video(video=video_id18, caption="<b>HTMLda dasturlash | 18. Class</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="19 Block va Inline", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id19 = 'BAACAgIAAxkBAAICumSjIvlSJ8mNbdmdThzCP9jTrRSLAAIsCwACW1mZSItH75f1zPXDLwQ'
    await message.answer_video(video=video_id19, caption="<b>HTMLda dasturlash | 19. Block va Inline elementlar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")


@dp.message_handler(text="20 'div' va 'span'", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id20 = 'BAACAgIAAxkBAAICvGSjIw7Fq5UlI78poxq3_4jw2cH6AAItCwACW1mZSMyYbq2SNdFKLwQ'
    await message.answer_video(video=video_id20, caption="<b>HTMLda dasturlash | 20. div va span</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="21 Forms 1-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id21 = 'BAACAgIAAxkBAAICvmSjIzYfjSF1-KPMQ0Ec7t1kBnXYAAIuCwACW1mZSJwd12b9kDF1LwQ'
    await message.answer_video(video=video_id21, caption="<b>HTMLda dasturlash | 21. Forms 1-qism</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="22 Forms 2-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id22 = 'BAACAgIAAxkBAAICwGSjI07oTDSbEs63mwABEIiUcuxZugACLwsAAltZmUjVhEQrJVzd5i8E'
    await message.answer_video(video=video_id22, caption="<b>HTMLda dasturlash | 22. Forms 2-qism</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="23 Forms 3-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id23 = 'BAACAgIAAxkBAAIROmS4ItVLhq6zqU4zNhGUXuUS_UdiAAJaDAACW1mZSLlgNBwnjUahLwQ'
    await message.answer_video(video=video_id23, caption="<b>HTMLda dasturlash | 23. Forms 3-qism</b>\n\nFormalar haqida qo'shimcha (ingliz tilida):\nhttps://www.w3schools.com/HTML_form_input_types.asp\nhttps://www.w3schools.com/HTML/HTML_form_elements.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="24 Layout va Semantics", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id24 = 'BAACAgIAAxkBAAICxGSjI6m1TCBCxmywSflAnyX2MGieAAIxCwACW1mZSI_6T5W48DaSLwQ'
    await message.answer_video(video=video_id24, caption="<b>HTMLda dasturlash | 24. Layout va Semantics</b>\n\nFormalar haqida qo'shimcha (ingliz tilida):\nhttps://www.w3schools.com/HTML5_semantic_elements.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="25 Head", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id25 = 'BAACAgIAAxkBAAICxmSjI7wpljggVSsWRIcaDp9aW6krAAI1CwACW1mZSDBZAAEdu-gFzi8E'
    await message.answer_video(video=video_id25, caption="<b>HTMLda dasturlash | 25. Head</b>\n\nFormalar haqida qo'shimcha (ingliz tilida):\nhttps://www.w3schools.com/HTML/HTML_head.asp\nhttps://www.w3schools.com/HTML/charset.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="26 Audio,Video va YouTube", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id26 = 'BAACAgIAAxkBAAICyGSjI83SCzLmci4x2JwXDYAT-KlNAAJzCQACf_O4S4ApT_IlU2IjLwQ'
    await message.answer_video(video=video_id26, caption="<b>HTMLda dasturlash | 26. Audio, Video va Youtube</b>\n\nFormalar haqida qo'shimcha (ingliz tilida):\nhttps://www.w3schools.com/HTML_charset.asp\nhttps://www.w3schools.com/HTML/HTML5_video.asp\nhttps://www.w3schools.com/HTML_youtube.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="27 Best Practises", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id27 = 'BAACAgIAAxkBAAICymSjI-LLEgABJB7M-xr9dMpX_9EdRwACNwsAAltZmUioAeS3J5IXlS8E'
    await message.answer_video(video=video_id27, caption="<b>HTMLda dasturlash | 27. Best practices</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="28 Project (Loyiha)", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id28 = 'BAACAgIAAxkBAAICzGSjI_B3QhOLa6osOgN3bgu_CBUxAAI4CwACW1mZSP9nBleZG1KNLwQ'
    await message.answer_video(video=video_id28, caption="<b>HTMLda dasturlash | 28. Loyiha (Project)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

#===========================================================================================================================
#===========================================================================================================================

@dp.message_handler(text="01 Kirish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJZWSz4Dk2awwmTGjX_G2bWJ0Gr_XjAAKICQACUl2BSNfTXBos6JkWLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 1. Kirish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="02 CSS haqida", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJaGSz6X9AAAHLFcVkqzc50RFIBgy6PAACcQoAAk8v2EtYpFKs8TJvdi8E'
    await message.answer_video(video=video_id, caption="<b>CSS | 2. CSS haqida. Kurs loyihasi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="03 Loyiha strukturasi", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJeWSz6d8Y7tYM1W297d3EAtp6i7qeAAK5CwAC1bTgSkPPISqwyOsLLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 3. HTML hujjat va CSS. Loyiha strukturasi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="04 Selectors", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJfGSz8WZTUIT_WxNvwbZtNsAj8i7YAAJaDAACapMgSQMxDTrQt0_TLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 4. Selectors (Tanlab oluvchilar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="05 Comments", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJfmSz8W35Ybf0WHrfNAyKY_By4O8dAAJbDAACapMgSfoM1jj-XacWLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 5. Comments (Izohlar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="06 Specificity", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJgGSz8XVymVjdNHx210d9MI_HSCDIAAKGDQAC1_-ZSUsOCrk1Qp81LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 6. Specificity (O'ziga xoslik)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="07 Inheritance", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJgmSz8X7DUdyoew9yqSsLkog85bD8AAK7DwACHwE4SeTOqmC4sHuFLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 7. Inheritance (Meros olish)</b>\n\nMeros bo'lib o'tadigan CSS xossalari ro'yhatiga ilova:https://stackoverflow.com/questions/5612302/which-css-properties-are-inherited\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="08 Combinators", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJhGSz8YTMm3AReTegh5hZ5wmHXYsMAAKHDQAC1_-ZSS_t68F5R5_hLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 8. Combinators (Kombinatorlar)</b>\n\nSources:\nhttps://d2slcw3kip6qmk.cloudfront.net/marketing/blog/2019Q3/family-tree-chart/genealogy-chart-example.png\n\nhttp://web.simmons.edu/~grabiner/comm244/weekfour/document-tree.HTML\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="09 Classlar", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJhmSz8Y5fCk0voZqtw_C5R1jq8eehAAK8DwACHwE4SUJN0C8rBCmfLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 9. Class lar va qo'shma (combined) selektorlar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="10 Class yoki ID", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJiGSz8ZvXcV_Oiw8mxIf9G_VhaAykAAK9DwACHwE4SfOFkbzjdO1mLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 10. Class yoki ID. !important haqida</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="11 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJimSz8aIpWteowbd_CyXzf0Oof6OMAAKJDQAC1_-ZSeEtJw7fuvIaLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 11. CSS asoslari yordamida loyihani yaxshilash</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="12 Box model", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJjGSz8anUDMOathlTeomguHKMW4xZAAKKDQAC1_-ZSbZSX3Js7coaLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 12. Box model (Quti modeli). Margin, Padding, Border</b>\n\nBox model haqida: https://hackernoon.com/the-box-model-44fc2c04a935\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="13 Margin collapsing", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJjmSz8bA1SXRjHD4OqTDcI7ce6-zuAALJDwACHwE4SZfBl8TfOTR-LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 13. Margin collapsing. Shorthands (Qisqartmalar)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="14 Height,Width..", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJkGSz8bwvFYYwU779euT5OSwB7V3QAAIZCgACi1WYSXclPfIrJceLLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 14. Height (balandlik), Width (kenglik). Max / Min - height / width</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="15 Display xossa", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJkmSz8cO_HGD7zXFjvHCeaZv17nSoAALLDwACHwE4SbEdRbnkxH1xLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 15. Display xossasi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="16 Text align..", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJlGSz8ckrEatZkSuK_ZaSAvoW-vhHAALMDwACHwE4SaJqG4WKC8BsLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 16. Text align, Vertical align va Float</b>\n\nFloat haqida: https://uxdesign.cc/float-58b9685f3928?gi=f11b6d656504\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="17 Text Decoration", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJlmSz8c4MDCSmGHwlbBPn1LvTpsQGAALNDwACHwE4SYfTLWLhYA1zLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 17. Text decoration. Pseudo classes va qoidalarni guruhlash</b>\n\nPseudo klasslarga qo'shimcha: https://www.w3schools.com/css/css_pseudo_classes.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="18 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJnGSz8gwwmYBBucCEn6211oeVRMRaAALODwACHwE4SeOaKq0xoDKNLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 18. Asosiy xossalar yordamida loyihani yaxshilash (1-qism)</b>\n\nRangni tanlab olish uchun maxsus Chrome plugin: https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg?hl=en\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="19 Loyihani yangilash 2-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJnmSz8hOvTYSe4YaCPlXccTIyxfmvAAIfCgACi1WYSbVcxtxcoirvLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 19. Asosiy xossalar yordamida loyihani yaxshilash (2-qism)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="20 Loyihani yangilash 3-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJoGSz8hpOEusf1Q3lt9x9JSpj6jmrAALQDwACHwE4SR-Va1ycVDrELwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 20. Asosiy xossalar yordamida loyihani yaxshilash (3-qism)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="21 Joylashish/Static", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJomSz8iGPSqT8i4WNyw1U8sMQXkSfAAK8CwAC1bTgSvXZdOafVIvLLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 21. Joylashish va static qiymati</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="22 Relative/Fixed", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJpGSz8if0BBkUlw5nSno4HG2rSozaAAKMDQAC1_-ZSRtj9KrY6rI_LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 22. Relative va Fixed</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="23 Absolute/Sticky", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJpmSz8i3Y3_j2pwQc4Ozxq5jU6xTMAAK9CwAC1bTgSnvEYZ-tFdHzLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 23. Absolute va Sticky</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="24 Z-index/Overflow", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJqGSz8jLXnThFAAHLrqxjS2oyRWF3QQACtAsAAtW04EoYfld6gJancy8E'
    await message.answer_video(video=video_id, caption="<b>CSS | 24. Z-index va Overflow</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="25 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJqmSz8j9865qZ2CAPxMwCPHa41PlyAAIlCgACi1WYSaKLfN4_UbfGLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 25. Positioning yordamida loyihani yaxshilash</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="26 Background", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJrGSz8kWjAsGlvt6Ccc33g4-YhoirAAKNDQAC1_-ZSRf0LBPD0sC3LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 26. Background</b>\n\nFoydali linklar: https://www.w3schools.com/css/css_background.asp\nhttps://www.w3schools.com/cssref/pr_background-image.php\nhttps://www.w3schools.com/cssref/css3_pr_background-size.php\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="27 Styling Images", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJrmSz8kxo9bAAATZcd-OiN9aqJeqdLQACjg0AAtf_mUncYcWSp7_RAAEvBA'
    await message.answer_video(video=video_id, caption="<b>CSS | 27. Styling images</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="28 Gradient/Filters", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJsGSz8lMHWZ5RePXCyZnYidP8JGfvAALvDAACmiIJS50BlklPbhYiLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 28. Gradient va Filterlar</b>\n\nGradientlar haqida ko'proq bilish uchun: https://www.w3schools.com/css/css3_gradients.asp\nhttps://www.w3schools.com/cssref/func_linear-gradient.php\nFilterlar haqida:https://www.w3schools.com/cssref/css3_pr_filter.php\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="29 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJsmSz8lmwPNOi6KX_R2D5Ub1sMksOAAIpCgACi1WYSW1R9bcy_871LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 29. Rasmlar (images) yordamida loyihani yaxshilash</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="30 Formalarga style berish 1-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJtGSz8mCtJ5vZVV3FnnVI78OKxpNmAAKeCgAC67_pSvA_MoVNxv-ELwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 30. Formalarga style berish (1-qism)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="31 Formalarga style berish 2-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJtmSz8mcrhI1valqpVCBUdXq0-fy_AAIrCgACi1WYST5D4U_MyPtaLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 31. Formalarga style berish (2-qism)</b>\n\nCheckbox va radio buttonga style berish:https://www.w3schools.com/howto/howto_css_custom_checkbox.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="32 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJuGSz8mx9aa1-CQ9vmcEqCkVqiD0wAAItCgACi1WYSccXGXnQV82WLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 32. Formalar yordamida loyihani yaxshilash</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="33 Units", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJumSz8nKmStra2f8G_hdpe2HBjONVAAK-CwAC1bTgSlviWuVl2XaiLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 33. O'lchov birliklari (Units)</b>\n\nWhatFont plugini:https://chrome.google.com/webstore/detail/whatfont/jabopobgcpjmedljpbcaablpmlmfcogm\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="34 Foiz(%)", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJvGSz8njCkUaurihxjDyfk1iYAQABiwAC8QwAApoiCUu3r8_xaI5sqS8E'
    await message.answer_video(video=video_id, caption="<b>CSS | 34. Foiz (%) o'lchov birligi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="35 'em' o'lchov birligi", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJvmSz8n2EOxmisxHnrQM0aKOslFbwAAImDAACzEPxSrENAfQWphM9LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 35. em o'lchov birligi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="36 'rem' o'lchov birligi", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJwGSz8oJbWPq6lAzn1O1BtNtujdrcAALyDAACmiIJS6XdSUMm_f-oLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 36. rem o'lchov birligi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="37 Viewport o\'lchov birligi", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJwmSz8opXW5m28lxDERq_ysi1SB34AALzDAACmiIJS7SWQUsCq3XOLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 37. Viewport o'lchov birligi</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="38 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJxGSz8pDCTMNse2pv_DrLVgABnJwk7gACwAsAAtW04ErhA_1E3H55Di8E'
    await message.answer_video(video=video_id, caption="<b>CSS | 38. Units yordamida loyihani yaxshilab olish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="39 Responsive Web Design", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJxmSz8pY3RWQ1-XckeMatrc-sYRkPAAInDAACzEPxStMkTaAsiqGLLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 39. Responsive Web Design (RWD)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="40 Media queries", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJyGSz8qNm4yc72sAQD-nZwbMBHNEIAAIoDAACzEPxSm4Pr270KVTILwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 40. Media queries</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="41 Breakpoints", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJymSz8qxqBFrnXOZiznX6923PJ-piAAKRDQAC1_-ZSfIeQrwAAWUUqi8E'
    await message.answer_video(video=video_id, caption="<b>CSS | 41. Breakpoints</b>\n\nBreakpoints haqida ko'proq ma'lumot: https://keysoftwareservices.co.in/responsive-design-breakpoints/\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="42 Loyihani yangilash 1-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJzGSz8rShQwJLSrUMfuTkAAGoTsmhzQACOQoAAotVmEnygDLehgvAZi8E'
    await message.answer_video(video=video_id, caption="<b>CSS | 42. RWD yordamida loyihani yaxshilash (1-qism)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="43 Loyihani yangilash 2-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJzmSz8sCTEPMdhKfD7ylpzL-xbs2UAAI6CgACi1WYSVCoLwdKn0oeLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 43. RWD yordamida loyihani yaxshilash (2-qism)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="44 Fonts", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ0GSz8syybPNjE9IcfzzJvXuJHcM3AAKVDQAC1_-ZSRPsCO8W7pPfLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 44. Fonts</b>\n\nSans-Serif haqida ma'lumot:https://zerogravitymarketing.com/sans-serif-readability/\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="45 Yangi font qo\'shish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ0mSz8tZkmnKeUj5fj726gUgF_S9lAAJfDQACk2aZSUmt6y1kdySiLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 45. Yangi font qo'shish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="46 Local font qo\'shish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ1GSz8t_KTLnI6JsQ-iD11unRhBdcAAIGDAACYquoSVH7X8s8_rs5LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 46. Local font qo'shish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="47 Font xossalari", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ1mSz8uUix2rAwySG5BrxyXdwZJsDAAIBDQACNd6xSU2LGPr9nXUgLwQ9'
    await message.answer_video(video=video_id, caption="<b>CSS | 47. Font xossalari</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="48 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ2GSz8ut-fxEew9lZsJak5jvI7o3oAALJCgACf0C5Sa3yREz7cEh6LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 48. Fonts yordamida loyihani yaxshilab olish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="49 2D transforms", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ2mSz8vEYBOpI3YyIFtmCY34W_HQTAALkCAACXFfISdXDo3m9iCw8LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 49. 2D transforms</b>\n\n2D Transform qo'shimcha ma'lumot:https://www.w3schools.com/css/css3_2dtransforms.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="50 3D transforms", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ3GSz8vdg9C-xqUq_kiMPmdVG0RDXAALoCQACbaHgSRkRY2x4bZ0ZLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 50. 3D transforms</b>\n\n3D transforms qo'shimcha ma'lumot: https://www.w3schools.com/css/css3_3dtransforms.asp\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="51 Transitions", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ3mSz8v1iQtDjITZfMczK2pWeMuEUAALtCQACbaHgSe6clM_3m1rFLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 51. Transitions</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="52 Animations 1-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ4GSz8wKCUw8Zo9YNtvx3BBfj_ycWAAIwCQACsGgQSkVkzNvLpxeFLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 52. Animations (1-qism)</b>\n\nCSS animation uchun misol: https://codingislove.com/build-a-smokin-hot-coffee-cup-animation-using-css-%E2%98%95/\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="53 Animations 2-qism", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ4mSz8wj2MkXzSaxS125E8QXh5wgcAAKtDAACZbcoSsT07LNlbL0ULwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 53. Animations (2-qism)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="54 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ5GSz8w6KAZfCNf5QifELlxr2_RIGAAIxCQACsGgQSkm0b4NLThGPLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 54. CSS Advanced yordamida loyihani yaxshilash</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="55 Flexbox", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ5mSz8xWFokk3tOjbGp9E0eiOq7TzAAIyCQACsGgQSl-ux0HnriPiLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 55. Flexbox: asoslari va terminlari</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="56 Flex-direction..", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ6GSz8xvtb6NInQ_yQEO6bGD0NUOHAAIzCQACsGgQSluSBFm7jkcBLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 56. Flexbox: flex-direction, flex-wrap, flex-flow va justify-content</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="57 Align-items", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ6mSz8yIVn0HJXW4akZQX50Ac7ktmAAKcCgACnJggSsNh9KfwWpDeLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 57. Flexbox: align-items va align-content</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="58 Order,flex-grow", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ7GSz8yex-J4rTgG5E4acVkAFu_i6AAKuDAACZbcoSsqPg5ELZ6mhLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 58. Flexbox: order, flex-grow va flex-shrink</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="59 Flex-basis", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ7mSz8y4DRjXe3aY9Tpk3BywWZ1EOAAK9CgACZbcwSqs7N_qK38xmLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 59. Flexbox: flex-basis, flex va align-self</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="60 Loyihani yangilash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ8GSz8zWFIElW9BO4INDvVc-SVD7mAAIHDgACSpM5Svk1J5mRIssgLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 60. Flexbox yordamida loyihani yaxshilash</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="61 CSS Grid", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ8mSz8zrPKyhDr4y-YjOAXZomOb2zAALqCgACSIZJSsJv-jNTDrz0LwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 61. CSS Grid</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="62 Best Practices", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ9GSz80Gj8rvSPKyOyd09jMoLbstHAAKjCAACSIZRSk-Itvs1LTcZLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 62. Best practices</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="63 Kurs yakuni.Loyihani yakunlash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIJ9mSz80dwa0JJVmBn5K4yN4zmfiMMAALSDAACCWtgSotfd1Fv7BhCLwQ'
    await message.answer_video(video=video_id, caption="<b>CSS | 63. Loyihani yakunlash. Kurs yakuni</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

#=======================================================================================================================
#=======================================================================================================================

@dp.message_handler(text="01 Kirish JS", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKpWS0MhwXVRgckaBUtOjEV7pfHGGYAAL7EAAC8cJBSvCjJ3RVKwTmLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 1. Kirish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="02 Javascript o\'zi", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKp2S0MjTtWOU82m3cE5sjDhs27-bRAALzDAACrIlISpfaX2TZIGM-LwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 2. Javascript va uning versiyalari</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="03 Hello World", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKqWS0Mm9_e9W8Z0jmbDxCpxo76Ug0AAIKDQACYyBgSqSCgbOlFA6nLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 3. Salom dunyo!</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="04 O\'zgaruvchilar", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKq2S0MpiFEjEpFQfff9vXqI1HjjzWAAIMDwACkjt4Sm6SlORo8iJRLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 4. Qiymatlar va o'zgaruvchilar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="05 Ma\'lumot turlari", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKrWS0MsExYNd0RIT5EWwaRchFJ0UbAAJ-DQACExSISijZb61AyA3HLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 5. Ma'lumot turlari</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="06 Let,const va var", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKr2S0MusznenEuoNOAzv0c5vXhtb3AAIlDgACWeOgShTaKB1AIVTLLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 6. let, const va var</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="07 Asosiy operatorlar", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKsWS0MxRu3jnuEQED_FjKg904gw4NAAKTDAACEezZSgq-baCEXUThLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 7. Asosiy operatorlar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="08 String", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKs2S0MzYbCN46PN3QaxgiRjonUayTAAIGEQACmAXwSunQ5VhgQNTSLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 8. String</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="09 Mantiqiy operator", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKtWS0M1kU-qm0qXg_CuLSJ9pvCvk7AAIGEQAChVBhSxkzVKKKH9UKLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 9. Mantiqiy operatorlar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="10 Typeni o\'zgartirish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKt2S0M37CrAwPYPfFo01eAAE-JXCpGQACAhAAArA_kUiZShuvI7pQ6y8E'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 10. Turni (type) o'zgartirish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="11 Funksiya", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKuWS0M6iBPJuoh0LNWWBep-cERdbmAAJVEwACkOmZSOe7o-8bMPAyLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 11. Funksiya va uni e'lon qilish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="12 Expression/Arrow", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKu2S0M9kztQVwCMtRhjx5d5xv2t_XAAJzFQACjOXgSHbyo85uUaOVLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 12. Function expression va arrow function</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="13 Funksiyani ishlatish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKvWS0NAAB67o-xJMBAUm9rENPbX2haQACbxIAAuNgCUolxL4FH3OktC8E'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 13. Funksiyalar bo'yicha amaliyot</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="14 Array", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKv2S0NCVqgxRLG7ZJB5xFxDouMnsOAALCGAACKFWxS6JlpRPcEH-2LwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 14. Array</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="15 Array methods", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKwWS0NE-JfZm8KkflsBVMFED3KsAiAAKNEQACuRS5S4h4A3XGDroNLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 15. Array methods</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="16 Objects", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKw2S0NI8Sgl9edUPljDyO4fNuSf89AALzFwACOuNYSKVzkIBFXwFnLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 16. Objects</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="17 Objects method", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKxWS0NNBCecTtW5cXZUj0_d1C7Ye_AAJkGwACq0pgSOl9IURqY1lMLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 17. Object methods</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="18 If-Else", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKx2S0NPxqGCzLfLVvvVEcwx0EWmKNAAJ9HQACg2XwSuo8X_zfcqLGLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 18. if/else</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="19 Switch", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKyWS0NRyeZg7pgt95Eqz_Jaev02WLAAJDJQAC2-i5SrBuU0z0kmx-LwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 19. switch</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="20 For", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKy2S0NVtHqXiV2bUxMaR1ckekhkH_AALrIgACUKnJSui9JZcpV2u9LwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 20. for</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="21 While", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKzWS0NbnFIQ-6hvbDf13iZkhdHWJeAAJLIAACM1DRSlbGFDaXcbArLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 21. while</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="22 Oqim boshqaruvi", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIKz2S0NeB0--6K1lLuQ2OSgHNva8BnAAJoIwACmFLhSs92oBywVhS8LwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 22. Oqim boshqaruvi bo’yicha amaliyot</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="23 DOM", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK0WS0Ng6bCIaIlXjMt3KuyhJBcWgfAAJKIwACtdboSucjhvEe2mAMLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 23. DOM</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="24 Elementni tanlash", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK02S0Nkmd8XqbJOzqMGchwSzEQz94AALaJAACkSHwSsU6rGd2OaqdLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 24. Elementlarni tanlab olish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="25 Elementni o\'zgartirish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK1WS0NvCcRWJSRrU0GHtC8bxf9ikhAAIpNAACL3ygSfwZecYYBvstLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 25. Elementlarni o’zgartirish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="26 Elementni qo\'shish", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK12S0Nyfn-a4IZregA1IXFg-2w2SaAAJCKAACkTUBS9hbF4rPB1CwLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 26. Elementlarni qo’shish va o’chirish</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="27 Events(Hodisalar)", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK2WS0N1VOPGEGgE26IQNR5-fGFRdbAAJ7JgAC9ugRSyz08eBt7MqALwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 27. Hodisalar (events)</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="28 Lots events", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK22S0N3lB-4lAhHarc7mb22gIbgv1AAKNIwACP4AZSwXvZ0Z3nm2bLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 28. Ko’p uchraydigan hodisalar</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="29 DOM (ma\'lumot)", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK3WS0N6vKdjm1R7GPHKCs_HkI6kj9AAL5HwAC8skoSxYo1CyIyZN7LwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 29. DOM bo’yicha amaliyot</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

@dp.message_handler(text="30 Kurs yakuni", state=Send.frontend)
async def sendfront(message: types.Message):
    video_id = 'BAACAgIAAxkBAAIK32S0N8-BnZCcx5GUsswo1xrVwnM7AAIwLQACpfooS9vpX6bVnJRNLwQ'
    await message.answer_video(video=video_id, caption="<b>Javascript asoslari | 30. Kurs yakuni</b>\n\n<b>©️Ustoz</b>: <i>Ulugbek Samigjonov</i>\n\nYou Tube↘️:\nhttps://www.youtube.com/@UlugbekSamigjonov\n\n@Foydali_kurslar_bot - Bepul IT kurslar platformasi☑️")

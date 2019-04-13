from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from classes import State


def keyboard_maker(keyboard_labels):
    my_keyboard = []
    for row in keyboard_labels:
        keyboard_row = []
        for label in row:
            keyboard_row.append(KeyboardButton(text=label))

        my_keyboard.append(keyboard_row)

    return ReplyKeyboardMarkup(keyboard=my_keyboard, resize_keyboard=True)


# button labels
bl_taste_of_tea = '☕️ طعم چای'
bl_soalino = '💡 سوالینو'
bl_contact_us = '☎️ پل‌های ارتباطی'
bl_fragrant_lines = '📖 خطوط خوش عطر'
bl_what_is_taste_of_tea = '🤔 طعم چای چیه؟'
bl_introduction = '📚 معرفی کنید'
bl_want_to_read = '📥 می‌خوام بخونم'
bl_want_to_send = '📤 می‌خوام بفرستم'
bl_what_is_soalino = '🤔 سوالینو چیه؟'
bl_soalino_98 = '🏅 سوالینوی نود و هشت'
bl_soalino_question = '❓ سوال سوالینو'
bl_soalino_send_answer = '✅ ارسال پاسخ سوالینو'
bl_back = '🔙 بازگشت'
bl_goto_main = '📋 منوی اصلی'

# messages
msg_start = 'خوش اومدی 😊'
msg_help = '''برای استفاده از بات میتونی از دکمه‌ها استفاده کنی یا یکی از دستورات زیر رو انتخاب کنی:

شروع کار با بات: /start

بازگشت به صفحه‌ی اصلی: /main_menu

کمک: /help'''

msg_wts = '''کتابایی که گفتیم چه قدر براتون جذاب بود؟
کدوم دیالوگ شما رو به فکر فرو برد؟
کدوم پاراگراف یه جرقه شد تا خیالتون به پرواز در بیاد؟
کدوم صفحه حالتونو خیلی خوب کرد؟

قسمت هایی از کتاب های معرفی شده رو که دوست داشتین و براتون جذاب یا آموزنده بود با ما در میون بذارید تا ما هم تو استوریامون به دوستای دانش آموزتون معرفیشون کنیم.
تا حس خوب کتاب خوندن گسترش پیدا کنه. 📚'''

msg_intro = '''قرار شده ما کتاب معرفی کنیم ولی دلمون میخواد اول از همه از شما بپرسیم دوست دارین چی بخونین؟
چه کتابی هست که تو لیست خوندنه براتون؟
چه کتابیه که مدت ها میخواین بخونین ولی فرصتش پیش نیومده؟
کتاب های خوب بهمون پیشنهاد کنید تا ما بتونیم کتابای بهتر معرفی کنیم.
منتظریما... 📖'''

msg_state = {
    State.MAIN_MENU.value: 'لطفا یکی از گزینه‌ها رو انتخاب کن 🙂',
    State.TASTE_OF_TEA.value: 'به طعم چای خوش اومدی 🙌',
    State.FRAGRANT_LINES.value: 'چیکار می‌خوای بکنی؟! 🤔',
    State.WANT_TO_READ.value: 'میخوای خلاصه کدوم کتابو ببینی؟📕📗📘',
    State.WANT_TO_SEND.value: msg_wts,
    State.INTRODUCTION.value: msg_intro,
    State.SOALINO.value: 'به سوالینو خوش اومدی 🙌',
    State.SOALINO_98.value: 'لطفا انتخاب کن 👀',
}

msg_contact_us = '''همايش زنگ تفريح در دانشگاه
🔔Break Time In University

🔹Contact us:'''

msg_what_is_taste_of_tea = '''سلام.✋🏻🍃
ما تصمیم گرفتیم یک حرکت نو رو شروع کنیم.
با این هدف که عادت خوب مطالعه و کتاب خوانی بینمون دوباره تازه شه.
 قراره طی یک روند منظم کتاب های خوب رو معرفی کنیم...
توی این عصر ها میشه یه لیوان چای برداشت و خستگی در کرد.
ما هم تصمیم گرفتیم اسمی که برای این حرکت نو می ذاریم این باشه:
#طعم_چای
تا چایی که هر بار حالمونو خوب می کنه این دفعه عطر و طعم کتاب و کتاب خونی هم بهش اضافه شه.
#چای_با_طعم_کتاب'''

msg_what_is_soalino = '''یه سنّتِ نو 
یه سوالِ نو 
توی سالِ نو 
#سوالینو 
سوالینو در اصل یه مسابقست که برنده های اون افرادی هستن که بهترین پاسخ رو به سوال ما بدن.'''

msg_soalino_question = '''جنس خوشبختی از چی میتونه باشه؟
وقتی میگیم فرد خوشبخت ،چه توصیفی براش میاد تو ذهنت؟ 
در مورد مفهوم خوشبختی چی فکر می کنی؟

به نظرت خوشبختی واقعا یعنی چی؟
سوالینوی امسال اینه. 
حداکثر تو نود و هشت کلمه به ما بگو: تعریف واقعی خوشبختی چیه؟
پاسخ خودتون رو، در قسمت «ارسال پاسخ سوالینو ✅» برای ما ارسال کنید .'''

msg_soalino_send_answer = '''❌مهلت ارسال پاسخ سوالینو 98 به پایان رسیده است...
منتظر اعلام نتایج باشید...📝'''

# inline keyboards
ikb_contact_us = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='BTIU Contact', url='https://t.me/btiu_contact')],
                     [InlineKeyboardButton(text='Instagram Page', url='https://instagram.com/breaktimeinuniversity')],
                     [InlineKeyboardButton(text='Telegram Channel', url='https://t.me/btiu_channel')],
                     ]
)

# reply keyboards
books_list = [['1️⃣ - جنگ که تمام شد بیدارم کن —- نوشته عباس جهانگیریان'],
              ['2️⃣ - شازده کوچولو —- نوشته آنتوان دو سنت اگزوپری'],
              ['3️⃣ - رز گمشده —- نوشته سردار ازکان']]

rkb_state = {
    State.MAIN_MENU.value: keyboard_maker([[bl_soalino, bl_taste_of_tea], [bl_contact_us]]),
    State.TASTE_OF_TEA.value: keyboard_maker(
        [[bl_what_is_taste_of_tea, bl_fragrant_lines], [bl_introduction, bl_back]]),
    State.FRAGRANT_LINES.value: keyboard_maker([[bl_want_to_read, bl_want_to_send], [bl_back, bl_goto_main]]),
    State.WANT_TO_READ.value: keyboard_maker(books_list + [[bl_back]]),
    State.WANT_TO_SEND.value: keyboard_maker([[bl_back], [bl_goto_main]]),
    State.INTRODUCTION.value: keyboard_maker([[bl_back], [bl_goto_main]]),
    State.SOALINO.value: keyboard_maker([[bl_what_is_soalino, bl_soalino_98], [bl_back]]),
    State.SOALINO_98.value: keyboard_maker([[bl_soalino_question, bl_soalino_send_answer], [bl_back, bl_goto_main]]),
}

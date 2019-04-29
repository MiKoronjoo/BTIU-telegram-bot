from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

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

bl_yes = '✅ بله'
bl_no = '❎ خیر'
bl_st_tiz = 'تیزهوشان و نمونه دولتی'
bl_st_dol = 'دولتی'
bl_st_ghe = 'غیر انتفاعی'
bl_st_othr = 'سایر'
bl_no_idea = 'ایده‌ای ندارم، اطلاعات رو ثبت کن'

# error messages
err_bad_input = 'لطفا یکی از دکمه‌ها رو انتخاب کن!'
err_bad_cmd = '''دستور مورد نظر پیدا نشد 🤷‍♂️
/help'''

err_free_time = 'لطفا ساعات خالی رو با فرمت گفته شده بفرست (5 خط و تو هر خط ساعات آزاد اون روز از هفته رو بنویس!)'
err_photo = 'لطفا عکس رو به عنوان فایل بفرست (send as a file)'
err_size = 'سایز عکس باید کمتر از 10MB باشه!'

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

msg_info = '''لطفا اطلاعات خواسته شده رو کامل و صحیح بفرست 🙂
هرجا که اشتباه شد میتونی با دکمه "🔙 بازگشت" برگردی به مرحله قبل
با تشکر 🙏'''

free_time_msg = '''ساعتای خالی‌ت در طول هفته رو بفرست (حتما به فرمتی که تو مثال زده شده، بفرست)
مثال: 👇

شنبه: 10-12 13:30-17:45
یکشنبه:
دوشنبه: 8-13
سه‌شنبه: 7:30-11
چهارشنبه:'''

sugg_templete = '''[Sender](tg://user?id=%d)
پیشنهاد:

'''

msg_state = {
    State.MAIN_MENU.value: 'لطفا یکی از گزینه‌ها رو انتخاب کن 🙂',
    State.TASTE_OF_TEA.value: 'به طعم چای خوش اومدی 🙌',
    State.FRAGRANT_LINES.value: 'چیکار می‌خوای بکنی؟! 🤔',
    State.WANT_TO_READ.value: 'میخوای خلاصه کدوم کتابو ببینی؟📕📗📘',
    State.WANT_TO_SEND.value: msg_wts,
    State.INTRODUCTION.value: msg_intro,
    State.SOALINO.value: 'به سوالینو خوش اومدی 🙌',
    State.SOALINO_98.value: 'لطفا انتخاب کن 👀',

    State.FULL_NAME.value: 'اسم و فامیل؟',
    State.PICTURE.value: 'لطفا عکست رو برای بات بفرست (عکس رو به عنوان فایل بفرست (as a file) - حداکثر سایز 10MB)',
    State.UNIVERSITY.value: 'رشته و دانشگاه؟',
    State.COMMITTEE.value: 'کدوم کمیته هستی؟',
    State.AGE.value: 'سن؟',
    State.PHONE_NUMBER.value: 'شماره موبایل؟',
    State.SHIRAZI.value: 'شیرازی هستی؟ (برای جواب لطفا از دکمه‌ها استفاده کن)',
    State.SCHOOL_INFO.value: 'اسم دبیرستان خودت همراه با آدرس کلی؟',
    State.SCHOOL_TYPE.value: 'نوع دبیرستانت رو انتخاب کن:',
    State.HOME_ADDR.value: 'محدوده‌ی سکونت؟',
    State.HAVE_CAR.value: 'ماشین داری؟! (لطفا انتخاب کن)',
    State.KNOWN_SCHOOLS.value: 'مدارسی که تو اونا دانش‌آموزای پایه‌های ۹ام تا ۱۲ام رو میشناسی، ذکر کن!',
    State.FREE_TIMES.value: free_time_msg,
    State.IDEA_AT_ALL.value: 'از هر ایده ای در مورد تبلیغات در مدارس استقبال می‌شود 🙂',
}

msg_tnx = 'ممنون که وقت گذاشتی 🙂🌺'
msg_tnx_s = 'ممنون از پیشنهادت 🙂🌺'

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

info_template = '''[TELEGRAM](tg://user?id=%d)
👤 اسم: %s
👨‍🎓 رشته و دانشگاه: %s
💪 کمیته: %s
👶 سن: %s
📱 شماره موبایل: %s
🏫 اسم دبیرستان و آدرس: %s
🏫 نوع دبیرستان: %s
🏘 محدوده سکونت: %s
🚙 ماشین داری؟ %s
🏫 مدارسی که میشناسی:
%s

🔥 ایده:
%s

⏰ وقت های آزاد:
'''


# inline keyboards
ikb_contact_us = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='BTIU Contact', url='https://t.me/btiu_contact')],
                     [InlineKeyboardButton(text='Instagram Page', url='https://instagram.com/breaktimeinuniversity')],
                     [InlineKeyboardButton(text='Telegram Channel', url='https://t.me/btiu_channel')],
                     ]
)

# reply keyboards
book1 = '1️⃣ - جنگ که تمام شد بیدارم کن —- نوشته عباس جهانگیریان'
book2 = '2️⃣ - شازده کوچولو —- نوشته آنتوان دو سنت اگزوپری'
book3 = '3️⃣ - رز گمشده —- نوشته سردار ازکان'
book4 = '4️⃣ - راز فال ورق —- نوشته یوستین گردر'

text1 = '''حوری مثل همیشه نیست. مثل آهویی است که از ترس پلنگی رمیده و پناه آورده به من.

_منو از این‌جا ببر!

_کجا ببرم؟!

_هر جا می‌خوای ببر!

_چی شده؟!




دیالوگ رمز آلود بالا، "حوری" یکی از شخصیت ها ی داستان را معرفی می کند؛ اما قصه، قصه ی حوری نیست.
 داستان در مورد "حامی" نوجوان پانزده ساله ای است که با شروع جنگ و از دست دادن پدر و مادر و خواهر و برادرش با "بی بی" و "دایی عباس" از آبادان به قم می آید.

در طول داستان با روزمرگی ها، تنهایی ها، امید ها و دلبستگی های حامی همراه می شویم.

رمان فضای سیال و پر گفت و گویی دارد و ضد جنگ بودن آن حتی از عنوان کتاب بر می آید.

آنچه بیش از همه کتاب را دلنشین و دوست داشتنی می کند، توصیف عشق بین دو نوجوان است، در نهایت پاکی و شفافیت کودکانه.



درباره ی نویسنده:
عباس جهانگیریان 35 داستان، نمایشنامه و فیلمنامه در کارنامه ی خود دارد. آثار او در نهاد هایی مانند شورای کتاب کودک، کانون پرورش فکری، کتاب فصل و جایزه ی ادبی اصفهان برگزیده یا تقدیر شده اند.
براساس دو کتاب هامون و شازده کدو دو فیلم سینمایی به کارگردانی ابراهیم فروزش در دست ساخت است.
هم چنین دو کتاب او در جمهوری های ارمنستان و قزاقستان ترجمه و منتشر شده اند.'''

text2 = '''روباه گفت : آدم ها این حقیقت را فراموش کرده اند اما تو نباید فراموش کنی، تو تا زنده ای نسبت به آنی که اهلی کرده ای مسئولی!  تو مسئول گُلِتی...




شازده کوچولو ساکن سیاره‌ی کوچکی به اندازه‌ی یک خانه‌ی معمولی است و در آن جا گل بی‌همتایی دارد که مایه‌ی همه‌ی عواطف و دلخوشی‌ها و رنج‌های اوست.

 خواننده اندک اندک با سرگذشت این موجود کوچولوی دوست‌داشتنی آشنا می‌شود و پی می‌برد که چرا او روزی تصمیم به ترک وطن می‌گیرد و پس از عبور از شش سیاره به سیاره‌ی هفتم، یعنی کره‌ی زمین می‌رسد. 

در این جا با روباهی آشنا می‌شود که مهم‌ترین راز زندگی را بر او آشکار می‌کند.

درباره ی نویسنده:
اگزوپری در شهر لیون و در یک خانواده ی کاتولیک مرفه به دنیا آمد. او فرزند سوم از پنج فرزند خانواده‌ی اگزوپری است. اگزوپری تا قبل از جنگ جهانی دوم ،خلبان تجاری موفقی به حساب می آمد و در خطوط پست هوایی میان اروپا، آفریقا و آمریکای جنوبی فعالیت میکرد. اما با شروع جنگ به نیروی هوایی فرانسه آزاد در شمال آفریقا پیوست .

«شازده کوچولو» متولد روزی است که هواپیمای اگزوپری در یکی از پروازهایش در صحرای آفریقا به دلیل مشکل فنی فرود آمد .'''

text3 = '''به دیگرانی که شما را از خودتان دزدیده اند اعتراض کنید.


رمان رز گمشده، داستان تکاپوی دختری است برای پیدا کردن خواهر گمشده اش.

داستان جست و جوی "دیانا" برای یافتن  خواهرش "مری" ، در تلاش برای رساندن این معناست که هر آدمی، گمشده ای دارد که باید برای پیدا کردنش از وجود و درون خود شروع کند و گاهی وقت ها درون انسان ها تا حدی تاریک و سیاه می شود که دیگر برای جستجو جایی را نمی توان دید.

در بخش هایی از این رمان تحسین شده می خوانیم:

_برای آنکه فکر نکنی چیزی را از دست داده ای، آنچه را در درون توست در بیرون جست و جو نکن.

_برای دلبسته شدن قبل از هر چیز، وارستگی لازم است.

_تا وقتی که زمان دارد به سوی آینده جاری می شود، آن آینده ای که مسحورش شده ایم، چیزی نیست جز گذشته ای بکر .'''

text4 = '''نشسته بودم و فکر می کردم چقدر غم انگیز است که مردم طوری بار می آیند که به چیزی شگفت انگیز چون زندگی عادت می کنند.



راز فال ورق در مورد پدر و پسری است که سال ها پیش مادر،  آنها را ترک کرده است. آن دو دیگر خبری از او ندارند تا یک روز که در یک مجله ی مُد، سرنخ هایی برای پیدا کردن او می یابند.
پدر و پسر روانه یک سفر زمینی در طول اروپا با ماشین شان می شوند تا مادر را پیدا کنند و به خانه بیاورند
هر فصل این کتاب به یک ورق نسبت داده شده است و یوستین گوردر با ارتباط دادن فصل ها یک شاهکار خلق می کند.

او در این کتاب مبانی و مفاهیم عمیق فلسفی را در قالب یک داستان و به زبان ساده بیان می کند.

یوستین گوردر از داستان ها و شهرهای فلاسفه می گوید و اصلی ترین پرسش های انسان را که "ما چه کسی هستیم؟ از کجا آمده ایم؟ و به چه شکل موجودیت پیدا کرده ایم؟” را در مکالمات ساده بین پدر و پسر و در یک کتاب کلوچه ای عجیب بیان می کند.'''

books_list = [[book1],
              [book2],
              [book3],
              [book4]]

book_dic = {
    book1: text1,
    book2: text2,
    book3: text3,
    book4: text4
}

rkb_back = keyboard_maker([[bl_back]])

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

    State.FULL_NAME.value: ReplyKeyboardRemove(),
    State.PICTURE.value: rkb_back,
    State.UNIVERSITY.value: rkb_back,
    State.COMMITTEE.value: rkb_back,
    State.AGE.value: rkb_back,
    State.PHONE_NUMBER.value: rkb_back,
    State.SHIRAZI.value: keyboard_maker([[bl_no, bl_yes], [bl_back]]),
    State.SCHOOL_INFO.value: rkb_back,
    State.SCHOOL_TYPE.value: keyboard_maker([[bl_st_tiz], [bl_st_dol], [bl_st_ghe], [bl_st_othr], [bl_back]]),
    State.HOME_ADDR.value: rkb_back,
    State.HAVE_CAR.value: keyboard_maker([[bl_no, bl_yes], [bl_back]]),
    State.KNOWN_SCHOOLS.value: rkb_back,
    State.FREE_TIMES.value: rkb_back,
    State.IDEA_AT_ALL.value: keyboard_maker([[bl_no_idea], [bl_back]]),
}

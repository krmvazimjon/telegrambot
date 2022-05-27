import logging
from myconfig import API_TOKEN # yoki * bolsa hammasi
from buttons import * 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
import sqlite3
#from loader import dp

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
admin = 913748839

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
        id integer PRIMARY KEY,
        usename varchar(15),
        id_numbers integer
        )""")
    connection.commit()

    check - message.chat.id 
    cursor.execute(f"SELECT id FROM user WHERE id = {check}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO user VALUES (?,?,?)", user_id)
        connection.commit()
        await message.reply("Xush kelibsiz!", reply_markup = setting)
    else:
        await message.answer("Siz ro'yhatda borsiz")

@dp.message_handler(commands = ['alluser'], user_id = 913748839)
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    count = message.chat.id
    cursor.execute("SELECT COUNT(id) from users")
    data = cursor.fetchall()
    for i in data:
        x = i[0]
        await message.answer(f"{x} ta foydalanuvchi mavjud")

##### telfon raqam
@dp.message_handler(content_types = ['contact'])
async def contact(message):
    print(message.contact['phone_number'])
    await message.answer("telfon raqarmi")


###### har xil xabarla
@dp.message_handler()
async def send_welcome(message: types.Message):
    await bot.send_message(admin,f"username: @{message.from_user.username} \nid: {message.from_user.id} \nXabari: {message.text}")

###########################################zakaz olishi 
@dp.message_handler(text = "🛍 Buyurtma berish")
async def send_welcome(message: types.Message):
    await message.reply("📗Bu menyu Marhamat", reply_markup = foods)

############################################################ lavash ################################################################
@dp.callback_query_handler(text = "lavash")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("img/lavash.jpg","rb"), caption = "Lavashning Turlari", reply_markup = Lavash)
    await call.message.delete()

# back knopkasi
@dp.callback_query_handler(text = "back1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

#######################################Mol gushtli lavash turi
@dp.callback_query_handler(text = "cow")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Cow)

# back knopkasi
@dp.callback_query_handler(text = "back2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini lavash
@dp.callback_query_handler(text = "min1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/minilavash.jpg","rb"),caption = """Narxi: 18000
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number)
    await call.message.delete()

# back knopkasi
@dp.callback_query_handler(text = "back3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Cow)

#classic lavash
@dp.callback_query_handler(text = "classic1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/minilavash.jpg","rb"),caption = """Narxi: 22000
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number2)
    await call.message.delete()

# back knopkasi
@dp.callback_query_handler(text = "back4")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Cow)

###########################################tovuq lavash
@dp.callback_query_handler(text = "chicken")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Chicken)

# back knopkasi
@dp.callback_query_handler(text = "back5")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini tovuqli lavash
@dp.callback_query_handler(text = "min2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/minilavash.jpg","rb"),caption = """Narxi: 18000
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number3)
    await call.message.delete()

# back knopkasi
@dp.callback_query_handler(text = "back6")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Chicken)

#classic tovuqli lavash
@dp.callback_query_handler(text = "classic2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/minilavash.jpg","rb"),caption = """Narxi: 22000
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number3)

# back knopkasi
@dp.callback_query_handler(text = "back7")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Chicken)

#########################################qalampir lavash
@dp.callback_query_handler(text = "cow+")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Qalampir)

# back knopkasi
@dp.callback_query_handler(text = "back8")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini qalampir lavash
@dp.callback_query_handler(text = "min3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/garimdori_lavash.jpg","rb"),caption = """Narxi: 19000
Tarkibi: Xamir, go`sht, garmdori chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number4)

# back knopkasi
@dp.callback_query_handler(text = "back9")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Qalampir)

#classic qalampir lavash
@dp.callback_query_handler(text = "classic3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/garimdori_lavash.jpg","rb"),caption = """Narxi: 22000
Tarkibi: Xamir, go`sht, garmdori, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number5)

# back knopkasi
@dp.callback_query_handler(text = "back10")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Qalampir)

#######################################qalampir tovuq lavash
@dp.callback_query_handler(text = "chicken+")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Qalampir2)

# back knopkasi
@dp.callback_query_handler(text = "back11")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini qalampir tovuq lavash
@dp.callback_query_handler(text = "min4")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/garimdori_tovuqlilavash.jpg","rb"),caption = """Narxi: 19000
Tarkibi: Xamir,tovuq go`sht, garmdori chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number7)

# back knopkasi
@dp.callback_query_handler(text = "back12")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Qalampir2)

#classic qalampir tovuq lavash
@dp.callback_query_handler(text = "classic4")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/garimdori_tovuqlilavash.jpg","rb"),caption = """Narxi: 22000
Tarkibi: Xamir, tovuq go`sht, garmdori, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number8)

# back knopkasi
@dp.callback_query_handler(text = "back13")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Qalampir2)

######################################pishloq lavash
@dp.callback_query_handler(text = "cow++")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Pishloq)

# back knopkasi
@dp.callback_query_handler(text = "back14")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini pishloq lavash
@dp.callback_query_handler(text = "min5")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/pishloqli_lavash.jpg","rb"),caption = """Narxi: 20000
Tarkibi: Xamir, go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number9)

# back knopkasi
@dp.callback_query_handler(text = "back15")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Pishloq)

#classic pishloq lavash
@dp.callback_query_handler(text = "classic5")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/pishloqli_lavash.jpg","rb"),caption = """Narxi: 25000
Tarkibi: Xamir, go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number10)

# back knopkasi
@dp.callback_query_handler(text = "back16")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Pishloq)

##################################pishloq tovuq lavash
@dp.callback_query_handler(text = "chicken++")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Pishloq2)

# back knopkasi
@dp.callback_query_handler(text = "back17")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini pishloq tovuq lavash
@dp.callback_query_handler(text = "min6")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/pishloqli_tovuqli_lavash.jpg","rb"),caption = """Narxi: 20000
Tarkibi: Xamir, tovuq go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number11)

# back knopkasi
@dp.callback_query_handler(text = "back18")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Pishloq2)

#classic pishloq tovuq lavash
@dp.callback_query_handler(text = "classic6")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/pishloqli_tovuqli_lavash.jpg","rb"),caption = """Narxi: 25000
Tarkibi: Xamir,tovuq go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number12)

# back knopkasi
@dp.callback_query_handler(text = "back19")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Pishloq2)

##################################Fitter
@dp.callback_query_handler(text = "fitter")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Fitter)

# back knopkasi
@dp.callback_query_handler(text = "back20")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Lavashning Turlari", reply_markup = Lavash)

#mini pishloq tovuq lavash
@dp.callback_query_handler(text = "min7")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/fitter.jpg","rb"),caption = """Narxi: 17000
Tarkibi: Fitter,  go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number13)

# back knopkasi
@dp.callback_query_handler(text = "back21")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Fitter)

#classic pishloq tovuq lavash
@dp.callback_query_handler(text = "classic7")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/fitter.jpg","rb"),caption = """Narxi: 21000
Tarkibi: Fitter , go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting """, reply_markup = number14)

# back knopkasi
@dp.callback_query_handler(text = "back22")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Fitter)

######################################################## Hotdog ################################################################
@dp.callback_query_handler(text = "hotdog")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Hot-Dogning Turlari", reply_markup = Hotdog)

# back knopkasi
@dp.callback_query_handler(text = "back23")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

################################ Double Hotdog
@dp.callback_query_handler(text = "hotdog1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/double-hotdog.jpg","rb"),caption = """Narxi: 17 000 so'm. 
Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.""", reply_markup = number15)

# back knopkasi
@dp.callback_query_handler(text = "back24")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Hotdog)

################################# Classic Hotdog
@dp.callback_query_handler(text = "cl_hotdog")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/classic_hotdog.jpg","rb"),caption = """Narxi: 8 000 so'm.
Kulcha, sosiska, ketchup va xantal, qovurilgan piyoz. """, reply_markup = number16)

# back knopkasi
@dp.callback_query_handler(text = "back25")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Hotdog)

################################# Karalevski Hotdog
@dp.callback_query_handler(text = "crown")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/karalevski_hotdog.jpg","rb"),caption = """Narxi: 15 000 so'm.
Kulcha, sosiska, ketchup va xantal, qovurilgan piyoz. """, reply_markup = number17)

# back knopkasi
@dp.callback_query_handler(text = "back26")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Hotdog)

################################# Tovuqli Hotdog
@dp.callback_query_handler(text = "chickenhot")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/tovuqli_hotdog.jpg","rb"),caption = """Narxi: 17 000 so'm.
Kulcha, tovuq go'shti, ketchup va xantal, qovurilgan piyoz. """, reply_markup = number18)

# back knopkasi
@dp.callback_query_handler(text = "back27")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Hotdog)

######################################################### Sandvich ###########################################################
@dp.callback_query_handler(text = "sendvich")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Sandvichning Turlari", reply_markup = Sandvich)

# back knopkasi
@dp.callback_query_handler(text = "back28")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

################################# Classic sandvich
@dp.callback_query_handler(text = "clsandvich")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/classic_sandvich.jpg","rb"),caption = """Narxi: 22 000 so'm.
Kulcha, tovuq go'shti, pomidor, sous,  piyoz. """, reply_markup = number19)

# back knopkasi
@dp.callback_query_handler(text = "back29")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Sandvich)

################################# Tovuqli Sandvich
@dp.callback_query_handler(text = "tvsandvich")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/classic_sandvich.jpg","rb"),caption = """Narxi: 22 000 so'm.
Kulcha, go'shti, pomidor, garimdori, sous,  piyoz. """, reply_markup = number20)

# back knopkasi
@dp.callback_query_handler(text = "back30")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Sandvich)

######################################################### Shaurma ##################################################################
@dp.callback_query_handler(text = "shaurma")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/shaurmalar.jpg","rb"),
        caption = "Shaurmaning Turlari",reply_markup = Shaurma)

# back knopkasi
@dp.callback_query_handler(text = "back31")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

####################################### Mol gushtli shaurma
@dp.callback_query_handler(text = "cow2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Cow_shaurma)

# back knopkasi
@dp.callback_query_handler(text = "back32")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Shaurmaning Turlari", reply_markup = Shaurma)

#mini goshtli shaurma
@dp.callback_query_handler(text = "min8")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/molgoshtli_shaurma.jpg","rb"),
        caption = """Kulcha, go'sht, pomidor, sous,  piyoz. 
Narxi: 18 000 so'm. """, reply_markup = number21)

# back knopkasi
@dp.callback_query_handler(text = "back33")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Cow_shaurma)

#classic shaurma goshtli
@dp.callback_query_handler(text = "classic8")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/molgoshtli_shaurma.jpg","rb"),
        caption = """Kulcha, go'sht, pomidor, sous,  piyoz. 
Narxi: 22 000 so'm. """, reply_markup = number22)

# back knopkasi
@dp.callback_query_handler(text = "back34")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Cow_shaurma)

####################### Tovuq Goshtli Shaurma 
@dp.callback_query_handler(text = "chicken2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Chicken_shaurma)

# back knopkasi
@dp.callback_query_handler(text = "back35")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Shaurmaning Turlari", reply_markup = Shaurma)

#mini tovuqli shaurma
@dp.callback_query_handler(text = "min9")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/tovuqlishaurma.jpg","rb"),
        caption = """Kulcha, go'sht, pomidor, sous,  piyoz. 
Narxi: 18 000 so'm. """, reply_markup = number23)

# back knopkasi
@dp.callback_query_handler(text = "back36")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Chicken_shaurma)

#classic shaurma tovuqli
@dp.callback_query_handler(text = "classic9")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/tovuqlishaurma.jpg","rb"),
        caption = """Kulcha, go'sht, pomidor, sous,  piyoz. 
Narxi: 22 000 so'm. """, reply_markup = number24)

# back knopkasi
@dp.callback_query_handler(text = "back37")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = Chicken_shaurma)

########################Gosht Garimdori shaurma
@dp.callback_query_handler(text = "cow3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = G_shaurma)

# back knopkasi
@dp.callback_query_handler(text = "back38")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Shaurmaning Turlari", reply_markup = Shaurma)

#mini garimdori gushtli shaurma
@dp.callback_query_handler(text = "min10")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/molgoshtli_shaurma.jpg","rb"),
        caption = """Kulcha, go'sht, garimdori, pomidor, sous,  piyoz. 
Narxi: 18 000 so'm. """, reply_markup = number25)

# back knopkasi
@dp.callback_query_handler(text = "back39")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = G_shaurma)

#classic shaurma gushtli garimdori
@dp.callback_query_handler(text = "classic10")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/molgoshtli_shaurma.jpg","rb"),
        caption = """Kulcha, go'sht, pomidor, garimdori, sous,  piyoz. 
Narxi: 22 000 so'm. """, reply_markup = number26)

# back knopkasi
@dp.callback_query_handler(text = "back40")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = G_shaurma)

#############Tovuq garimdori shaurma
@dp.callback_query_handler(text = "chicken3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = T_shaurma)

# back knopkasi
@dp.callback_query_handler(text = "back41")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Shaurmaning Turlari", reply_markup = Shaurma)

#mini garimdori tovuqli shaurma
@dp.callback_query_handler(text = "min11")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/tovuqlishaurma.jpg","rb"),
        caption = """Kulcha, tovuq go'shti, pomidor, garimdori, sous,  piyoz. 
Narxi: 20 000 so'm.. """, reply_markup = number27)

# back knopkasi
@dp.callback_query_handler(text = "back42")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = T_shaurma)

#classic shaurma tovuqli garimdori
@dp.callback_query_handler(text = "classic11")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/tovuqlishaurma.jpg","rb"),
        caption = """Kulcha, tovuq go'shti, pomidor, garimdori, sous,  piyoz. 
Narxi: 22 000 so'm.""", reply_markup = number28)

# back knopkasi
@dp.callback_query_handler(text = "back43")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Qaysi birini tanlaysiz", reply_markup = T_shaurma)

################################################## Gamburgers ################################################################
@dp.callback_query_handler(text = "burger")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Gamburgerning Turlari", reply_markup = Hamburger)

# back knopkasi
@dp.callback_query_handler(text = "back44")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

################################# gamburger
@dp.callback_query_handler(text = "gamburger")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/hamburger.jpg","rb"),
        caption = """Gamburger 18000mig so'm """, reply_markup = number29)

# back knopkasi
@dp.callback_query_handler(text = "back45")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Hamburger)

################################# Chizburger
@dp.callback_query_handler(text = "chizburger")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/chizburger.jpg","rb"),
        caption = """Chizburger 21000mig so'm """, reply_markup = number30)

# back knopkasi
@dp.callback_query_handler(text = "back46")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Hamburger)

################################################### Donar #######################################################################
@dp.callback_query_handler(text = "donar")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Donarning Turlari", reply_markup = Donar)

# back knopkasi
@dp.callback_query_handler(text = "back47")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

################################# Gushtli donar
@dp.callback_query_handler(text = "d_gosht")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/donar_gushtli.jpg","rb"),
        caption = """Donar go'shtli 23000mig so'm""", reply_markup = number31)

# back knopkasi
@dp.callback_query_handler(text = "back48")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Donar)

################################# Tovuqli Donar
@dp.callback_query_handler(text = "d_tovuq")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/donar_tovuqlik.jpg","rb"),
        caption = """Donar tov 21000mig so'm """, reply_markup = number32)

# back knopkasi
@dp.callback_query_handler(text = "back49")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Donar)

####################################################### Gazaklar ################################################################
@dp.callback_query_handler(text = "gazak")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Gazaklarning Turlari", reply_markup = Gazaklar)

# back knopkasi
@dp.callback_query_handler(text = "back50")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

################################# free 150gr
@dp.callback_query_handler(text = "free")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/frie.jpg","rb"),
        caption = """Frie 6000mig so'm""", reply_markup = number33)

# back knopkasi
@dp.callback_query_handler(text = "back51")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Gazaklar)

################################# derevenski free
@dp.callback_query_handler(text = "free2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/derevenski.jpg","rb"),
        caption = """Derevenski 8000mig so'm """, reply_markup = number34)

# back knopkasi
@dp.callback_query_handler(text = "back52")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Gazaklar)

################################# Kicik guruch
@dp.callback_query_handler(text = "kicik_g")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/guruch_katta.jpg","rb"),
        caption = """Guruch katta 4000mig so'm""", reply_markup = number35)

# back knopkasi
@dp.callback_query_handler(text = "back53")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Gazaklar)

################################# Katta guruch
@dp.callback_query_handler(text = "katta_g")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/guruch_katta.jpg","rb"),
        caption = """Guruch katta 8000mig so'm""", reply_markup = number36)

# back knopkasi
@dp.callback_query_handler(text = "back54")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Gazaklar)

######################################################## Drinks ###############################################################
@dp.callback_query_handler(text = "drinks")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Ichimlikning Turlari", reply_markup = Drinks)

# back knopkasi
@dp.callback_query_handler(text = "back55")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

################################# Cofee and tea
@dp.callback_query_handler(text = "teaandcofe")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Coffee va Choy""", reply_markup = Cofeandtea)

# back knopkasi
@dp.callback_query_handler(text = "back56")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Drinks)

####################### Coffee 
@dp.callback_query_handler(text = "cofe")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Coffee ning turlari""", reply_markup = Coffee)

# back knopkasi
@dp.callback_query_handler(text = "back57")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Cofeandtea)

###########Cofferlar
######Cofe1
@dp.callback_query_handler(text = "cofe1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/americano.jpg","rb"),
        caption = """Americano 12000mig so'm""", reply_markup = Cofe1)

# back knopkasi
@dp.callback_query_handler(text = "back58")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Coffee)

##########cofe2
@dp.callback_query_handler(text = "cofe2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Big or Small""", reply_markup = Cofe2)

# back knopkasi
@dp.callback_query_handler(text = "back59")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Coffee)

########### cap small
@dp.callback_query_handler(text = "cap1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/cappucino.jpg","rb"),
        caption = """Capuchino small 80g ☕️ 10000mig so'm""", reply_markup = Cap1)

# back knopkasi
@dp.callback_query_handler(text = "back66")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Cofe2)

########### cap big
@dp.callback_query_handler(text = "cap2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/cappucino.jpg","rb"),
        caption = """Capuchino big 120g☕️ 15000mig so'm""", reply_markup = Cap2)

# back knopkasi
@dp.callback_query_handler(text = "back67")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Cofe2)

############ Cofe3
@dp.callback_query_handler(text = "cofe3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/3v1.jpg","rb"),
        caption = """Coffee3v1 4000mig so'm""", reply_markup = Cofe3)

# back knopkasi
@dp.callback_query_handler(text = "back60")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Coffee)

#############Cofe4
@dp.callback_query_handler(text = "cofe4")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Big or Small""", reply_markup = Cofe4)

# back knopkasi
@dp.callback_query_handler(text = "back61")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Coffee)

########### latte small
@dp.callback_query_handler(text = "latte1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/latte.jpg","rb"),
        caption = """Latte small 80g☕️ 10000mig so'm""", reply_markup = Lat1)

# back knopkasi
@dp.callback_query_handler(text = "back69")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Cofe4)

########### latte big
@dp.callback_query_handler(text = "latte2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/latte.jpg","rb"),
        caption = """Latte big 120g☕️ 15000mig so'm""", reply_markup = Lat2)

# back knopkasi
@dp.callback_query_handler(text = "back70")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Cofe4)


################# Tea
@dp.callback_query_handler(text = "tea")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Choyningning turlari""", reply_markup = Tea)

# back knopkasi
@dp.callback_query_handler(text = "back62")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Cofeandtea)

############# Choylar
@dp.callback_query_handler(text = "tea1")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/choyqora.jpg","rb"),
        caption = """Choy qora 3000mig so'm""", reply_markup = Tea1)

# back knopkasi
@dp.callback_query_handler(text = "back63")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Tea)

@dp.callback_query_handler(text = "tea2")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/choyqora.jpg","rb"),
        caption = """Choy ko'k 3000mig so'm""", reply_markup = Tea2)

# back knopkasi
@dp.callback_query_handler(text = "back64")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Tea)

@dp.callback_query_handler(text = "tea3")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/choyqora.jpg","rb"),
        caption = """Choy limon 6000mig so'm""", reply_markup = Tea3)

# back knopkasi
@dp.callback_query_handler(text = "back65")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Tea)

#######################Cola fanta pepsi sprite
@dp.callback_query_handler(text = "freshdrinks")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Kategoriyadan birini tanlang""", reply_markup = Freshdrinks)

# back knopkasi
@dp.callback_query_handler(text = "back71")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Drinks)

####Cola
@dp.callback_query_handler(text = "cola")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/cola.jpg","rb"),
        caption = """Coca-Cola 5000mig so'm""", reply_markup = Cola)

# back knopkasi
@dp.callback_query_handler(text = "back72")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Freshdrinks)

####Fanta
@dp.callback_query_handler(text = "fanta")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/fanta.jpg","rb"),
        caption = """Fanta 5000mig so'm""", reply_markup = Fanta)

# back knopkasi
@dp.callback_query_handler(text = "back73")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Freshdrinks)

####Sprite
@dp.callback_query_handler(text = "sprite")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/sprite.jpg","rb"),
        caption = """Sprite 5000mig so'm""", reply_markup = Sprite)

# back knopkasi
@dp.callback_query_handler(text = "back74")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Freshdrinks)

####Pepsi
@dp.callback_query_handler(text = "pepsi")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/pepsi.jpg","rb"),
        caption = """Pepsi 5000mig so'm""", reply_markup = Pepsi)

# back knopkasi
@dp.callback_query_handler(text = "back75")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Freshdrinks)

####################### Natural drinks
@dp.callback_query_handler(text = "natural")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("""Kategoriyadan birini tanlang""", reply_markup = Natural)

# back knopkasi
@dp.callback_query_handler(text = "back76")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Drinks)

####Bliss
@dp.callback_query_handler(text = "bliss")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/bliss.jpg","rb"),
        caption = """Sok Bliss 10000mig so'm""", reply_markup = Bliss)

# back knopkasi
@dp.callback_query_handler(text = "back77")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Natural)

####apple
@dp.callback_query_handler(text = "fresh")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/freshsabzi.jpg","rb"),
        caption = """Fresh sabzi + olma 13000mig so'm""", reply_markup = Apple)

# back knopkasi
@dp.callback_query_handler(text = "back78")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Natural)

#################################################### Desertlar #####################################################################
@dp.callback_query_handler(text = "desert")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/desert.jpg","rb"),
        caption = "Desertning Turlari", reply_markup = Sweets)

# back knopkasi
@dp.callback_query_handler(text = "back79")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

####assalim
@dp.callback_query_handler(text = "asal")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/assalim.jpg","rb"),
        caption = """Аnʼnaviy taʼm - asal asosidagi biskvit va krem 
Narxi: 14 000 so'm""", reply_markup = Asal)

# back knopkasi
@dp.callback_query_handler(text = "back80")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Sweets)

####choco
@dp.callback_query_handler(text = "choco")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/choco.jpg","rb"),
        caption = """Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem 
Narxi: 14 000 so'm""", reply_markup = Choco)

# back knopkasi
@dp.callback_query_handler(text = "back81")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Sweets)

####qulupnay
@dp.callback_query_handler(text = "qulupnay")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/qulupnay.jpg","rb"),
        caption = """Qulupnayli Muss 
Narxi: 14 000 so'm""", reply_markup = Qulupnay)

# back knopkasi
@dp.callback_query_handler(text = "back82")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Sweets)

############################################ Pizza ########################################################################
@dp.callback_query_handler(text = "pizza")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Ichimlikning Turlari", reply_markup = Pizza)

# back knopkasi
@dp.callback_query_handler(text = "back83")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("📗Bu menyu Marhamat", reply_markup = foods)

####peperonni
@dp.callback_query_handler(text = "pep")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/peperonni.jpg","rb"),
        caption = """Пицца Пепперони

Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто
Сыр 110 гр.

Narxi: 65 000 so'm""", reply_markup = Peperonni)

# back knopkasi
@dp.callback_query_handler(text = "back84")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Pizza)

####margaritta
@dp.callback_query_handler(text = "mar")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/margarita.jpg","rb"),
        caption = """Пицца "Маргарита"

Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры

Narxi: 53 000 so'm""", reply_markup = Margaritta)

# back knopkasi
@dp.callback_query_handler(text = "back85")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Pizza)

####ananas
@dp.callback_query_handler(text = "ananas")
async def send_welcome(call: CallbackQuery):
    await call.message.answer_photo(photo = open("img/ananas.jpg","rb"),
        caption = """Пицца с Ананасом

Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
Грибы

Narxi: 65 000 so'm""", reply_markup = Ananas)

# back knopkasi
@dp.callback_query_handler(text = "back86")
async def send_welcome(call: CallbackQuery):
    await call.message.answer("Nimadan Boshlaymiz", reply_markup = Pizza)










# @dp.message_handler(text = "🇺🇿 O'zbekcha")
# async def send_welcome(message: types.Message):
#     await message.reply("Good job man.", reply_markup = m2)

# oddiy knopka 
# @dp.message_handler(text = "🇺🇸 English")
# async def send_welcome(message: types.Message):
#     await message.reply("Good", reply_markup = m3)

#tepada chiqodigon knopka
# @dp.callback_query_handler(text = "ku")
# async def menu_tanlash(call:CallbackQuery):
#     await call.message.answer(f"<b>Assalom Alaykum</b>", parse_mode = "HTML", reply_markup = m2)

# @dp.callback_query_handler(text = "co")
# async def menu_tanlash(call:CallbackQuery):
#     await call.message.answer(f"<b>Hi Welcome</b>", parse_mode = "HTML", reply_markup = m3)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Tilni tanlang!\nChoose language", reply_markup = mainmenu)
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
# """buttonga javob qaytarish """
# @dp.callback_query_handler(text = "uz")
# async def menu_tanlash(call:CallbackQuery):
#     await call.message.answer(f"<b>Assalom Alaykum</b>", parse_mode = "HTML", reply_markup = m2)

# @dp.callback_query_handler(text = "ku")
# async def menu_tanlash2(call:CallbackQuery):
#     await call.message.answer(f"<b>Bizning kursimizda:</b>", parse_mode = "HTML", reply_markup = k2)

# @dp.callback_query_handler(text = "it")
# async def menu_tanlash2(call:CallbackQuery):
#     await call.message.answer(f"<b>Python\nJavaScript\nC# and C++</b>", parse_mode = "HTML")

# @dp.callback_query_handler(text = "smm")
# async def menu_tanlash2(call:CallbackQuery):
#     await call.message.answer(f"<b>Kurs davomiyligi 6oy\nHaftada 3 kun\nNarxi:500000</b>", parse_mode = "HTML")

# @dp.callback_query_handler(text = "en")
# async def menu_tanlash(call:CallbackQuery):
#     await call.message.answer(f"<b>Hi Welcome</b>", parse_mode = "HTML", reply_markup = m3)

# @dp.callback_query_handler(text = "co")
# async def menu_tanlash2(call:CallbackQuery):
#     await call.message.answer(f"<b>In our course have:</b>", parse_mode = "HTML", reply_markup = k3)

# @dp.callback_query_handler(text = "it2")
# async def menu_tanlash2(call:CallbackQuery):
#     await call.message.answer(f"<b>Python\nJavaScript\nC# and C++</b>", parse_mode = "HTML")

# @dp.callback_query_handler(text = "smm2")
# async def menu_tanlash2(call:CallbackQuery):
#     await call.message.answer(f"<b>Smm course will be 6 month\n3 times in one week\nPrice:500000</b>", parse_mode = "HTML")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#     if message.text == "Salom":
#         await message.answer("what's up\nNigga", reply_markup = mainmenu)
#     # if message.text == isdigit():
#     #     await message.text("raqam yozma ,soz yoz!")
#     #await message.answer(message.text)
#     elif message.text:
#         await message.answer("Go home", reply_markup = mainmenu)

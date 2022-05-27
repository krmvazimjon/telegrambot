from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# zakaz olishi
setting = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "🛍 Buyurtma berish"),
			KeyboardButton(text = "Phone number")
		],
		[
			KeyboardButton(text = "⚙️ Sozlamalar" ),
			KeyboardButton(text = "📞 Biz bilan aloqa")
		]
	],
	resize_keyboard = True
)
############################ asosiy menyu foods di 
foods = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "Lavash🌯", callback_data = "lavash"),
			InlineKeyboardButton(text = "Hod Dog🌭", callback_data = "hotdog"),
		],
		[
			InlineKeyboardButton(text = "Sandvich Club🥪", callback_data = "sendvich"),
			InlineKeyboardButton(text = "Shaurma🥙", callback_data = "shaurma"),
		],
		[
			InlineKeyboardButton(text = "Burger🍔", callback_data = "burger"),
			InlineKeyboardButton(text = "Donar🍲", callback_data = "donar"),
		],
		[
			InlineKeyboardButton(text = "Gazaklar🍟", callback_data = "gazak"),
			InlineKeyboardButton(text = "Ichimliklar🥤", callback_data = "drinks"),
		],
		[
			InlineKeyboardButton(text = "Desertlar🍩", callback_data = "desert"),
			InlineKeyboardButton(text = "Pizza🍕", callback_data = "pizza")
		],
	],
)
############################lavash menyu
Lavash = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mol Goshtlik🥩", callback_data = "cow"),
			InlineKeyboardButton(text = "Tovuq Goshtlik🍗", callback_data = "chicken"),
		],
		[
			InlineKeyboardButton(text = "Qalampir + Mol🥩🌶", callback_data = "cow+"),
			InlineKeyboardButton(text = "Qalampir + Tovuq🍗🌶", callback_data = "chicken+"),
		],
		[
			InlineKeyboardButton(text = "Pishloq + Mol🥩🧀", callback_data = "cow++"),
			InlineKeyboardButton(text = "Pishloq + Tovuq🍗🧀", callback_data = "chicken++"),
		],
		[
			InlineKeyboardButton(text = "Fitter🥬", callback_data = "fitter"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back1")
		]
	]
)

####################mol gushtli lavash
Cow = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min1"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic1"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back2")
		]
	]
)

#mini gushtli
number = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back3")
		]
	]
)
#max gushtli
number2 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back4")
		]
	]
)

############################tovuq gusht
Chicken = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min2"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic2"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back5")
		]
	]	
)

#mini tovuq
number3 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back6")
		]
	]
)

#classic lavash
number4 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back7")
		]
	]
)

#################################qalampir goshtli
Qalampir = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min3"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic3"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back8")
		]
	]
)

#mini qalampir
number5 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back9")
		]
	]
)
#max  qalampir gushtli
number5 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back10")
		]
	]
)

#################################qalampir tovuq
Qalampir2 = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min4"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic4"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back11")
		]
	]
)

#mini qalampir tovuq
number7 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back12")
		]
	]
)
#max  qalampir tovuq
number8 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back13")
		]
	]
)

####################pishloqli gusht
Pishloq = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min5"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic5"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back14")
		]
	]
)

#mini qalampir tovuq
number9 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back15")
		]
	]
)
#max  qalampir tovuq
number10 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back16")
		]
	]
)

###################################pishloqli tovuq
Pishloq2 = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min6"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic6"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back17")
		]
	]
)

#mini qalampir tovuq
number11 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back18")
		]
	]
)
#max  qalampir tovuq
number12 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back19")
		]
	]
)

#############################Fitter
Fitter = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min7"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic7"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back20")
		]
	]
)

#mini fitter
number13 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back21")
		]
	]
)
#max  fitter
number14 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back22")
		]
	]
)

# ########################################  Hot-dog
Hotdog = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Hot-dog Baget Dabl", callback_data = "hotdog1"),
			InlineKeyboardButton(text = "Classic Hot-dog", callback_data = "cl_hotdog"),
		],
		[
			InlineKeyboardButton(text = "Karalevski", callback_data = "crown"),
			InlineKeyboardButton(text = "Tovuqli Hot-Dog", callback_data = "chickenhot"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back23")
		]
	]
)

################################## Double Hotdog
number15 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back24")
		]
	]
)

################################# Classic Hotdog
number16 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back25")
		]
	]
)

################################# Karalevski Hotdog
number17 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back26")
		]
	]
)

################################# Tovuqli Hotdog
number18 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back27")
		]
	]
)

# ########################################  Sandvich
Sandvich = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Classic Sandvich", callback_data = "clsandvich"),
			InlineKeyboardButton(text = "Tovuqli Sandvich", callback_data = "tvsandvich"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back28")
		]
	]
)

################################# Classic Hot dog
number19 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back29")
		]
	]
)

################################# Tovuqli Sandvich
number20 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back30")
		]
	]
)


# ########################################      Shaurma
Shaurma = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mol Goshtli🥩", callback_data = "cow2"),
			InlineKeyboardButton(text = "Tovuq Goshtli🥩", callback_data = "chicken2"),
		],
		[
			InlineKeyboardButton(text = "Mol Goshtli🥩 + Garimdori", callback_data = "cow3"),
			InlineKeyboardButton(text = "Tovuq Goshtli🥩 + Garimdori", callback_data = "chicken3"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back31")
		]
	]
)
############## Mol Goshtli Shaurma
Cow_shaurma = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min8"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic8"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back32")
		]
	]
)

#mini cow shaurma
number21 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back33")
		]
	]
)
#max cow  Shaurma
number22 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back34")
		]
	]
)

############## Tovuq Goshtli Shaurma
Chicken_shaurma = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min9"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic9"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back35")
		]
	]
)

#mini chicken shaurma
number23 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back36")
		]
	]
)
#max chicken Shaurma
number24 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back37")
		]
	]
)

##############  Goshtli Garimdori Shaurma
G_shaurma = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min10"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic10"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back38")
		]
	]
)

#mini cow +g shaurma
number25 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back39")
		]
	]
)
#max cow +g Shaurma
number26 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back40")
		]
	]
)


##############  Tovuqli Garimdori Shaurma
T_shaurma = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Mini", callback_data = "min11"),
			InlineKeyboardButton(text = "Classic", callback_data = "classic11"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back41")
		]
	]
)

#mini chicken +g shaurma
number27 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back42")
		]
	]
)
#max chicken +g Shaurma
number28 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back43")
		]
	]
)

############ Gamburgers
Hamburger = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Gamburger", callback_data = "gamburger"),
			InlineKeyboardButton(text = "Chizburger", callback_data = "chizburger"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back44")
		]
	]
)

################################# Gamburger
number29 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back45")
		]
	]
)

################################# Chizburger
number30 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back46")
		]
	]
)

######################### Donar
Donar = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Donar Go'shtlik", callback_data = "d_gosht"),
			InlineKeyboardButton(text = "Donar Tovuqlik", callback_data = "d_tovuq"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back47")
		]
	]
)

################################# donar gushtlik
number31 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back48")
		]
	]
)

################################# donar tovuqlik
number32 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back49")
		]
	]
)

############################ Gazak
Gazaklar = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Frie 150gr🍟", callback_data = "free"),
			InlineKeyboardButton(text = "Kartoshka derevenski🍟", callback_data = "free2"),
		],
		[
			InlineKeyboardButton(text = "Kichik Guruch", callback_data = "kicik_g"),
			InlineKeyboardButton(text = "Katta Guruch", callback_data = "katta_g"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back50")
		]
	]
)

################################# free 150gr
number33 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back51")
		]
	]
)

################################# derevenski free
number34 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back52")
		]
	]
)

################################# kicik guruch
number35 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back53")
		]
	]
)

################################# katta guruch
number36 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back54")
		]
	]
)

################################## IChimliklar 
Drinks = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Choy va Coffee☕️", callback_data = "teaandcofe"),
			InlineKeyboardButton(text = "Sovuq Ichimliklar", callback_data = "freshdrinks"),
		],
		[
			InlineKeyboardButton(text = "Tabiiy Soklar va Freshlar🥤", callback_data = "natural"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back55")
		]
	]
)

################# Cofe va choy 
Cofeandtea  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Coffee☕️", callback_data = "cofe"),
			InlineKeyboardButton(text = "Choylar🫖", callback_data = "tea"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back56")
		]
	]
)

######### Coffee
Coffee  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Americano☕️", callback_data = "cofe1"),
			InlineKeyboardButton(text = "Cappucino🧋", callback_data = "cofe2"),
		],
		[
			InlineKeyboardButton(text = "Coffee 3v1☕️", callback_data = "cofe3"),
			InlineKeyboardButton(text = "Latte🧋", callback_data = "cofe4"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back57")
		]
	]
)

Cofe1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back58")
		]
	]
)

Cofe2 = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Cappucino Small🧋", callback_data = "cap1"),
			InlineKeyboardButton(text = "Cappucino Big🧋", callback_data = "cap2"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back57")
		]
	]
)

Cap1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back66")
		]
	]
)

Cap2 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back67")
		]
	]
)

	


Cofe3 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back60")
		]
	]
)

Cofe4 = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Latte Small🧋", callback_data = "latte1"),
			InlineKeyboardButton(text = "Latte Big🧋", callback_data = "latte2"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back61")
		]
	]
)

Lat1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back69")
		]
	]
)

Lat2 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back70")
		]
	]
)
Tea = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Qora choy", callback_data = "tea1"),
			InlineKeyboardButton(text = "Ko'k choy", callback_data = "tea2"),
		],
		[
			InlineKeyboardButton(text = "Limon Choy", callback_data = "tea3"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back62")
		]
	]
)

Tea1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back63")
		]
	]
)

Tea2 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back64")
		]
	]
)

Tea3 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back65")
		]
	]
)


######### Sovuq ichimliklar
Freshdrinks  = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Coca Cola 0.5", callback_data = "cola"),
			InlineKeyboardButton(text = "Fanta 0.5", callback_data = "fanta"),
		],
		[
			InlineKeyboardButton(text = "Sprite 0.5", callback_data = "sprite"),
			InlineKeyboardButton(text = "Pepsi 0.5", callback_data = "pepsi"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back71")
		]
	]
)

######## Cola
Cola = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back72")
		]
	]
)

#########fANTA
Fanta = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back73")
		]
	]
) 

#########Sprite
Sprite = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back74")
		]
	]
) 

######### Pepsi
Pepsi = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back75")
		]
	]
) 

############ natural drinks
Natural = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Bliss 1L", callback_data = "bliss"),
			InlineKeyboardButton(text = "Olma va sabzi fresh", callback_data = "fresh"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back76")
		]
	]
) 

######### bliss
Bliss = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back77")
		]
	]
)

######### 
Apple = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back78")
		]
	]
)

######################## Desert
Sweets = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Assalim", callback_data = "asal"),
			InlineKeyboardButton(text = "Choco", callback_data = "choco"),
		],
		[
			InlineKeyboardButton(text = "Qulupnay", callback_data = "qulupnay"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back79")
		]
	]
)

######### assalim
Asal = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back80")
		]
	]
)

##############Choco
Choco = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back81")
		]
	]
)

#qulupnay
Qulupnay = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back82")
		]
	]
)

##############pizza
Pizza = InlineKeyboardMarkup(
	inline_keyboard= [
		[
			InlineKeyboardButton(text = "Peperonni", callback_data = "pep"),
			InlineKeyboardButton(text = "Margaritta", callback_data = "mar"),
		],
		[
			InlineKeyboardButton(text = "Ananaslik", callback_data = "ananas"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back83")
		]
	]
)

#
###### peperonni
Peperonni = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back84")
		]
	]
)

######## Margaritta
Margaritta = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back85")
		]
	]
)

###### ananaslik
Ananas = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "1️⃣", callback_data = "one"),
			InlineKeyboardButton(text = "2️⃣", callback_data = "two"),
			InlineKeyboardButton(text = "3️⃣", callback_data = "three"),
		],
		[
			InlineKeyboardButton(text = "4️⃣", callback_data = "four"),
			InlineKeyboardButton(text = "5️⃣", callback_data = "five"),
			InlineKeyboardButton(text = "6️⃣", callback_data = "six"),
		],
		[
			InlineKeyboardButton(text = "7️⃣", callback_data = "seven"),
			InlineKeyboardButton(text = "8️⃣", callback_data = "eight"),
			InlineKeyboardButton(text = "9️⃣", callback_data = "nine"),
		],
		[
			InlineKeyboardButton(text = "🔙Back", callback_data = "back86")
		]
	]
)









# mainmenu = InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		InlineKeyboardButton(text = "🇺🇿 O'zbekcha", callback_data = "uz"),
# 		InlineKeyboardButton(text = "🇺🇸 English", callback_data = "en")
# 		],
# 	],
# )
# language = ReplyKeyboardMarkup(
# 	keyboard = [
# 		[
# 		KeyboardButton(text = "🇺🇿 O'zbekcha"),
# 		KeyboardButton(text = "🇺🇸 English")
# 		],
# 	],
# 	resize_keyboard = True
# )
# m2 = InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		InlineKeyboardButton(text = "Kurs haqida informatsiya", callback_data = "ku")
# 		],
# 	],
# )

# m3 = InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		 InlineKeyboardButton(text = "Information about course", callback_data = "co")
# 		],
# 	],
# )

# k2 =InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		InlineKeyboardButton(text = "IT", callback_data = "it"),
# 		InlineKeyboardButton(text = "SMM", callback_data = "smm")
# 		],
# 	],
# ) 

# k3 =InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		InlineKeyboardButton(text = "IT", callback_data = "it"),
# 		InlineKeyboardButton(text = "SMM", callback_data = "smm")
# 		],
# 	],
# ) 



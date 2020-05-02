import requests
from bs4 import BeautifulSoup
import telebot
import random
import lxml.etree
from telebot import types
import wikipedia

wikipedia.set_lang('ru')

bot = telebot.TeleBot('1144899408:AAHs9EuMWSCJE_TnCytKPrYtl40fHPfMv54')
game_dict=[]
def parse(search):
    #search=input("Введите понятие:   ")
    URL=f"https://ru.wikipedia.org/wiki/{search}"
    HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    response=requests.get(URL, headers=HEADERS)
    soup=BeautifulSoup(response.content,'html.parser')
    items=soup.find_all('p',limit=1)
    if items==[]:
        vars=soup.body('li',limit=10)
        return [(vars[0]).get_text(),URL]
    else: 
        doc=items[0]
        k=doc.get_text()
        return [k,URL]
    

  
@bot.message_handler(commands=['start','help'])
def start_message(message):
    bot.send_message(message.chat.id, """\
Привет, я много всего знаю, так что напиши мне какой-нибудь термин, а я его расскажу!\
    """)

@bot.message_handler(content_types=['text'])
def term(message):
    try:

        pag=wikipedia.page(message.text)
        pag.images

        a=(parse(message.text))
        words=a[0]
        if a[0]=="Состояниеотпатрулирована":
            bot.send_message(message.chat.id,"Либо Википедия не знает этого, либо это многозначный термин, пока что я такое обработать не могу(")
        #else:
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Открыть статью полностью", url=a[1])
        im_button = types.InlineKeyboardButton(text="Отправить картинку", callback_data=message.text)
        add_button=types.InlineKeyboardButton(text="Добавить в подборку", callback_data=f"d{message.text}")
        show_button=types.InlineKeyboardButton(text="Показать подборку",callback_data="show")
        keyboard.add(url_button)
        keyboard.add(im_button)
        keyboard.add(add_button)
        keyboard.add(show_button)
        bot.send_message(message.chat.id, words, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, "Либо Википедия не знает этого, либо это многозначный термин, пока что я такое обработать не могу(")
@bot.callback_query_handler(func=lambda call: call.data=="show")
def show(call):
    for i in game_dict:
       bot.send_message(call.message.chat.id, f'{i}')
     #bot.send_message(call.message.chat.id,f'{game_dict}')
        
@bot.callback_query_handler(func=lambda query: (query.data).startswith('d'))
def game_d(query):
    w=(query.data)[1:]
    ww=parse(w)
    #game_dict.update({query.data:query.data})
    game_dict.append(ww[0])
    game_dict.append('🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓')
    bot.send_message(query.message.chat.id,"Элемент добавлен")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    try:
        pag=wikipedia.page(call.data)
        image_url=pag.images[4]
        if image_url[-3:]=="jpg":
            bot.send_photo(call.message.chat.id, image_url)
        else: bot.send_message(call.message.chat.id,"К данной статье фото не прилагается:(")
        bot.answer_callback_query(callback_query_id=call.id, text='')
    except:
        bot.send_message(call.message.chat.id,"Что-то пошло не так:((((")




bot.polling()

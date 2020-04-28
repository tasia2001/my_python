import requests
from bs4 import BeautifulSoup
import telebot
import random
import lxml.etree
from telebot import types

#бот пока ничего не умеет, кроме приветствовать, повторять отправленный текст и реагировать на отправленную фотографию
answers=["То, что находится на этой картинке, похоже на моего кота", "Красота!!!!!", "Был бы у меня инстаграм, я бы поставил лайк два раза", "Картинка огонь, качество не очень", "Не вызывай у меня зависть такими шедеврами"]

bot = telebot.TeleBot('*****')

c=[]

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

@bot.message_handlers(commands=["game"])
def game():

    bot.send_message

@bot.message_handler(content_types=['text'])
def term(message):
    a=(parse(message.text))
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Открыть статью полностью", url=a[1])
    game_button=types.InlineKeyboardButton(text="Начать игру", callback_game=)
    keyboard.add(url_button)
    keyboard.add(game_button)
    #bot.send_message(message.chat.id,"", reply_markup=keyboard)
    bot.send_message(message.chat.id, a[0], reply_markup=keyboard)

@bot.message_handler(content_types=['photo'])
def ph(message):
    bot.send_message(message.chat.id, random.choice(answers))


bot.polling()

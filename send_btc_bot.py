import requests
import telebot
from auth_data_bot import token
import datetime
from telebot import types


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'hello')

        																																				bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
   

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                data = datetime.datetime.now()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    '{}\nSell BTC price:{}'.format(sell_price,data)
                    
                    # \nSell BTC price: {sell_price}"

# f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n


                    # bot.send_message(message.chat.id, "Температура в {}: {} C".format(city, temp))
                    # bot.send_message(message.chat.id, 'Температура в ', city, ': ',temp , '°C')
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'wrong'
                )


    bot.polling()





if __name__=="__main__":
    telegram_bot(token)
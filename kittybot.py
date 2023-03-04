from telegram import Bot
from telegram.ext import Updater, Filters, MessageHandler

TOKEN = '5770436977:AAFLGEP9Ob48JnZ_KEt4_R63QTpzlJEjvNg'
CHAT_DESKTOP = '789047106'
CHAT_PHONE = '5416117742'

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

# chat_id = CHAT_DESKTOP


def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение
    # будет отправлено 'Привет, я KittyBot!'
    print(update.message['text'])
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))


# Метод start_polling() запускает процесс polling,
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle()

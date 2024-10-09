import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=20, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
    try:
        fulltime = parse(text)
        message_id = bot.send_message(chat_id, 'Запускаю таймер')
        bot.create_countdown(
            fulltime, timer, chat_id=chat_id, message_id=message_id, fulltime=fulltime)

    except(TypeError):
        bot.update_message(chat_id, message_id, 'Неверный формат времени')


def timer(secs_left, chat_id, message_id, fulltime):
    progress = fulltime - secs_left
    progressbar = render_progressbar(
        fulltime, progress, prefix='', suffix='', length=20, fill='█', zfill='░')
    if secs_left > 0:
        bot.update_message(chat_id, message_id,
                           f'Осталось {secs_left} секунд!\n{progressbar}')
    else:
        bot.update_message(chat_id, message_id,
                           f'Осталось {secs_left} секунд!\n{progressbar}')
        bot.send_message(chat_id, 'Время вышло!')


def main():
    global bot
    load_dotenv('LoginData.env')
    tg_token = os.getenv('tg_token')
    chat_id = os.getenv('tg_chat_id')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == '__main__':
    main()


























import psutil
import telebot
import asyncio
import datetime

# Токен вашего бота в Telegram
TOKEN = "YOUR_BOT_TOKEN"
# ID чата или пользователя, которому будет отправляться статистика
CHAT_ID = "CHAT_ID"

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки статуса
def send_status():
    # Получаем данные о процессоре
    cpu_percent = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq()
    cpu_info = f"💻 Процессор: {cpu_percent}% загрузки ({cpu_freq.current:.2f} GHz / {cpu_freq.max:.2f} GHz)"

    # Получаем данные о памяти
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_total = f"{memory.total // (1024 ** 2)} МБ"
    memory_used = f"{memory.used // (1024 ** 2)} МБ"
    memory_free = f"{memory.free // (1024 ** 2)} МБ"
    memory_info = f"🧠 ОЗУ: {memory_percent}% использовано ({memory_used} / {memory_total}) свободно {memory_free}"

    # Получаем данные о жестком диске
    disk_usage = psutil.disk_usage("/")
    disk_percent = disk_usage.percent
    disk_total = f"{disk_usage.total // (1024 ** 3)} ГБ"
    disk_used = f"{disk_usage.used // (1024 ** 3)} ГБ"
    disk_free = f"{disk_usage.free // (1024 ** 3)} ГБ"
    disk_info = f"💽 Жесткий диск: {disk_percent}% использовано ({disk_used} / {disk_total}) свободно {disk_free}"

    # Получаем время последнего обновления
    last_update = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    # Собираем сообщение со всей статистикой
    message = f"🖥️ Статус системы 🖥️\n\n" \
              f"{memory_info}\n" \
              f"{disk_info}\n" \
              f"{cpu_info}\n" \
              f"🕒 Время последнего обновления: {last_update}"

    # Отправляем сообщение в Telegram
    bot.send_message(chat_id=CHAT_ID, text=message)

# Бесконечный цикл отправки статуса
async def main():
    while True:
        # Отправляем статус и ждем 5 минут
        send_status()
        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(main())

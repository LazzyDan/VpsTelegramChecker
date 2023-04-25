# Этот бот отправляет вам каждые 5 минут статус о вашем VPS в ваши личные сообщения.

# Давайте приступим!

- Для установки этого скрипта потребуются следующие команды:

- Для установки Python 3.6 в ОС семейства Ubuntu, в терминале необходимо выполнить следующие команды:

# Установка зависимостей:

- sudo apt-get update

- sudo apt-get install build-essential checkinstall

- sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \ libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
    
# Загрузка архива с исходным кодом Python 3.6 с официального сайта:

- wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz

# Распаковка архива:

- tar -xvf Python-3.6.0.tgz

# Переход в директорию с распакованным исходным кодом:

- cd Python-3.6.0

# Конфигурация исходного кода перед компиляцией:

- ./configure

# Компиляция и установка Python 3.6:

- make
- sudo make install

# После этого Python 3.6 будет установлен на вашей ОС.

# Установка библиотек psutil и telebot:

- pip install psutil
- pip install pyTelegramBotAPI

# Запустить скрипт с помощью Python 3:

- python3 script.py

При запуске скрипта в консоли не должно быть ошибок, и после этого он будет отправлять статистику системы каждые 5 минут в указанный чат в Telegram. Обратите внимание, что для этого вам потребуется указать токен вашего бота в Telegram и ID чата или пользователя, которому будет отправляться статистика, в переменных TOKEN и CHAT_ID соответственно.

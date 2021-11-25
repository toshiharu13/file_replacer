# Python скрипт file_replacer
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

Скрипт предназначен для замены  файла на группе компьютеров. 

## Техническое описание
Скрипт запускается на Linux компьютере, маунтится по списку к удаленным WIN компьютерам, проделывает описанные операции.

## Системные требования
- [Python 3](https://www.python.org/)
- Linux OS

##  Установка
Для установки дастоточно:

Cклонировать проект

    $ git clone https://github.com/toshiharu13/file_replacer.git

Установить requirements.txt

      $ pip install -r requirements.txt

### Создание файла переменного окружения

 - FILE_DESTINATION=<путь, куда будет произведено копирование с учетом маунта>
 - MOUNT_DESTINATION=<путь к папке монтировния>
 - USER=<имя пользователя>
 - PASSWORD=<пароль>

## Запуск
Файл для замены должен лежать в папке <copy_file>, перед первым стартом  папку надо создать, или просто запустить скрипт, папка автоматически появится.


Для запуска, из паки проекта в терминале:

      python3 bat_replace.py

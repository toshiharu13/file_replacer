#!/usr/bin/env python3
import logging
import os
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s; %(levelname)s; %(name)s; %(message)s',
    filename='logs.log',
    filemode='w',
)


def copy(batsourse, batdeest):
    """
    Копируем файлы
    """
    try:
        shutil.copy(batsourse, batdest)
        print(f'Успешно скопировано из {batsourse} на {arm}')
    except FileNotFoundError:
        print('Замена не произведена, что то пошло не так')


def mount(arm, user, passwd):
    """
    Монтируем АРМ по шаре C$
    """
    os.system(f'sudo -S mount -t cifs //{arm}/c$ /home/boyko-ab/mnt/logs2/ '
              f'--verbose -o user={user},password={passwd}')


def unmount(arm):
    """
    Размонтируем
    """
    os.system('sudo -S umount /home/boyko-ab/mnt/logs2/')
    print(f'Отключаемся от {arm}')


if __name__ == '__main__':
    batsourse = 'Settings.xml'
    batdest = '/mnt/logs2/procdump/Settings.xml'
    arm = ''
    user = input('введите имя пользователя ')
    passwd = input('введите пароль ')

    with open('listarm.txt', 'r') as infile:
        for line in infile:
            arm = line.strip()
            mount(arm, user, passwd)
            copy(batsourse, batdest)
            unmount(arm)

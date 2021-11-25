#!/usr/bin/env python3
import logging
import os
import shutil
from pathlib import Path

from environs import Env


def copy(file_source, file_dest):
    """
    Копируем файлы
    """
    try:
        shutil.copy(file_source, file_dest)
        print(f'Успешно скопировано из {file_source} на {arm}')
    except BaseException as ex:
        print(f'Замена не произведена {ex}')
        return ex


def mount(arm, user, passwd, mount_dest):
    """
    Монтируем АРМ по шаре C$
    """
    try:
        os.system(f'sudo -S mount -t cifs //{arm}/c$ {mount_dest} '
                  f'--verbose -o user={user},password={passwd}')
    except BaseException as ex:
        print(f'монтирование к {mount_dest} не произведено,'
              f'ошибка: {ex}')
        return ex




def unmount(arm, mount_dest):
    """
    Размонтируем
    """
    try:
        os.system(f'sudo -S umount {mount_dest}')
        print(f'Отключаемся от {arm}')
    except BaseException as ex:
        print(f'Размантирование не удалось: {ex}')
        return ex


if __name__ == '__main__':
    env = Env()
    env.read_env()

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s; %(levelname)s; %(name)s; %(message)s',
        filename='logs.log',
        filemode='w',
    )

    copy_folder = Path.cwd() / 'copy_folder'
    Path(copy_folder).mkdir(parents=True, exist_ok=True)
    file_source = os.listdir(copy_folder)
    if not file_source:
        logging.info(f'Не обноружено файла в папке {copy_folder}, отключаемся')
        raise SystemExit(1)
    file_source = Path(copy_folder/os.listdir(copy_folder)[0])
    file_dest = env.str('FILE_DESTINATION')
    mount_dest = env.str('MOUNT_DESTINATION')
    user = env.str('USER')
    passwd = env.str('PASSWORD')

    with open('listarms.txt', 'r') as arms:
        for arm in arms:
            arm = arm.strip()
            mount_result = mount(arm, user, passwd, mount_dest)
            if mount_result:
                logging.info(
                    f'подключение к {mount_dest}, не удалось:{mount_result}'
                    f' отключаемся')
                continue
            copy_result = copy(file_source, file_dest)
            if copy_result:
                logging.info(
                    f'копирование в {file_source}, не удалось:{copy_result}'
                )
            unmount_result = unmount(arm, mount_dest)
            if unmount_result:
                logging.info(f'Размантирование не удалось на {arm},'
                             f' причина: {unmount_result}')

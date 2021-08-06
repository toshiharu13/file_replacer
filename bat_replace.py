#!/usr/bin/env python3

import os
import shutil

def copy(batsourse,batdeest):
    try:
        shutil.copy(batsourse, batdest)
        print(f'Успешно скопировано из {batsourse} на {ARM}')
    except FileNotFoundError:
        print('Замена не произведена, что то пошло не так')

def mount(ARM):
    os.system(f'sudo -S mount -t cifs //{ARM}c$ /home/boyko-ab/mnt/logs2/ --verbose -o user={user},password={PASS}')
    print(f'подключились к {ARM}')

def unmount(ARM):
    os.system('sudo -S umount /home/boyko-ab/mnt/logs2/')
    print(f'Отключаемся от {ARM}')


batsourse = 'Settings.xml'
batdest = '/mnt/logs2/procdump/coredump.bat'
ARM = ''
user = input('введите имя пользователя ')
PASS = input('введите пароль ')

with open('listarm.txt', 'r') as infile:
    for line in infile:
       ARM = line.strip()
       mount(ARM)
       #copy(batsourse,batdest)
       #unmount(ARM)

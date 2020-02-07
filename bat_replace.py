#!/usr/bin/env python3

import os
import shutil

def copy(batsourse,batdeest):
    try:
        shutil.copy(batsourse, batdest)
        print('Успешно скопировано из ', batsourse, ' на ', ARM)
    except FileNotFoundError:
        print('Замена не произведена, нет программы мониторинга')

def mount(ARM):
    os.system('mount -t cifs //'+ ARM + '/c$ /mnt/logs2/ --verbose -o user=vpn,password='+ PASS + '')
    print('подключились к ', ARM)

def unmount():
    os.system('umount /mnt/logs2')
    print('Отключаемся от', ARM)


batsourse = '/mnt/myfolder/temp/coredump.bat'
batdest = '/mnt/logs2/procdump/coredump.bat'
ARM = ''
PASS = ''

with open('/home/boyko-ab/Документы/python/batreplace/listarm.txt', 'r') as infile:
    for line in infile:
       ARM = line.strip()
       mount(ARM)
       copy(batsourse,batdest)
       unmount()

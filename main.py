# -*- coding: utf-8 -*-

import threading
import asyncio
import config
import dev_ice
from asyncio import sleep
import time

#
config.light_active = True
lock=threading.Lock()

def drag_doorbeetwin():
    if dev_ice.door2_isop():
        dev_ice.door2_close()
    else:
        dev_ice.door2_open()


def prepare():
    config.prepare=True
    config.step=17



def autodial_loop():
    config.ring_trig = True
    while not config.autodial_ready:
        sleep(1)
        print('1')
    while config.autodial_ready:
        print('2')
        sleep(1)
    config.autodial_sended=False
def autodial():
    autd= threading.Thread(target=autodial_loop)
    autd.start()

def power_off():
    config.phone_on_flag=False
    dev_ice.door2_close()
    dev_ice.lamp2_Off()
    dev_ice.lamp2_table_Off()
    dev_ice.lamp1_Off()
    dev_ice.lamp1_table_Off()
    config.go = False
    time.sleep(1)
    dev_ice.power_off()


def power_on():
    dev_ice.power_on()
    time.sleep(1)
    if config.pwr_on_flag:
        go_stream = threading.Thread(target=go_thread, daemon=True)
        go_stream.start()
        config.go = True
def stop():
    config.step=-2
    dev_ice.door2_close()


async def scene():
    print("основной цикл")

    while config.go:
        await sleep(0)
        print("Вход выполнен")
        #config.Idle=False
        print (str(config.step) + 'Шаг')
#################################################################step 0
        await sleep(0)
        if config.step == 0 and config.go == True:
            config.phone_on_flag = True
            dev_ice.phone_on()
            dev_ice.lamp2_table_Off()
            dev_ice.lamp1_Off()
            dev_ice.lamp1_table_Off()
            dev_ice.lamp2_Off()
            config.current_step_label.append('Выполняется шаг 0 ... - Завести игроков в комнаты\n Вручную перейдите к шагу 1')
            while config.step == 0 and config.go == True:
                await sleep(0)
        await sleep(0)
#################################################################step 1
        await sleep(0)
        if config.step == 1 and config.go == True:
            dev_ice.door1_turn()
            config.phone_on_flag = True
            dev_ice.phone_on()

            config.current_step_label.append('Выполняется шаг 1 ... - Поднять трубку')
            await sleep(2)
            dev_ice.lamp2_On()
            await sleep(2)
            dev_ice.lamp1_bright(30)
            dev_ice.lamp2_table_On()
            await sleep(5)
            while config.step == 1 and config.go == True:
                config.ring_trig = True
                await sleep(0.1)
                if config.autodial_ready:
                    config.step += 1
                    await sleep(2)
            dev_ice.lamp1_bright(0)
            config.switch2_add = True
            config.light_active= True
            await sleep(0.5)
            config.switch2_add=True
            config.current_step_label.append('Выполняется шаг 1 - Поднять трубку - Завершено')
        await sleep(0)
#################################################################step 2
        await sleep(0)
        if config.step == 2 and config.go == True:
            print('step2 ')
            config.current_step_label.append('Выполняется шаг 2 ... - Установить предмет на стол 2')
            while config.step == 2 and config.go == True:
                print('step2 into')
                await sleep(config.scene_rate)
                if dev_ice.check_rfid_table2():
                    config.current_step_label.append('Предмет на стол 2 установлен')
                    config.step+=1
        await sleep(0)
#################################################################step 3
        await sleep(0)
        if config.step == 3 and config.go == True:
            config.current_step_label.append('Выполняется шаг 3 ... - Открыть верхнюю дверь шкафа 1')
            while config.step == 3 and config.go == True:
                for x in range(0,config.MAGNET_TRIES):
                    dev_ice.Shave1_top_door_open()
                    await sleep(config.MAGNET_PAUSE)
                    dev_ice.Shave1_top_door_close()
                    await sleep(config.MAGNET_PAUSE)
                    if config.step !=3:
                        break
                if config.step != 3:
                    break
                if config.manual_door:
                    continue
                config.step+=1
            config.current_step_label.append('Выполняется шаг 3 - Открыть верхнюю дверь шкафа 1 - Завершено ')
        await sleep(0)
#################################################################step 4
        await sleep(0)
        if config.step == 4 and config.go == True:
            config.current_step_label.append('Выполняется шаг 4 ... - Установить предмет на стол 1')
            while config.step == 4 and config.go == True:
                await sleep(config.scene_rate)
                if dev_ice.check_rfid_table_1():
                    config.current_step_label.append('Предмет на стол 1 установлен')
                    config.step += 1
        await sleep(0)
#################################################################step 5
        await sleep(0)
        if config.step == 5 and config.go == True:
            config.current_step_label.append('Выполняется шаг 5 ... - Открыть верхнюю дверь шкафа 2')
            while config.step == 5 and config.go == True:
                for x in range(0,config.MAGNET_TRIES):
                    dev_ice.Shave2_top_door_open()
                    await sleep(config.MAGNET_PAUSE)
                    dev_ice.Shave2_top_door_close()
                    await sleep(config.MAGNET_PAUSE)
                    if config.step != 5:
                        break
                if config.step != 5:
                    break
                if config.manual_door:
                    continue
                config.step += 1
            config.current_step_label.append('Выполняется шаг 5 - Открыть верхнюю дверь шкафа 2 - Завершено ')

        await sleep(0)
#################################################################step 6
        await sleep(0)
        if config.step == 6 and config.go == True:
            config.current_step_label.append('Выполняется шаг 6 ... - Поставить книгу на шкаф 2')
            while config.step == 6 and config.go == True:
                await sleep(config.scene_rate)
                if dev_ice.check_rfid_shave_2():
                    config.current_step_label.append('Книга на шкаф 2 установлена')
                    config.step += 1
        await sleep(0)
#################################################################step 7
        await sleep(0)
        if config.step == 7 and config.go == True:
            config.current_step_label.append('Выполняется шаг 7 ... - Открыть дверь в столе 1')
            while config.step == 7 and config.go == True:
                for x in range(0, config.MAGNET_TRIES):
                    dev_ice.table1_door_open()
                    await sleep(config.MAGNET_PAUSE)
                    dev_ice.table1_door_close()
                    await sleep(config.MAGNET_PAUSE)
                    if config.step != 7:
                        break
                if config.step != 7:
                    break
                if config.manual_door:
                    continue
                config.step += 1
            config.current_step_label.append('Выполняется шаг 7 - Открыть дверь в столе 1 - Завершено ')

        await sleep(0)
#################################################################step 8
        await sleep(0)
        if config.step == 8 and config.go == True:
            config.current_step_label.append('Выполняется шаг 8 ... - Поставить предмет в шкаф 1')
            while config.step == 8 and config.go == True:
                await sleep(config.scene_rate)
                if dev_ice.check_rfid_shave_1():
                    config.current_step_label.append('Предмет в шкаф 1 установлен')
                    config.step += 1
        await sleep(0)
#################################################################step 9
        await sleep(0)
        if config.step == 9 and config.go == True:
            config.phone_on_flag = False
            config.current_step_label.append('Выполняется шаг 9 ... - Открыть нижние двери в обоих шкафах\nТелефоны отключены ')
            while config.step == 9 and config.go == True:
                for x in range(0, config.MAGNET_TRIES):
                    dev_ice.Shave1_bottom_door_open()
                    dev_ice.Shave2_bottom_door_open()
                    await sleep(config.MAGNET_PAUSE)
                    dev_ice.Shave1_bottom_door_close()
                    dev_ice.Shave2_bottom_door_close()
                    await sleep(config.MAGNET_PAUSE)
                    if config.step != 9:
                        break
                if config.step != 9:
                    config.phone_on_flag = True
                    config.current_step_label.append('Прервано, Телефоны включены')
                    break

                if config.manual_door:
                    continue
                config.step += 1
                config.current_step_label.append('Выполняется шаг 9 - Открыть нижние двери в обоих шкафах - Завершено \nТелефоны отключены')
                config.phone_on_flag = False

        await sleep(0)
#################################################################step 10
        await sleep(0)
        if config.step == 10 and config.go == True:
            config.current_step_label.append('Выполняется шаг 10 ... - Кнопки в чумаданах')
            while config.step == 10 and config.go == True:
               await sleep(0)
               if await dev_ice.case_checker():
                   await sleep(0)
                   dev_ice.door2_open()
                   config.step=11
                   config.current_step_label.append('Кнопки в чумаданах были нажаты. Двери между комнатами открыты')
            config.current_step_label.append('Выполняется шаг 10 - Кнопки в чумаданах - Завершено')
        await sleep(0)
#################################################################step 11
        await sleep(0)
        if config.step == 11 and config.go == True:

            config.current_step_label.append('Выполняется шаг 11 ... - Повесить любую из картин на место')
            while config.step == 11 and config.go == True:
                await sleep(config.scene_rate)
                if dev_ice.check_rfid_wall1()==True or dev_ice.check_rfid_wall2()==True:
                    config.current_step_label.append('Одна из картин на месте')
                    config.step+=1
                    dev_ice.door2_close()
        await sleep(0)
#################################################################step 12
        await sleep(0)
        if config.step == 12 and config.go == True:
            config.current_step_label.append('Выполняется шаг 12 ... - Опускание завесы ')
            dev_ice.tape_drag()
            config.current_step_label.append('Выполняется шаг 12 - Завеса снята')
            config.step += 1
        await sleep(0)
#################################################################step 13
        await sleep(0)
        if config.step == 13 and config.go == True:
            config.current_step_label.append('Выполняется шаг 13 ... - Повесить еще одну картину на место')
            while config.step == 13 and config.go == True:
                await sleep(config.scene_rate)
                if dev_ice.check_rfid_wall1()==True and dev_ice.check_rfid_wall2()==True:
                    config.current_step_label.append('Картина на месте')
                    config.step+=1
        await sleep(0)
#################################################################step 14
        await sleep(0)
        if config.step == 14 and config.go == True:
            config.current_step_label.append('Выполняется шаг 14 ... - Ввести код')
            dev_ice.lock_clock_on()
            code='none'
            dev_ice.lamp1_bright(100)
            while config.step == 14 and config.go == True:
                await sleep(config.scene_rate)
                code = dev_ice.lock_clock_check()
                if code == 'proper':
                    dev_ice.lock_clock_off()
                    config.step = 16
                    config.current_step_label.append('Правильный код ')
                    break
                if code == 'fail':
                    dev_ice.lock_clock_off()
                    config.current_step_label.append('Неправильный код ')
                    config.step = 15
                    break
            dev_ice.lock_clock_off()
        await sleep(0)
#################################################################step 15
        await sleep(0.2)
        if config.step == 15 and config.go == True:
            config.current_step_label.append('Выполняется шаг 15 ... - УДАР!!!')
            dev_ice.window_drag()
            config.step=14
        await sleep(0.1)
#################################################################step 16
        await sleep(0.2)
        if config.step == 16 and config.go == True:
            await sleep(0.2)
            dev_ice.door1_turn()
            dev_ice.lamp1_speed(100)
            dev_ice.lamp1_bright(100)
            dev_ice.lamp1_table_On()
            dev_ice.lamp2_table_On()
            dev_ice.lamp2_On()
            dev_ice.lamp1_table_On()
            for x in range(0, 4):
                dev_ice.lamp1_table_On()
                await sleep(0.1)
                dev_ice.lamp1_table_Off()
                await sleep(0.2)
            config.current_step_label.append('Сценарий завершился! \nВыведите игроков.')
            config.step = -2
################################################################# prepare
        await sleep(0)
        if config.step == 17 and config.go == True:
            config.current_step_label.append('Выполняется подготовка')
            dev_ice.lamp1_On()
            dev_ice.lamp1_table_On()
            dev_ice.lamp2_On()
            dev_ice.lamp2_table_On()
            while config.step == 17 and config.go == True:
                for x in range(0,config.MAGNET_prepare_TRIES):
                    dev_ice.Shave1_top_door_open()
                    dev_ice.Shave1_bottom_door_open()
                    dev_ice.Shave2_bottom_door_open()
                    dev_ice.Shave2_top_door_open()
                    dev_ice.table1_door_open()
                    await sleep(config.MAGNET_PAUSE)
                    dev_ice.Shave1_top_door_close()
                    dev_ice.Shave1_bottom_door_close()
                    dev_ice.Shave2_bottom_door_close()
                    dev_ice.Shave2_top_door_close()
                    dev_ice.table1_door_close()
                    await sleep(config.MAGNET_PAUSE)
                    if config.step !=17:
                        break
                if config.step != 17:
                    break
                if config.manual_door:
                    continue
                config.step=-2
                config.prepare=False
            config.current_step_label.append('Подготовка завершена ')
        await sleep(0)

async def other():
     dev_ice.start()
     while config.go:
        dev_ice.check_ligt_switch()
        dev_ice.phone_checker()
        config.door_between_is_open = dev_ice.door2_isop()
        await sleep(0.02)
     print('Свет и телефон потоки завершились')

def go_thread():
    print('Поток сценария стартовал')
    ioloop_start = asyncio.new_event_loop()
    asyncio.set_event_loop(ioloop_start)
    tasks = [other(),scene()]
    ioloop_start.run_until_complete(asyncio.wait(tasks))
    ioloop_start.close()
    print('Поток сценария завершился')


def go_func():
    config.light_active = True
    config.step = 0
    print('3456546869780789078907890780')

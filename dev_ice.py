# -*- coding: utf-8 -*-
import config
import mod_bus
import asyncio
from time import sleep
####################################
#### Defines #######################
####################################
def start():
    config.switch1status = mod_bus.Read_Registers(23, 8, 1)[0]
    config.switch2status = mod_bus.Read_Registers(23, 7, 1)[0]
    config.switch1_add = False
    config.switch2_add = True
    sleep(0.2)


def power_on():
    try:
        config.Idle=True
        if mod_bus.open_port():
            mod_bus.Write_Register(22, 2, 1)
            config.pwr_on_flag = True
            config.messages_label.append('!Связь с основным контроллером установлена!')
    except ReferenceError:
        config.allert_messages_label.append(
            '!Проверьте соединение переходника с шиной.\n Убедитесь что питание системы включено.')
        config.pwr_on_flag = False


def power_off():
    mod_bus.Write_Register(22, 2, 0)
    config.pwr_on_flag = False
    config.messages_label.append('Питание системы выключено')

    del mod_bus.master
    config.messages_label.append('Порт закрыт!')


####################################
#### RFIDS #######################
####################################
def check_rfid_shave_1():
    try:
        if mod_bus.Read_Registers(slave_addr=6, start_reg=0, num_of_regg=14) == config.RFID6_ID:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с RFID шкаф 1')


def check_rfid_shave_2():
    try:
        if mod_bus.Read_Registers(slave_addr=2, start_reg=0, num_of_regg=14) == config.RFID2_ID:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с RFID шкаф 2')


def check_rfid_table_1():
    try:
        if mod_bus.Read_Registers(slave_addr=5, start_reg=0, num_of_regg=14) == config.RFID5_ID:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с RFID стол 1')


def check_rfid_table2():
    try:
        if mod_bus.Read_Registers(slave_addr=1, start_reg=0, num_of_regg=14) == config.RFID1_ID:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с RFID стол 2')


def check_rfid_wall1():
    try:
        if mod_bus.Read_Registers(slave_addr=3, start_reg=0, num_of_regg=14) == config.RFID3_ID:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с RFID стена 1')


def check_rfid_wall2():
    try:
        if mod_bus.Read_Registers(slave_addr=4, start_reg=0, num_of_regg=14) == config.RFID4_ID:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с RFID стена2')


####################################
#### LAMPS ###########################
####################################
def lamp1_bright(br=0):
    try:
        mod_bus.Write_Register(10, 1, br)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с димером')


def lamp1_speed(speed=0):
    try:
        mod_bus.Write_Register(10, 0, speed)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с димером')


def lamp1_Off():
    try:

        mod_bus.Write_Register(10, 1, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с димером')


def lamp1_On():
    try:
        mod_bus.Write_Register(10, 1, 100)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с димером')


def lamp2_Off():
    try:
        mod_bus.Write_Register(23, 2, 0)
    except ReferenceError:
        config.allert_messages_label.append('контроллером остальных ламп')


def lamp2_On():
    try:
        mod_bus.Write_Register(23, 2, 1)
    except ReferenceError:
        config.allert_messages_label.append('контроллером остальных ламп')


def lamp1_table_On():
    try:
        mod_bus.Write_Register(23, 3, 1)
    except ReferenceError:
        config.allert_messages_label.append('контроллером остальных ламп')


def lamp1_table_Off():
    try:
        mod_bus.Write_Register(23, 3, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером остальных ламп')


def lamp2_table_On():
    try:
        mod_bus.Write_Register(23, 1, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером остальных ламп')


def lamp2_table_Off():
    try:
        mod_bus.Write_Register(23, 1, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером остальных ламп')


####################################
#### SHAVES #####       TABLE 1 DOOR
####################################
def Shave2_top_door_open():
    try:
        mod_bus.Write_Register(26, 2, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 2')


def Shave2_top_door_close():
    try:
        mod_bus.Write_Register(26, 2, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 2')


def Shave2_bottom_door_open():
    try:
        mod_bus.Write_Register(26, 1, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 2')


def Shave2_bottom_door_close():
    try:
        mod_bus.Write_Register(26, 1, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 2')


####################################
def Shave1_top_door_open():
    try:
        mod_bus.Write_Register(25, 2, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 1')


def Shave1_top_door_close():
    try:
        mod_bus.Write_Register(25, 2, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 1')


def Shave1_bottom_door_open():
    try:
        mod_bus.Write_Register(25, 1, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 1')


def Shave1_bottom_door_close():
    try:
        mod_bus.Write_Register(25, 1, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей шкафа 1')


####################################
def table1_door_open():
    try:
        mod_bus.Write_Register(24, 1, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей cтол 1')


def table1_door_close():
    try:
        mod_bus.Write_Register(24, 1, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером дверей cтол 1')


####################################
#### Buttons #######################
####################################
def check_ligt_switch():

    print('light checker')
    lt1 = False
    lt2 = False
    l1 = False
    l2 = False
    try:
        if config.light_active:
            print('light')
            if config.switch1_add:
                sleep(0.1)
                get1 = mod_bus.Read_Registers(23, 8, 1)[0]
                sleep(0.1)
                ######
                if config.lamps_on_table:
                    if check_rfid_table_1():
                        lamp1_table_On()
                    else:
                        lamp1_table_Off()
                ######
                if config.switch1status != get1:
                    lamp2_On()
                    lamp2_table_On()
                    lamp1_Off()
                    if not config.child_mode:
                        lamp1_table_Off()
                    config.switch1_add = False
                    config.switch2_add = True
                    sleep(0.1)
                    config.switch2status = mod_bus.Read_Registers(23, 7, 1)[0]
                    sleep(0.1)

            if config.switch2_add:
                sleep(0.1)
                get2 = mod_bus.Read_Registers(23, 7, 1)[0]
                sleep(0.1)
                ######
                if config.lamps_on_table:
                    if check_rfid_table2():
                        lamp2_table_On()
                    else:
                        lamp2_table_Off()
                ######
                if config.switch2status != get2:
                    lamp1_On()
                    lamp1_table_On()
                    lamp2_Off()
                    if not config.child_mode:
                        lamp2_table_Off()
                    config.switch1_add = True
                    config.switch2_add = False
                    sleep(0.1)
                    config.switch1status = mod_bus.Read_Registers(23, 8, 1)[0]
                    sleep(0.1)

        if mod_bus.Read_Registers(23, 3, 1)[0] == 0:
            lt1 = False
        else:
            lt1 = True

        if mod_bus.Read_Registers(23, 1, 1)[0] == 0:
            lt2 = False
        else:
            lt2 = True

        if mod_bus.Read_Registers(23, 2, 1)[0] == 0:
            l2 = False
        else:
            l2 = True

        if mod_bus.Read_Registers(10, 1, 1)[0] == 0:
            l1 = False
        else:
            l1 = True
        if config.lamp_drag[0]==1:
            config.lamp_drag[0]=0
            if l1:
                lamp1_Off()
            else:
                lamp1_On()
        if config.lamp_drag[1]==1:
            config.lamp_drag[1]=0
            if lt1:
                lamp1_table_Off()
            else:
                lamp1_table_On()
        if config.lamp_drag[2]==1:
            config.lamp_drag[2]=0
            if l2:
                lamp2_Off()
            else:
                lamp2_On()
        if config.lamp_drag[3]==1:
            config.lamp_drag[3]=0
            if lt2:
                lamp2_table_Off()
            else:
                lamp2_table_On()
        config.lamp_stat = [l1, lt1, l2, lt2]

    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером при опросе выключателей')


####################################
#### DOORS #########################
####################################
def door2_open():
    try:
        mod_bus.Write_Register(25, 3, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером при открытии дверь 2')


def door2_close():
    try:
        mod_bus.Write_Register(25, 3, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером при закрытии дверь 2')


def door2_isop():
    if mod_bus.Read_Registers(25, 3, 1)[0] == 1:
        return True
    else:
        return False


####################################
def door1_turn():
    try:
        mod_bus.Write_Register(22, 4, 1)
        sleep(0.5)
        mod_bus.Write_Register(22, 4, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с основным контроллером при откр\закр дверь 1')


####################################
####         PHONES     ############
####################################
def phone_on():
    try:
        mod_bus.Write_Register(22, 1, 1)
    except ReferenceError:
        config.messages_label.append('Нет связи с тлф')


def phone_off():
    try:
        mod_bus.Write_Register(22, 1, 0)
    except ReferenceError:
        config.messages_label.append('Нет связи с тлф')


def phone_ring():
    try:
        mod_bus.Write_Register(22, 3, 1)
        sleep(1)
        mod_bus.Write_Register(22, 3, 0)
    except ReferenceError:
        config.messages_label.append('Нет связи с тлф')


def phone_established():
    try:
        get1 = mod_bus.Read_Registers(22, 7, 1)[0]
        if get1 == 1:
            return True
        else:
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с тлф')


####################################


def phone_checker():
    print('phone checker')
    # print(config.phone_label_text)
    if not config.phone_on_flag:
        config.phone_label_text = 'Телефоны выключены'
        phone_off()
    else:

        config.autodial_ready = False
        phone_on()

    if config.phone_on_flag:
        if phone_established():
            config.phone_label_text = 'Трубки сняты'
            config.dial_sended = False
            config.ring_trig = False
            config.autodial_ready = True
            return True
        config.autodial_ready = False
        if config.ring_trig == True and config.dial_sended == False:
            phone_ring()
            config.dial_sended = True
            config.ring_trig = False
        # if config.autodial_trig==True and config.dial_sended == False:
        #    phone_ring()
        #   config.dial_sended = True
        #   config.autodial_trig = False
        if config.dial_sended:
            config.phone_label_text = 'Звонок отправлен'
            return False




####################################
###         windows     ############
####################################
def window_drag():
    try:
        lamp1_speed(100)
        lamp1_table_Off()
        mod_bus.Write_Register(23, 4, 1)
        lamp1_bright(0)
        sleep(0.5)
        mod_bus.Write_Register(23, 4, 0)

        lamp1_speed(15000)
        lamp1_bright(100)

    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером при опускании окна')


def tape_drag():
    try:
        mod_bus.Write_Register(23, 5, 1)
        sleep(1)
        mod_bus.Write_Register(23, 5, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с контроллером при снятии завесы')


####################################
###         cases    ############
####################################
async def case_checker():
    try:
        loop = 1
        set = 0
        if loop == 1 and config.go == True and config.step == 10:
            for x in range(6, 1, -1):
                set = 0
                await asyncio.sleep(0.5)
                mod_bus.Write_Register(20, x, 1)
                mod_bus.Write_Register(21, x-1, 1)
                if mod_bus.Read_Registers(20, 8, 1)[0] == 1 or mod_bus.Read_Registers(21, 7, 1)[0] == 0 or \
                        mod_bus.Read_Registers(21, 8, 1)[0] == 0 or mod_bus.Read_Registers(20, 8, 1)[0] == 1:
                    set = 1
                await asyncio.sleep(0.5)
                if mod_bus.Read_Registers(20, 8, 1)[0] == 1 or mod_bus.Read_Registers(21, 7, 1)[0] == 0 or \
                        mod_bus.Read_Registers(21, 8, 1)[0] == 0 or mod_bus.Read_Registers(20, 8, 1)[0] == 1:
                    set = 1
                mod_bus.Write_Register(20, x, 0)
                mod_bus.Write_Register(21, x-1, 0)
                if config.step != 10:
                    break
            await asyncio.sleep(0.2)
            mod_bus.Write_Register(20, 1, 1)
            mod_bus.Write_Register(21, 6, 1)
            await asyncio.sleep(0.3)
            if config.easy_case:
                set=0
            if set == 0 and mod_bus.Read_Registers(20, 7, 1)[0] == 1 and mod_bus.Read_Registers(21, 8, 1)[0] == 0 and \
                    mod_bus.Read_Registers(21, 7, 1)[0] != 0 and mod_bus.Read_Registers(20, 8, 1)[0] != 1:
                mod_bus.Write_Register(20, 1, 0)
                mod_bus.Write_Register(21, 6, 0)
                loop = 0
                return True
            await asyncio.sleep(0.5)
            set = 0
            mod_bus.Write_Register(20, 1, 0)
            mod_bus.Write_Register(21, 6, 0)
            return False
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с чумаданами')


####################################
###        CODE         ############
####################################
def lock_clock_on():
    try:
        mod_bus.Write_Register(30, 0, 1)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с часами')


def code_erase():
    try:
        mod_bus.Write_Register(30, 1, 0)
        mod_bus.Write_Register(30, 2, 0)
        mod_bus.Write_Register(30, 3, 0)
        mod_bus.Write_Register(30, 4, 0)
        mod_bus.Write_Register(30, 5, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с часами')


def lock_clock_off():
    try:
        mod_bus.Write_Register(30, 0, 0)
    except ReferenceError:
        config.allert_messages_label.append('Нет связи с часами')


def lock_clock_check():
    try:
        var = (0, 0, 0, 0, 0,)
        var = mod_bus.Read_Registers(slave_addr=30, start_reg=1, num_of_regg=5)

        if var == config.PROPER_CODE:
            code_erase()
            return 'proper'
        if var == config.NONE_CODE:
            return 'none'
        else:
            code_erase()
            return 'fail'

    except ReferenceError:
        config.allert_messages_label.append('Нет связи с часами')

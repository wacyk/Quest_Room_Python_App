# -*- coding: utf-8 -*-
from datetime import datetime


switch1status =0
switch2status = 0
switch1_add=False
switch2_add=True
# ######################RFID IDs
RFID1_ID=(2, 49, 50, 48, 48, 57, 56, 48, 48, 68, 70, 53, 53, 3, )
RFID2_ID=(2, 49, 53, 48, 48, 50, 70, 48, 50, 70, 48, 67, 56, 3, )
RFID3_ID=(2, 53, 48, 48, 48, 54, 65, 68, 68, 68, 70, 51, 56, 3, )
RFID4_ID=(2, 49, 50, 48, 48, 55, 56, 68, 54, 55, 50, 67, 69, 3, )
RFID5_ID=(2, 49, 50, 48, 48, 57, 56, 49, 70, 53, 49, 67, 52, 3, )
RFID6_ID=(2, 49, 50, 48, 48, 56, 65, 67, 50, 65, 52, 70, 69, 3, )
RFID7_ID=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, )
#########################BUS SETTINGS
RS485_TRIES=10 # TRY_ONE_BY_ONE_TIMES
PORT = 'COM9' # usually can be checked in device manager - > COM-ports
#########################PHONES
phone_label_text = ' телефоны выключены'
autodial_trig = False
autodial_in_msec = 8000
dial_sended = False
ring_trig = False
phone_on_flag = False
autodial_sended = False
autodial_ready = True
#########################LIGHT CONTROL
child_mode = False
light_active = True
light_permission_txt = 'Право на выключатель: ----- -'
lamp_stat = [False, False, False, False]
lamp_drag=[0,0,0,0]
lamps_on_table=False
#########################GLOBAL FLAGS
pwr_on_flag= False
Idle_set = True
easy_case = False
#########################MAGNETS
MAGNET_prepare_TRIES=40
MAGNET_PAUSE = 1
MAGNET_TRIES = 5
manual_door = False
door_between_is_open=False
#########################MAIN GO
step_to_set=0
step=-1
go= False
current_step_label = ['Welcome to the QUESTER CONTROL ROOM V.1.5 ALPHA']
messages_label = []
allert_messages_label = []
scene_rate = 0.1
#########################CODE
PROPER_CODE =  (3, 1, 4, 6, 255, )
NONE_CODE =  (0, 0, 0, 0, 0, )
n=0
#########################GUI
prepare=False
scene_step= ['шаг 0 - Завести игроков в комнаты', 'шаг 1 - Поднять трубку',
             'шаг 2 - Установить предмет на стол 2', 'шаг 3 - Открыть верхнюю дверь шкафа 1',
             'шаг 4 - Установить предмет на стол 1',
             'шаг 5 - Открыть верхнюю дверь шкафа 2',
             'шаг 6 - Поставить книгу на шкаф 2', 'шаг 7 - Открыть дверь в столе 1',
             'шаг 8 - Поставить предмет в шкаф 1', 'шаг 9 - Открыть нижние двери в обоих шкафах',
             'шаг 10 - Кнопки в чумаданах', 'шаг 11 - Повесить любую из картин на место',
             'шаг 12 - Опускание завесы', 'шаг 13 - Повесить еще одну картину на место',
             'шаг 14 - Ввести код', 'шаг 15 - УДАР!!!', 'Завершить']

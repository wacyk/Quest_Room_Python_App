# -*- coding: utf-8 -*-
from tkinter import *
import config
import main
from datetime import datetime
from time import  sleep

root = Tk()
val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()
val6 = IntVar()

def chl1():
    config.lamp_drag[0]=1


def chl2():
    config.lamp_drag[1] = 1


def chl3():
    config.lamp_drag[2] = 1


def chl4():
    config.lamp_drag[3] = 1


def power_on():
    if not config.pwr_on_flag:
        main.power_on()
        button1_['fg'] = 'green'
        button4_['fg'] = 'blue'


def power_off():
    if config.pwr_on_flag == True :
        main.power_off()
        button1_['fg'] = 'black'
        button4_['fg'] = 'black'

def start():
    if  config.pwr_on_flag == True and config.prepare == False:
        main.go_func()
        config.current_step_label.append('Сценарий запущен!')
        button1_['fg'] = 'black'
        button3_['fg'] = 'red'
        button4_['fg'] = 'black'


def autodial():
    main.autodial()


def prepare():
    if config.pwr_on_flag == True and config.prepare == False and config.step not in range(0,17):
        button1_['fg'] = 'black'
        button4_['fg'] = 'black'
        button3_['fg'] = 'red'

        main.prepare()


def stop():
    if config.step in range(0,17) or config.step == -2 or config.prepare:
        config.current_step_label.append('Сценарий остановлен оператором')
        if config.step in range(0, 18):
            main.stop()
        config.prepare = False




def step_up():
    if config.step_to_set < 16:
        config.step_to_set += 1
        label_txt_step_['text'] = config.scene_step[config.step_to_set]


def step_down():
    if config.step_to_set > 0:
        config.step_to_set -= 1
        label_txt_step_['text'] = config.scene_step[config.step_to_set]


def call_phones():
    if config.go:

        if config.autodial_ready!= True and config.dial_sended:
            config.dial_sended = False
            config.autodial_ready=False
            config.phone_on_flag = False
            sleep(1)

            button2_['text'] = 'ПОЗВОНИТЬ'
            label_phone_update()
        else:
            config.phone_on_flag = True
            config.ring_trig = True
            button2_['text']='Отменить'
            label_phone_update()
def change_step():
    if config.step in range(0,17):
        config.step = config.step_to_set
        config.current_step_label.append('Шаг изменен на ' + str(config.step))
        label_phone_update()


def drag_door():
    if config.pwr_on_flag:
        main.drag_doorbeetwin()


######## UPDATE IFACE##########################
def label_phone_update():
    label_phone_.after(100, label_phone_update)
    label_phone_['text'] = config.phone_label_text
    if config.current_step_label:
        config.n = 0
        for config.n in config.current_step_label:
            text1.insert(END, '[' + str(datetime.strftime(datetime.now(), "%H:%M:%S")) + ']   ' + config.n + '\n', 'bl')
        config.current_step_label = []
        text1.yview_moveto(1)
    if config.messages_label:
        config.n = 0
        for config.n in config.messages_label:
            text1.insert(END, '[' + str(datetime.strftime(datetime.now(), "%H:%M:%S")) + ']   ' + config.n + '\n',
                         'blu')
        config.messages_label = []
        text1.yview_moveto(1)
    if config.allert_messages_label:
        config.n = 0
        for config.n in config.allert_messages_label:
            text1.insert(END, '[' + str(datetime.strftime(datetime.now(), "%H:%M:%S")) + ']   ' + config.n + '\n',
                         'red')
        config.allert_messages_label = []
        text1.yview_moveto(1)
    #
    if val1.get() == 1:
        config.child_mode = True
    else:
        config.child_mode = False

    if val6.get() == 1:
        config.lamps_on_table = True
    else:
        config.lamps_on_table = False

    if val3.get() == 1:
        config.manual_door = True
    else:
        config.manual_door = False
    if val4.get() == 1:
        config.easy_case = True
    else:
        config.easy_case = False

   # if val2.get() == 1 and config.autodial_sended == False and config.dial_sended == False and config.go == True and 10 > config.step > 1:
    #    config.phone_on_flag = True
    #    config.autodial_sended = True
     #   config.messages_label.append('Автодозвон через ' + str(config.autodial_in_msec / 1000) + ' секунд')
    #    autodial_.after(config.autodial_in_msec, autodial)

    if config.step in range(0, 17):
        label_step_['text'] = str(config.step)

    if config.switch1_add:
        light_permission_label['text'] = 'Право на выключатель: игрок 1'
    if config.switch2_add:
        light_permission_label['text'] = 'Право на выключатель: игрок 2'
    if not config.light_active:
        light_permission_label['text'] = 'Право на выключатель: никому'

    if config.lamp_stat[0]==True:
        l1_['fg'] = 'green'
    else:
        l1_['fg'] = 'black'

    if config.lamp_stat[1]==True:
        l2_['fg'] = 'green'
    else:
        l2_['fg'] = 'black'

    if config.lamp_stat[2]==True:
        l3_['fg'] = 'green'
    else:
        l3_['fg'] = 'black'

    if config.lamp_stat[3]==True:
        l4_['fg'] = 'green'
    else:
        l4_['fg'] = 'black'

    if config.door_between_is_open:
        dl_['text'] = 'Дверь между комнатами открыта'
        dl_['fg'] = 'red'
    else:
        dl_['text'] = 'Дверь между комнатами закрыта'
        dl_['fg'] = 'blue'
    if config.step==-2:
        button1_['fg'] = 'green'
        button3_['fg'] = 'black'
        button4_['fg'] = 'blue'




######################################
root.geometry('1200x720+0+0')
root.title('QUESTER CONTROL ROOM V.1.5 ALPHA')
root.configure(background='grey')
button1_ = Button(root, text='СТАРТ', width=12, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 14', command=start)
button2_ = Button(root, text='ПОЗВОНИТЬ', width=20, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=call_phones)
button3_ = Button(root, text='ОСТАНОВ', width=12, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 14', command=stop)
button4_ = Button(root, text='ПОДГОТОВКА', width=12, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 14', command=prepare)
button6_ = Button(root, text='ВКЛ. ПИТ. СИСТЕМЫ', width=20, height=2, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=power_on)
button7_ = Button(root, text='ОТКЛ. ПИТ. СИСТЕМЫ', width=20, height=2, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=power_off)
button8_ = Button(root, text='  <<  ', width=6, height=2, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=step_down)
button9_ = Button(root, text='  >>  ', width=6, height=2, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=step_up)
go_ = Button(root, text='GO', width=10, height=2, bg='grey', fg='black', activebackground='blue',
             activeforeground='white', font='arial 9', command=change_step)

drag_l1_ = Button(root, text='on/off', width=10, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=chl1)
drag_l2_ = Button(root, text='on/off', width=10, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=chl2)
drag_l3_ = Button(root, text='on/off', width=10, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=chl3)
drag_l4_ = Button(root, text='on/off', width=10, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=chl4)
drag_door_ = Button(root, text='onpen/close', width=10, height=1, bg='grey', fg='black', activebackground='blue',
                  activeforeground='white', font='arial 9', command=drag_door)

label_phone_ = Label(root, text=config.phone_label_text, width=24, height=2, bg='grey', fg='black', font='arial 14')
label_step_ = Label(root, text='--', width=2, height=1, bg='grey', fg='blue', font='arial 16')
label_txt_ = Label(root, text='Ручное управление сценарием:', width=26, height=1, bg='grey', fg='black',
                   font='arial 14')
label_txt_step_ = Label(root, text=config.scene_step[config.step_to_set], width=48, height=1, bg='grey', fg='black',
                        font='arial 14')
light_permission_label = Label(root, text=config.light_permission_txt, width=48, height=1, bg='grey', fg='black',
                               font='arial 12')
child_mode_flag_ = Checkbutton(root, background='grey', width=24, height=1, text='Лампы на столах всегда Вкл',
                               fg='black', font='arial 12', variable=val1, onvalue=1, offvalue=0)
easy_case_flag_ = Checkbutton(root, background='grey', width=15, height=1, text='EASY чумаданы',
                               fg='black', font='arial 12', variable=val4, onvalue=1, offvalue=0)
autodial_ = Checkbutton(root, background='grey', width=24, height=1, text='Автодозвон', fg='black', font='arial 12',
                        variable=val2, onvalue=1, offvalue=0)
manual_door_ = Checkbutton(root, background='grey', width=43, height=1, text='Защелки срабатывают бесконечно',
                           fg='black', font='arial 12', variable=val3, onvalue=1, offvalue=0)
lamps_always_ = Checkbutton(root, background='grey', width=25, height=1, text='Лампы светят, если на месте',
                           fg='black', font='arial 12', variable=val6, onvalue=1, offvalue=0)
l1_ = Label(root, text='Л1', width=10, height=1, bg='grey', fg='black', font='arial 14')
l2_ = Label(root, text='ЛС1', width=10, height=1, bg='grey', fg='black', font='arial 14')
l3_ = Label(root, text='Л2', width=10, height=1, bg='grey', fg='black', font='arial 14')
l4_ = Label(root, text='ЛС2', width=10, height=1, bg='grey', fg='black', font='arial 14')
dl_ = Label(root, text='Дверь между комнатами: ------', width=36, height=1, bg='grey', fg='black', font='arial 14')

text1 = Text(root, font='arial 14', wrap=WORD, bg='grey', fg='orange', bd=8)
text1.place(x=10, y=10, height=700, width=450)
scrollbar = Scrollbar(root, bg='black')
scrollbar.place(x=460, y=10, height=700)
# первая привязка
scrollbar['command'] = text1.yview
# вторая привязка
text1['yscrollcommand'] = scrollbar.set

text1.tag_add('blu', '0.0')
text1.tag_config('blu', foreground='blue', wrap=WORD, font='Arial 12')
text1.tag_add('bl', '0.0')
text1.tag_config('bl', foreground='black')
text1.tag_add('red', '0.0')
text1.tag_config('red', foreground='red')

button1_.place(x=1030, y=50)
button2_.place(x=580, y=10)
button3_.place(x=1030, y=110)
button4_.place(x=1030, y=170)
button6_.place(x=1030, y=550)
button9_.place(x=700 + 90, y=600)
button7_.place(x=1030, y=610)
button8_.place(x=525 + 90, y=600)
go_.place(x=600 + 90, y=600)
drag_l1_.place(x=500, y=300)
drag_l2_.place(x=600, y=300)
drag_l3_.place(x=700, y=300)
drag_l4_.place(x=800, y=300)
drag_door_.place(x=900, y=370)
l1_.place(x=485, y=270)
l2_.place(x=585, y=270)
l3_.place(x=680, y=270)
l4_.place(x=780, y=270)
dl_.place(x=490, y=370)
label_step_.place(x=625 + 90, y=645)
label_txt_step_.place(x=455, y=540)
label_phone_.place(x=500, y=50)
label_txt_.place(x=500, y=500)
child_mode_flag_.place(x=575, y=150)
easy_case_flag_.place(x=570, y=100)
#autodial_.place(x=570, y=100)
light_permission_label.place(x=480, y=240)
manual_door_.place(x=513, y=200)
lamps_always_.place(x=730, y=100)
label_phone_.after(1000, label_phone_update)

root.mainloop()

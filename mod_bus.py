# -*- coding: utf-8 -*-
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu
import serial
import config

def open_port():
    try:
        global master
        master = modbus_rtu.RtuMaster(serial.Serial(port=config.PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0, ))
        master.set_timeout(0.15) # 0.3 OК
        config.messages_label.append('Порт '+ config.PORT + 'Открыт успешно')

        return True
    except serial.serialutil.SerialException:
        config.allert_messages_label.append('Не могу открыть порт '+ config.PORT + '\n 1. Проверьте соединение с переходником \n 2. Убедитесь что порт указан верно (cм. в диспетчере устройств Windows)')
        return False


##############################################################################################################
##############################################################################################################
def Read_Registers(slave_addr, start_reg, num_of_regg):

    global master
    eer_cnt=0
    eer=True
    ret = (0, )
    while eer:
        try:
            ret = master.execute(slave_addr, cst.READ_HOLDING_REGISTERS, start_reg, num_of_regg)
            eer = False
            if eer_cnt!=0:
                config.messages_label.append('Реконнект удался!')
            return ret
        except (modbus_tk.exceptions.ModbusInvalidRequestError, modbus_tk.exceptions.ModbusInvalidResponseError):
            eer=True
            eer_cnt+=1
            config.messages_label.append("Устройство с ИД № " + str(slave_addr) + " не отвечает на запросы чтения регистров, Попытка №" + str(eer_cnt))
            if eer_cnt == config.RS485_TRIES:
                raise ReferenceError

##############################################################################################################
##############################################################################################################
def Write_Register(slave_addr, reg, val):
    global master
    eer_cnt=0
    eer=True
    while eer:
        try:
            master.execute(slave_addr, cst.WRITE_SINGLE_REGISTER, reg, output_value=val  )
            eer=False
            if eer==False and eer_cnt!=0:
                config.messages_label.append('Реконнект удался!')
        except (modbus_tk.exceptions.ModbusInvalidRequestError, modbus_tk.exceptions.ModbusInvalidResponseError):
            eer=True
            eer_cnt+=1
            config.messages_label.append("Устройство с ИД № " + str(slave_addr) + " не отвечает на запросы записи регистров, Попытка №  " + str(eer_cnt))
            if eer_cnt == config.RS485_TRIES:
                raise ReferenceError



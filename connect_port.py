import serial.tools.list_ports


def ser_write(data):
    f_port = None
    print('Search...')
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("Ports not found")
        print("Возможно нет СОМ портов или не установлены драйвера")
        return

    for port in ports:
        if port.pid: f_port = port
        print('Find port ' + port.device)

    if not f_port:
        print("Device not found")
        print("Проверьте правильность подключения устройства в порт и попробуйте еще раз")
        return

    ser = serial.Serial(f_port.device)

    if ser.isOpen():
        ser.close()

    ser = serial.Serial(f_port.device, 9600, timeout=1)
    ser.flushInput()
    ser.flushOutput()
    print('Connect ' + ser.name)

    ser.write(data.encode())
    ser.close()


def ser_write_example(data):
    import random
    f_port = None
    print('Search...')

    ports = (("COM1", "COM2", "COM3:ASWE4565:PID0000", "COM4", "COM5"), [], ("COM3:ASWE4565:PID0000", "COM7", "COM8", "COM9", "COM10"))
    ports = random.choice(ports)
    if not ports:
        print("Port not found")
        print("Проверьте правильность подключения устройства в порт и попробуйте еще раз")
        return

    for port in ports:

        if port == "COM3:ASWE4565:PID0000": f_port = port
        print('Find port ' + port)

    if f_port:
        print('Connect ' + f_port.split(':')[0])
        print(f"Информация '{data}' отправлена на порт", f_port)


if __name__ == '__main__':
    ser_write_example('Hello')

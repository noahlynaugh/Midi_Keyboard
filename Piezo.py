from machine import Pin, ADC
import utime
import uos
import machine


#Creating a UART Object
uart = machine.UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
uos.dupterm(uart)



adc= ADC(Pin(26, Pin.IN))

conversion_factor = 3.3/65535

def cc(byte_cmd, byte_d1, byte_d2):

    print(byte_cmd)
    print(byte_d1)
    print(byte_d2)


while True:

    # print(adc.read_u16() * conversion_factor)
    
    if adc.read_u16()* conversion_factor>.9:
            print(adc.read_u16() * conversion_factor)
                    # uart.write(b'\x80\x3C\x7F')  
                    # x7F Replace this with the velocity
                    # // Try this if printing to python does not work//#
            # cc(144,60,adc.read_u16()/3.3)
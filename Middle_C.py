import time
import rtmidi
import serial

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports)

serial_connection = serial.Serial('/dev/cu.usbmodem2101',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE)
print("Serial_Port is {}".format(serial_connection.name))

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("IAC Driver Bus 1")

try: 
    while True:

        raw_line = serial_connection.readline()
        decoded_line = raw_line.decode('utf-8')
        stripped_line = decoded_line.strip('\r\n')
        
        print(decoded_line)

        if decoded_line == "toggle":
            print("toggle")
            with midiout:
                note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
                note_off = [0x80, 60, 0]
                midiout.send_message(note_on)
                time.sleep(0.5)
                midiout.send_message(note_off)
                time.sleep(0.1)

finally:    

    del midiout
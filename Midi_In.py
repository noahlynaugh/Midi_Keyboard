import mido
import time
import serial


# Print available MIDI output ports
print("Available MIDI Output Ports:")
for port in mido.get_output_names():
    print("Port={}".format(port))

# Replace 'Virtual Output' with the actual name of the IAC Driver port
virtual_port_name = port
# Create a virtual MIDI port
virtual_port = mido.open_output(virtual_port_name)

serial_connection = serial.Serial('/dev/cu.usbmodem101',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE)
print("Serial_Port is {}".format(serial_connection.name))


try:

        # Function to send a MIDI note-on message
        def send_note_on(note, velocity):
            msg = mido.Message('note_on', note=note, velocity=velocity)
            virtual_port.send(msg)

        # Function to send a MIDI note-off message
        def send_note_off(note):
            msg = mido.Message('note_off', note=note)
            virtual_port.send(msg)

        # Play a C4 note 
        note_to_play = 60  # MIDI note number for C4
        note_to_play2 = 61  # MIDI note number for C#4
        note_to_play3 = 62  # MIDI note number for D
        note_to_play4 = 63  # MIDI note number for d#
        note_to_play5 = 64  # MIDI note number for e
        note_to_play6 = 65  # MIDI note number for F
        note_to_play7 = 66  # MIDI note number for f#
        note_to_play8 = 67  # MIDI note number for G
        note_to_play9 = 68  # MIDI note number for g#
        note_to_play10 = 69  # MIDI note number for a
        note_to_play11 = 70  # MIDI note number for a#
        note_to_play12 = 71  # MIDI note number for b
        velocity = 64      # Velocity (volume) of the note


        # Midi control change #7 - Volume



        while True:
            raw_line = serial_connection.readline()
            decoded_line = raw_line.decode('utf-8')
            stripped_line = decoded_line.strip('\r\n')
            print(decoded_line)
            if stripped_line == "C":
                send_note_on(note_to_play, velocity)
                if stripped_line == "stop":
                    send_note_off(note_to_play)
            if stripped_line == "C#":
                send_note_on(note_to_play2, velocity)
            send_note_off(note_to_play2)
            if stripped_line == "d":
                send_note_on(note_to_play3, velocity)
            send_note_off(note_to_play3)
            if stripped_line == "d#":
                send_note_on(note_to_play4, velocity)
            send_note_off(note_to_play4)
            if stripped_line == "e":
                send_note_on(note_to_play5, velocity)
            send_note_off(note_to_play5)
            if stripped_line == "f":
                send_note_on(note_to_play6, velocity)
            send_note_off(note_to_play6)
            if stripped_line == "f#":
                send_note_on(note_to_play7, velocity)
            send_note_off(note_to_play7)
            if stripped_line == "g":
                send_note_on(note_to_play8, velocity)
            send_note_off(note_to_play8)
            if stripped_line == "g#":
                send_note_on(note_to_play9, velocity)
            send_note_off(note_to_play9)
            if stripped_line == "a":
                send_note_on(note_to_play10, velocity)
            send_note_off(note_to_play10)
            if stripped_line == "a#":
                send_note_on(note_to_play11, velocity)
            send_note_off(note_to_play11)
            if stripped_line == "b":
                send_note_on(note_to_play12, velocity)
            send_note_off(note_to_play12)
finally:
    # Close the virtual port
    virtual_port.close()
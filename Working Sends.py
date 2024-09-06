import mido
import time
import serial

# Print available MIDI output ports
print("Available MIDI Output Ports:")
for port in mido.get_output_names():
    print("Port={}".format(port))

# Choose a MIDI port
port_name = "IAC Driver Bus 1"
# input("Enter the name of the MIDI port to use: ")

# Create a virtual MIDI port
virtual_port = mido.open_output(port_name)


serial_connection = serial.Serial('/dev/cu.usbmodem101',
                                  baudrate=115200,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE)
print("Serial_Port is {}".format(serial_connection.name))

try:
    while True:
        # Read the byte array sent by the Pico
        data = serial_connection.readline()

        # Decode the received data to bytes
        data_bytes = data.decode('utf-8')
        
        # Strip unnecessary characters from the string
        stripped_data = data_bytes.strip()
        
        # Process the byte array as needed
        print("Received data:", stripped_data)

        # Example: Process MIDI message
        if stripped_data:
            # Remove the brackets and split the string by commas
            data_parts = stripped_data[1:-1].split(", ")

            # Convert each part to an integer
            status = int(data_parts[0])
            note = int(data_parts[1])
            velocity = int(data_parts[2])
     
            # Create MIDI message based on the status byte
            if status == 0x90:  # Note On message
                msg = mido.Message('note_on', note=note, velocity=velocity)
            elif status == 0x80:  # Note Off message
                msg = mido.Message('note_off', note=note, velocity=velocity)
                
            # # Send the MIDI message to the virtual MIDI port
            virtual_port.send(msg)
        else:
            print("Invalid data format:", stripped_data)

            

finally:
    # Close the virtual port
    virtual_port.close()

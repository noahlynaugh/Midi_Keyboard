from machine import Pin
from utime import sleep, ticks_ms
import uos
import machine

print("running program")

# LED and Button Variables
led=Pin("LED", Pin.OUT)
LEDS = [
Pin(15, Pin.OUT),
Pin(14, Pin.OUT),
Pin(13, Pin.OUT),
Pin(12, Pin.OUT),
Pin(11, Pin.OUT),
Pin(10, Pin.OUT),
Pin(9, Pin.OUT),
Pin(8, Pin.OUT),
Pin(7, Pin.OUT),
Pin(6, Pin.OUT),
Pin(5, Pin.OUT),
Pin(4, Pin.OUT)]
BTNS = [
Pin(2, Pin.IN, Pin.PULL_DOWN),
Pin(3, Pin.IN, Pin.PULL_DOWN),
Pin(27, Pin.IN, Pin.PULL_DOWN),
Pin(26, Pin.IN, Pin.PULL_DOWN),
Pin(22, Pin.IN, Pin.PULL_DOWN),
Pin(21, Pin.IN, Pin.PULL_DOWN),
Pin(20, Pin.IN, Pin.PULL_DOWN),
Pin(19, Pin.IN, Pin.PULL_DOWN),
Pin(28, Pin.IN, Pin.PULL_DOWN),
Pin(18, Pin.IN, Pin.PULL_DOWN),
Pin(17, Pin.IN, Pin.PULL_DOWN),
Pin(16, Pin.IN, Pin.PULL_DOWN)]

# Debounce time in milliseconds
debounce_time = 500

#Creating a UART Object
uart = machine.UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
uos.dupterm(uart)

# Initialize note states
note_states = [False] * len(BTNS)
last_pressed_times = [0] * len(BTNS)

# Chromatic scale notes
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_on_off(btn, idx):
    global note_states, last_pressed_times

    if btn.value() == 1:
        if not note_states[idx] and ticks_ms() - last_pressed_times[idx] > debounce_time:
            last_pressed_times[idx] = ticks_ms()
            note_states[idx] = True
            midi_note = 60 + idx  # MIDI note number for C is 60
            data = ([0x90, midi_note, 0x7F])  # Note On message
            # uart.write(data)
            print(data)  # Print the data being sent
    else:
        if note_states[idx]:
            note_states[idx] = False
            midi_note = 60 + idx  # MIDI note number for C is 60
            data = ([0x80, midi_note, 0x00])  # Note Off message
            # uart.write(data)
            print(data)  # Print the data being sent

    sleep(0.01)  # Adding a small delay to avoid busy looping

try:
    led.on()
    while True:
        for idx, note in enumerate(BTNS):
            # print(note.value())
            note_on_off(note, idx)
            


finally:
    led.off()
    for note in LEDS:
        note.off()
from pythonosc import osc_message_builder
from pythonosc import udp_client
import serial
import sys
import time

# select the correct port and baud rate
ser = serial.Serial('COM3', 9600)

while True:
    try:
        ser_bytes = ser.readline()
        serialVal = str(ser_bytes, 'ascii').strip()
        if (serialVal == "0"):
            sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
            #sender.send_message('/trigger/prophet', [43, 53, 57, 58, 62])
            sender.send_message('/trigger/prophet', [80,71,1])
            time.sleep(2)

        if (serialVal == "1"):
            sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
            #sender.send_message('/trigger/prophet', [43, 53, 57, 58, 62])
            sender.send_message('/trigger/pulse', [80,71,1])
            time.sleep(2)


    except:
        print(sys.exc_info()[0])
        break


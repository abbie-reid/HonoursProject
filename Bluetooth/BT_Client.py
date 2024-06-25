# Code from pybluez - https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-client.py


import sys
import bluetooth

jeston_nano_4_uuid = "00001800-0000-1000-8000-00805f9b34fb"
server_name = "JetsonNano4"

addr = None

if len(sys.argv) < 2:
    print("No device specified. Searching all nearby bluetooth devices for "
          "the SampleServer service...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on {}...".format(addr))

# search for the SampleServer service
service_matches = bluetooth.find_service(uuid=jetson_nano_4_uuid, address=addr)

if len(service_matches) == 0:
    print("Couldn't find the SampleServer service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected. Type something...")
while True:
    data = input()
    if not data:
        break
    sock.send(data)

sock.close()

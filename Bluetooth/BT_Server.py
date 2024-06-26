# Code from Pybluez - https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-server.py

import bluetooth

print(bluetooth.read_local_bdaddr())

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

jetson_nano_4_uuid = "00001800-0000-1000-8000-00805f9b34fb"
server_name = "JetsonNano4"

bluetooth.advertise_service(server_sock, server_name, service_id=jetson_nano_4_uuid,
	                    service_classes=[jetson_nano_4_uuid, bluetooth.SERIAL_PORT_CLASS],
	                    )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

try:
	while True:
		data = client_sock.recv(1024)
		if not data:
		    break
		print("Received", data)
except OSError:
	pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done.")

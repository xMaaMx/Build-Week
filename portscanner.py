import socket

indirizzo_ip = input('Inserisci indirizzo ip: ')
porte = input('Inserire un range di porte (valore minimo 0, valore massimo 65.535): ')

minporta = int(porte.split('-')[0])
massporta = int(porte.split('-')[1])


print('Scansione IP: ', indirizzo_ip, 'dalla porta', minporta, 'alla porta',massporta)

massporta = int(porte.split('-')[1])+1

for port in range(minporta, massporta ):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	status = sock.connect_ex((indirizzo_ip, port))
	if(status == 0):
		print('Port',port,'- OPEN')

	sock.close()

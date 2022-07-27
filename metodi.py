import http.client

host = input ('Inserire IP del sistema target: ')
porta = input('Inserire la pota del sitema target(default:80): ')

if(porta == ''):
	porta = 80
try:
	connessione_0 = http.client.HTTPConnection(host, porta)
	connessione_1 = http.client.HTTPConnection(host, porta)
	connessione_2 = http.client.HTTPConnection(host, porta)
	connessione_3 = http.client.HTTPConnection(host, porta)
	connessione_4 = http.client.HTTPConnection(host, porta)
	connessione_5 = http.client.HTTPConnection(host, porta)
	#connessione_6 = http.client.HTTPConnection(host, porta)
	connessione_0.request('GET','/phpMyAdmin/')
	connessione_1.request('POST','/phpMyAdmin/')
	connessione_2.request('PUT','/phpMyAdmin/')
	connessione_3.request('HEAD','/phpMyAdmin/')
	connessione_4.request('DELETE','/phpMyAdmin/')
	connessione_5.request('OPTION','/phpMyAdmin/')
	#connessione_6.request('PATCH','/phpMyAdmin/')
	risposta_0 = connessione_0.getresponse()
	risposta_1 = connessione_1.getresponse()
	risposta_2 = connessione_2.getresponse()
	risposta_3 = connessione_3.getresponse()
	risposta_4 = connessione_4.getresponse()
	risposta_5 = connessione_5.getresponse()
	#risposta_6 = connessione_6.getresponse()
	print('Il metodo GET è: ',risposta_0.status, risposta_0.reason)
	print('Il metodo POST è: ',risposta_1.status, risposta_1.reason)
	print('Il metodo PUT è: ',risposta_2.status, risposta_2.reason)
	print('Il metodo HEAD è: ',risposta_3.status, risposta_3.reason)
	print('Il metodo DELETE è: ',risposta_4.status, risposta_4.reason)
	print('Il metodo OPTION è: ',risposta_5.status, risposta_5.reason)
	#print('Il metodo PATCH è: ',risposta_6.status, risposta_6.reason)
	connessione_0.close()
	connessione_1.close()
	connessione_2.close()
	connessione_3.close()
	connessione_4.close()
	connessione_5.close()
	#connessione_6.close()

except ConnectionRefusedError:
	print('Connessione fallita')import http.client

host = input ('Inseirire IP del sistema target: ')
porta = input ( 'Inserire la pota del sistema target(default:80): ')

if(porta == ''):
		porta = 80
try:
		connessione = http.client.HTTPConnection(host, porta)
		connessione.request('OPTION', '/phpMyAdmin/')
		risposta = connessione.getresponse()
		print('I metodi abilitati sono:', risposta.status, risposta.reason)
		connessione.close()
except ConnectionRefusedError:
	print('Connessione fallita')


import http.client

host = input ('Inserire IP del sistema target: ')
porta = input('Inserire la porta del sistema target(default:80): ')
path = input('Inserire il path dove controllare i metodi abilitati: ')

if(porta == ''):
	porta = 80
try:
	connessione = http.client.HTTPConnection(host, porta)
	connessione.request('OPTIONS', path)
	risposta = connessione.getresponse()
	print(risposta.getheader('allow'))
	connessione.close()

except ConnectionRefusedError:
	print('Connessione fallita')

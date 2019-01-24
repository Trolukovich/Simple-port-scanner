import socket
from netaddr import iter_iprange


start = '212.85.101.181'
end = '212.85.101.185'
port = 21

ips = iter_iprange(start, end, step=1)
opened = []

while True:
	try:
		host = str(next(ips))
		s = socket.socket()
		s.settimeout(0.1)
		try:
			s.connect((host, port))
		except socket.error:
			print(host + ': {} port closed'.format(port))
			continue
		else:
			s.close
			print(host + ': {} port opened'.format(port))
			opened.append(host)
	except:
		print('\n/----------------SCAN COMPLETE---------------/\n')
		break

if opened:
	with open('opened.txt', 'w') as f:
		for ip in opened:
			f.write(ip + '\n')
	print('{} ips with opened {} port found'.format(len(opened), port))
	print('See "opened.txt" in script folder')
else:
	print('No opened ports found')
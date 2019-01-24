import socket
import ipaddress
from tkinter import *
from netaddr import iter_iprange


def scan():

	# Getting IPs and port from Entry
	start_ip = e_start_ip.get().strip()
	end_ip = e_end_ip.get().strip()
	port = e_port.get().strip()

	# Checking entered IPs and port
	if check_ip(start_ip, end_ip) and check_port(port):
		ips = iter_iprange(start_ip, end_ip, step=1)

		while True:
			try:
				host = str(next(ips))
				s = socket.socket()
				s.settimeout(0.1)
				try:
					s.connect((host, int(port)))
				except socket.error:
					t_status.insert(END, host + ' {} port closed\n'.format(port))
					t_status.see('end')
					continue
				else:
					s.close
					t_opened.insert(END, host + '\n')
					t_opened.see('end')
			except:
				t_status.insert(END, '\n/-------------SCAN COMPLETE------------/\n')
				t_status.see('end')
				break

	else:
		t_status.insert(END, 'Enter correct IP and port(0-65535)\n')
		t_status.see('end')
	
def check_ip(start, end):
	'''
	Validates IP addresses from IP Entries 
	'''
	try:
		ipaddress.ip_address(start)
		ipaddress.ip_address(end)
		return True
	except:
		return False

def check_port(port):
	'''
	Validates the port from port Entry
	'''
	try:
		if 0 <= int(port) <= 65535:
			return True
		else:
			return False
	except:
		return False


root = Tk()
root.resizable(False, False)
root.title('Simple port scanner')

up_frame = Frame()
dwn_frame = Frame()
data_frame = Frame(up_frame)
ip_frame = LabelFrame(data_frame, text='Address range')
ip_frame_t = Frame(ip_frame)
ip_frame_b = Frame(ip_frame)
port_frame = LabelFrame(data_frame, text='Port')
opened_frame = LabelFrame(up_frame, text='Opened')

e_start_ip = Entry(ip_frame_t, width=15)
e_end_ip = Entry(ip_frame_b, width=15)
e_port = Entry(port_frame, width=21)

l_start_ip = Label(ip_frame_t, text='Start')
l_end_ip = Label(ip_frame_b, text='End ')

b_scan = Button(data_frame, text='Scan', width=18, command=scan)

t_opened = Text(opened_frame, width=18, height=8)
t_status = Text(dwn_frame, width=40, height=8, bg='darkgreen', fg='white')

s_ip = Scrollbar(opened_frame, command=t_opened.yview)
s_st = Scrollbar(dwn_frame, command=t_status.yview)

up_frame.pack()
dwn_frame.pack()
data_frame.pack(side=LEFT, padx=4)
ip_frame.pack(padx=2, pady=2)
ip_frame_t.pack(padx=2, pady=2)
l_start_ip.pack(side=LEFT, padx=2, pady=2)
e_start_ip.pack(side=LEFT, padx=2, pady=2)
ip_frame_b.pack(padx=2, pady=2)
l_end_ip.pack(side=LEFT, padx=2, pady=2)
e_end_ip.pack(side=LEFT, padx=2, pady=2)
port_frame.pack(padx=2, pady=2)
e_port.pack(padx=4, pady=4)
b_scan.pack(padx=2, pady=2)

opened_frame.pack(side=LEFT, padx=4)
t_opened.pack(side=LEFT, padx=4, pady=4)
s_ip.pack(side=LEFT, fill=Y)
t_status.pack(side=LEFT, padx=4, pady=4)
s_st.pack(side=LEFT, fill=Y)

t_opened.config(yscrollcommand=s_ip.set)
t_status.config(yscrollcommand=s_st.set)
t_status.see(END)

root.mainloop()
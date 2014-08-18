import socket

def netcat(hostname, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((hostname, port))
	while 1:
		n = s.recv(1024)
		print "Received:", repr(n)
		data = s.recv(1024)
		print "Received:", repr(data)
		en1=int(data.split('\n')[1])
		en2=int(data.split('\n')[2])
		print(en1,en2)
		a=max(en2,en1)
		b=min(en2,en1)
		a=en2//en1
		b=en2-a*en1
		m=en1
		mmod=((a**2*m**3+a*b*m**2+b**2*m)/(a**2*m**2+a*b*m+b**2*1))
		print(a,b)
		print(mmod)
		s.sendall(str(mmod)+'\n')
		data = s.recv(1024)
		print "Received:", repr(data)

netcat('54.64.40.172',5454)

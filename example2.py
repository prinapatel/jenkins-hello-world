import time
import datetime as dt
import socket

i=1

host=socket.gethostbyname(socket.gethostname())

while True:
	print("From {}, the time is {}".format(host,dt.datetime.now().strftime("%H:%M:%S")))
	time.sleep(2)
	i+=1
	if i==10:break

